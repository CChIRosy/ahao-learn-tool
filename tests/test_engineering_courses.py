import json
import pytest
import diagnose as d
from grade import grade

COURSES={'steel','hydraulics','river','coastal'}
NODES=[node for pack in d.bundles() if pack['id'] in COURSES for node in pack['skills']]


@pytest.mark.parametrize('node',NODES,ids=lambda node:node['id'])
def test_new_engineering_topic_runs_and_retains_model_review(node):
    state=d.start('synthetic',node['id'])
    question=d.next_question(state)
    assert question['id']==node['items'][0]['id']
    assert not {'answer','rubric','hints','learning_steps'} & question.keys()
    for item in node['items']:
        result=grade(item,item['answer'])
        assert result['verdict'] in ('correct','pending'),(item['id'],result)
        if item['answer_type'] in ('expression','vector'):
            assert item['requires_context'] and result['verdict']=='pending'
        assert item['verification']['key_parsed']
        assert not item['verification']['teacher_reviewed']
    lesson=d.learn(state,node['id'])
    assert lesson['example']['purpose']=='learning'
    state.update(phase='transfer',current=None)
    transfer=d.next_question(state)
    state.update(phase='retention',current=None)
    retention=d.next_question(state)
    assert len({question['id'],lesson['example']['id'],transfer['id'],retention['id']})==4
    assert 'answer' not in transfer and 'answer' not in retention


@pytest.mark.parametrize('query,sid',[
    ('角焊缝','steel.fillet-weld'),('高强螺栓','steel.friction-bolts'),
    ('水跃','hydraulics.jump'),('渗流','hydraulics.seepage'),
    ('Shields','river.bed-shear'),('河口','river.estuary'),
    ('波谱','coastal.random-waves'),('高桩码头','coastal.piled-quay'),
    ('疏浚','coastal.dredging')])
def test_engineering_topics_are_discoverable_and_course_filter_works(query,sid):
    assert sid in {row['id'] for row in d.search(query)}
    filtered=d.search(query,sid.split('.')[0])
    assert filtered and all(row['course']==sid.split('.')[0] for row in filtered)


@pytest.mark.parametrize('target,parent',[
    ('steel.column','materials.stability-design'),
    ('hydraulics.jump','hydraulics.momentum')])
def test_incorrect_result_routes_to_engineering_prerequisite(target,parent):
    state=d.start('synthetic',target);d.next_question(state)
    event=d.submit(state,'0')
    assert event['verdict']=='incorrect'
    assert d.next_question(state)['skill_id']==parent


def test_new_course_scope_and_cross_course_bridges_are_valid():
    assert COURSES <= {course['id'] for course in d.manifest()['courses']}
    audit=json.loads((d.REF/'syllabus-audit.json').read_text(encoding='utf-8'))
    rows=[r for r in audit['entries'] if r['id'].startswith('engineering.')]
    assert {sid for row in rows for sid in row['skills']}=={node['id'] for node in NODES}
    assert all(r['previous_version_status']=='missing' for r in rows)
    assert all(r['source'] in audit['sources'] for r in rows)
    catalog={row['id'] for row in d.catalog()}
    bridges=json.loads((d.REF/'cross-course-bridges.json').read_text(encoding='utf-8'))
    assert all(r['from'] in catalog and r['to'] in catalog for r in bridges['relations'])
