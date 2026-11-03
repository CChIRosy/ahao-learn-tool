"""Behavioral cases identified during the wording and runtime review."""
import json
import subprocess
import sys
import pytest
import diagnose as d
from grade import grade

def test_public_context_does_not_include_teaching_notes():
    for pack in d.bundles():
        for node in pack['skills']:
            for item in node['items']:
                if item['purpose']=='diagnostic':
                    assert node['teaching'] not in json.dumps(d.public(item),ensure_ascii=False),item['id']

def test_review_old_answer_preserves_next_pending_question():
    state=d.start('a','math02.chain');d.next_question(state)
    first=d.submit(state,'cos(x**2)')
    pending=d.next_question(state)
    d.amend(state,first['id'],'incorrect','核对原题：漏掉内层导数2x')
    assert d.next_question(state)==pending
    assert d.submit(state,'cos(u)')['question_id']==pending['id']

def test_invalid_choice_needs_clarification():
    item={'answer':'是','answer_type':'choice','options':['是','否']}
    assert grade(item,'不知道')['verdict']=='pending'
    assert grade(item,'随便写')['verdict']=='pending'
    assert grade(item,'否')['verdict']=='incorrect'

def test_repeated_pause_resumes_same_question(tmp_path):
    cmd=[sys.executable,'-X','utf8',str(d.ROOT/'scripts/diagnose.py'),'--profile','pause','--data-dir',str(tmp_path)]
    def call(*args):
        r=subprocess.run(cmd+list(args),capture_output=True,text=True,encoding='utf-8',check=True)
        return json.loads(r.stdout)
    question=call('start','--skill','math02.chain')
    call('pause');call('pause')
    assert call('resume')==question
    assert call('answer','--answer','2*x*cos(x**2)')['phase']=='diagnostic'

def test_report_gives_next_step_for_success():
    state=d.start('a','math02.basic')
    for answer in ('cos(u)','2*x'):
        d.next_question(state);d.submit(state,answer)
    interpretation=d.report(state)['nodes'][0]['interpretation']
    assert '独立完成' in interpretation and '迁移' in interpretation

def test_paused_next_returns_pause_status():
    state=d.start('a','math02.chain');d.next_question(state)
    state['phase']='paused'
    assert d.next_question(state)['phase']=='paused'

def test_context_schema_and_reserved_profile_names(tmp_path):
    with pytest.raises(ValueError):d.start('a','math02.chain',context=['not','an','object'])
    for name in ('CON','aux','NUL','COM1','lpt9'):
        with pytest.raises(ValueError):d.data_path(name,tmp_path)

def test_pending_answer_waits_for_review_before_new_diagnostic():
    state=d.start('a','math01.function');d.next_question(state)
    event=d.submit(state,'不知道')
    assert event['verdict']=='pending'
    waiting=d.next_question(state)
    assert waiting['phase']=='awaiting_review' and waiting['attempt_ids']==[event['id']]
    d.amend(state,event['id'],'skip','学生选择跳过，保留未测状态')
    assert d.next_question(state)['id']=='math01.function.2'

@pytest.mark.parametrize('answer',['(x+1,2)','[(x+1),(2)]','x+1,2','（x+1，2）'])
def test_parenthesized_vector_components(answer):
    assert grade({'answer':'x+1,2','answer_type':'vector'},answer)['verdict']=='correct'

@pytest.mark.parametrize('answer',['4,6,-2','-2,-3,1','1,3/2,-1/2'])
def test_normal_vector_accepts_nonzero_scalar_multiples(answer):
    assert grade(d.skill('math08.planes')['items'][0],answer)['verdict']=='correct'

def test_direction_vector_rejects_zero_or_nonparallel_vector():
    item=d.skill('math08.planes')['items'][1]
    assert grade(item,'0,0,0')['verdict']=='incorrect'
    assert grade(item,'1,0,0')['verdict']=='incorrect'
