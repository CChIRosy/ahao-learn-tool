import json
import pytest
import sympy as s
import diagnose as d
from grade import grade, expression
from audit_syllabus import MATH, STRUCTURES

NEW=[n for p in d.bundles() for n in p['skills'] if n.get('introduced_version')=='0.2.0']


def test_syllabus_has_all_declared_sections_and_no_orphaned_skills():
    audit=json.loads((d.REF/'syllabus-audit.json').read_text(encoding='utf-8'))
    rows=audit['entries'];catalog={n['id'] for n in d.catalog()}
    mapped={sid for row in rows for sid in row['skills']}
    assert mapped==catalog
    assert len([r for r in rows if r['id'].startswith('math.')])==82
    expected={f'math.{ch}.{i}' for ch,sec in MATH.items() for i in range(1,len(sec.split(';'))+1)}
    expected|={f'structures.{ch}.{i}' for ch,sec in STRUCTURES.items() for i in range(1,len(sec.split(';'))+1)}
    assert expected <= {r['id'] for r in rows}
    assert all(r['source'] in audit['sources'] and r['skills'] for r in rows)
    assert all(not r['teacher_reviewed'] and not r['depth_validated'] for r in rows)


@pytest.mark.parametrize('node',NEW,ids=lambda n:n['id'])
def test_added_topic_can_present_all_learning_phases_and_grade_keys(node):
    state=d.start('synthetic',node['id'])
    q=d.next_question(state)
    assert q['id']==node['items'][0]['id']
    assert not {'answer','rubric','hints','learning_steps'} & q.keys()
    for item in node['items']:
        result=grade(item,item['answer'])
        assert result['verdict'] in ('correct','pending'),(item['id'],result)
        assert item['verification']['key_parsed']
    d.learn(state,node['id'])
    state.update(phase='transfer',current=None)
    transfer=d.next_question(state)
    state.update(phase='retention',current=None)
    retest=d.next_question(state)
    assert transfer['purpose']=='transfer' and retest['purpose']=='retention'
    assert len({q['id'],transfer['id'],retest['id']})==3
    assert 'answer' not in transfer and 'answer' not in retest


@pytest.mark.parametrize('query,expected',[
    ('Γ函数','math05.gamma'),('多跨静定梁','structures.gerber'),
    ('最小二乘','math09.least-squares'),('碰撞','theory.impact'),
    ('应变花','materials.rosette'),('多自由度振动','structures.modal')])
def test_missing_topics_are_now_discoverable(query,expected):
    assert expected in {r['id'] for r in d.search(query)}


def test_new_antiderivatives_and_ode_solutions_satisfy_equations():
    x=s.Symbol('x',real=True)
    for sid,index,f in [
        ('math04.integral-table',0,1/(1+4*x*x)),
        ('math04.integral-table',3,s.exp(5*x)),
        ('math04.trig-rational',3,s.sin(x)*s.cos(x))]:
        answer=expression(d.skill(sid)['items'][index]['answer'])
        assert s.simplify(s.diff(answer,x)-f)==0
    y=expression(d.skill('math07.bernoulli')['items'][1]['answer'])
    assert s.simplify(s.diff(y,x)-y*y)==0 and y.subs(x,0)==1


def test_space_curve_direction_allows_nonzero_multiples():
    assert grade(d.skill('math09.vector-curves')['items'][0],'2,4,6')['verdict']=='correct'
    assert grade(d.skill('math09.vector-curves')['items'][2],'-1,-2,-3')['verdict']=='correct'
