import copy
from pathlib import Path
import subprocess
import sys
import pytest
import diagnose as d

def test_public_question_hides_key_and_resume_keeps_question():
    state=d.start('a','math02.chain');first=d.next_question(state)
    assert 'answer' not in first and 'rubric' not in first and 'hints' not in first
    assert first==d.next_question(state)
    assert first['id'] in state['seen']

def test_error_goes_to_prerequisite_instead_of_repeating_solution():
    state=d.start('a','math02.chain');d.next_question(state)
    d.submit(state,'cos(x**2)')
    q=d.next_question(state)
    assert q['skill_id']=='math02.basic'
    d.submit(state,'cos(u)')
    assert d.next_question(state)['skill_id']=='math02.chain'

def test_hint_not_counted_as_independent_even_after_review():
    state=d.start('a','math02.basic');d.next_question(state);d.hint(state)
    ev=d.submit(state,'cos(u)');assert ev['verdict']=='assisted'
    d.amend(state,ev['id'],'correct','核验学生的公式与变量')
    assert ev['verdict']=='assisted' and state['corrections'][0]['before']['hint_level']==1
    assert d.status(state,'math02.basic')=='提示后完成'

def test_skip_and_pause_are_not_failures():
    state=d.start('a','math02.basic');d.next_question(state)
    state['phase']='paused'
    with pytest.raises(ValueError):d.submit(state,'cos(u)')
    state['phase']='diagnostic'
    ev=d.submit(state,'不会',True)
    assert ev['verdict']=='skip' and not d.evidence(state,'math02.basic')

def test_six_question_cap_and_no_implicit_parent_mastery():
    state=d.start('a','materials.deflection');d.next_question(state)
    state['current']=None;state['diagnostic_count']=6
    result=d.next_question(state)
    assert result['phase']=='evidence_ready'
    assert d.report(state)['unmeasured_prerequisites']

def test_restart_preserves_seen_and_no_retest_answer_leak():
    state=d.start('a','math02.basic');old=d.next_question(state)
    state=d.start('a','math02.basic',state)
    assert d.next_question(state)['id']!=old['id']
    d.learn(state,'math02.basic')
    state['phase']='transfer';q=d.next_question(state)
    assert q['purpose']=='transfer' and 'answer' not in q
    d.submit(state,'exp(x)');state['phase']='retention'
    ret=d.next_question(state)
    assert ret['id']!=q['id'] and 'answer' not in ret

def test_profile_isolation_and_atomic_restore(tmp_path):
    a=d.data_path('a',tmp_path);b=d.data_path('b',tmp_path)
    state=d.start('a','math02.chain');q=d.next_question(state);d.hint(state);d.save(a,state)
    restored=d.read_state(a)
    assert d.next_question(restored)==q and restored['hint_level']==1
    assert not b.exists()
    with pytest.raises(ValueError):d.data_path('../escape',tmp_path)
    with pytest.raises(ValueError):d.data_path('a',d.ROOT/'sessions')

def test_amend_retains_raw_answer_and_old_verdict():
    state=d.start('a','math02.basic');d.next_question(state)
    ev=d.submit(state,'cos(x)')
    original=copy.deepcopy(ev)
    d.amend(state,ev['id'],'pending','变量是否为u需要向学生核实')
    assert state['corrections'][0]['before']==original
    assert ev['answer']=='cos(x)' and ev['verdict']=='pending'

@pytest.mark.parametrize('meta',d.manifest()['courses'],ids=lambda m:m['id'])
def test_every_module_diagnostic_learning_transfer_retention(meta,tmp_path):
    target=next(x['id'] for x in d.catalog() if x['course']==meta['id'])
    state=d.start(meta['id'],target)
    for _ in range(2):
        q=d.next_question(state);assert q['purpose']=='diagnostic'
        answer=state['current']['answer'];ev=d.submit(state,answer)
        if ev['verdict']=='pending':d.amend(state,ev['id'],'correct','合成路径：核对题库要点与明确题设，不代表真实学生表现')
    assert d.next_question(state)['phase']=='evidence_ready'
    lesson=d.learn(state,target);assert lesson['example']['purpose']=='learning'
    for phase in ('transfer','retention'):
        state['phase']=phase;q=d.next_question(state)
        assert q['purpose']==phase and 'answer' not in q
        ev=d.submit(state,state['current']['answer'])
        if ev['verdict']=='pending':d.amend(state,ev['id'],'correct','合成路径要点核对')
    assert len(d.report(state)['transfer_results'])==2
    path=d.data_path(meta['id'],tmp_path);d.save(path,state)
    assert d.read_state(path)['seen']==state['seen']

def test_cli_round_trip_and_cross_course_return(tmp_path):
    cmd=[sys.executable,'-X','utf8',str(d.ROOT/'scripts/diagnose.py'),'--profile','beam','--data-dir',str(tmp_path)]
    import json
    def run(*args):
        r=subprocess.run(cmd+list(args),capture_output=True,text=True,encoding='utf-8',check=True)
        return json.loads(r.stdout)
    run('start','--skill','materials.deflection','--context','{"sign":"下挠为正"}')
    run('learn','--skill','math04.primitive')
    result=run('transfer','--return-target')
    assert result['skill_id']=='materials.deflection'
    assert 'answer' not in result
    run('pause');assert run('resume')['id']==result['id']
    run('answer','--answer','P*L**3/(3*E*I)')
    assert run('report')['transfer_results'][0]['verdict']=='pending'
    run('review','--attempt','1','--verdict','correct','--reason','已核对题设悬臂、端载、EI常量、挠度绝对值及单位')
    assert run('report')['transfer_results'][0]['verdict']=='correct'

@pytest.mark.parametrize('focus,observation',[('theory.model','把固定端画成铰支座'),('math04.primitive','将2x的原函数写成2x²'),('materials.boundary','把简支端转角全部设为0')])
def test_beam_evidence_routes_to_distinct_probe_then_returns(focus,observation):
    state=d.start('beam','materials.deflection',context={'routing_evidence':observation},focus=focus)
    q=d.next_question(state);assert q['skill_id']==focus
    wrong='否' if state['current']['answer']=='是' else '0'
    ev=d.submit(state,wrong)
    assert ev['skill_id']==focus
    assert d.report(state)['nodes'][1]['status']=='需继续核验或补习'
    d.learn(state,focus)
    state['focus']=state['return_target'];state['phase']='transfer'
    assert d.next_question(state)['skill_id']=='materials.deflection'

def test_focus_override_requires_evidence_and_valid_dependency():
    with pytest.raises(ValueError):d.start('a','materials.deflection',focus='math04.primitive')
    with pytest.raises(ValueError):d.start('a','materials.deflection',context={'routing_evidence':'猜测'},focus='math12.fourier')
