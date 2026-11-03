import json
from pathlib import Path
from validate_resources import validate,BASE,ROOT
import diagnose as d

def test_resource_graph_and_independent_math_calculations():
    result=validate()
    assert not result['failures']
    assert result['modules']==15 and result['parsed_keys']==result['questions']
    assert result['independent_calculations']>200

def test_course_ambiguity_and_key_skills():
    assert any(x['id']=='math02.chain' for x in d.search('链式法则'))
    assert all(x['course']=='materials' for x in d.search('弯曲','materials'))
    assert d.skill('structures.matrix')['prerequisites']==['structures.displacement','structures.algebra-bridge']

def test_every_skill_has_disjoint_phases_and_truthful_review_flags():
    for pack in d.bundles():
        for skill in pack['skills']:
            assert len({x['id'] for x in skill['items']})==5
            for item in skill['items']:
                assert not item['verification']['teacher_reviewed']
                assert not item['verification']['student_validated']

def test_package_budget():
    files=[p for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc']
    assert len(files)<=30
    assert sum(p.stat().st_size for p in files)<=40*1024*1024
