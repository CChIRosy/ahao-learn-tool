import argparse
import json
from pathlib import Path
import sys
import sympy as s
from oracles import calculations

BASE=Path(__file__).resolve().parents[1];ROOT=BASE/'skill/campus-gap-diagnoser';REF=ROOT/'references'
sys.path.insert(0,str(ROOT/'scripts'))
from grade import expression

def validate(update=False):
    manifest=json.loads((REF/'course-manifest.json').read_text(encoding='utf-8'))
    skills={};items={};packs=[];fail=[];parsed=0;checked=0
    for meta in manifest['courses']:
        path=REF/'courses'/meta['file'];pack=json.loads(path.read_text(encoding='utf-8'));packs.append((path,pack))
        assert len(pack['skills'])==meta['skill_count']
        for node in pack['skills']:
            assert node['id'] not in skills;skills[node['id']]=node
            assert [i['purpose'] for i in node['items']]==['diagnostic','diagnostic','learning','transfer','retention']
            assert len({i['prompt'] for i in node['items']})==5
            for item in node['items']:
                assert item['id'] not in items;items[item['id']]=item
                assert item['skill_id']==node['id'] and item['rubric'] and item['hints']
                kind=item['answer_type']
                try:
                    if kind in ('expression','vector'):
                        for value in item['answer'].split(','):expression(value)
                    elif kind=='choice':assert item['answer'] in item['options']
                    else:assert kind=='open' and item['answer']
                    item['verification']['key_parsed']=True;parsed+=1
                except Exception as exc:fail.append((item['id'],'key',str(exc)))
    visited=set();stack=set()
    def visit(sid):
        assert sid in skills,('missing prerequisite',sid)
        assert sid not in stack,('cycle',sid)
        if sid in visited:return
        stack.add(sid)
        for parent in skills[sid]['prerequisites']:visit(parent)
        stack.remove(sid);visited.add(sid)
    for sid in skills:visit(sid)
    for qid,value in calculations().items():
        if qid not in items:fail.append((qid,'missing','oracle has no item'));continue
        item=items[qid]
        try:
            actual=[expression(v) for v in item['answer'].split(',')]
            expected=list(value) if isinstance(value,(list,tuple)) else [s.sympify(value)]
            assert len(actual)==len(expected)
            assert all(s.simplify(a-b)==0 for a,b in zip(actual,expected))
            checked+=1;item['verification']['independent_oracle']=True
        except Exception as exc:fail.append((qid,'oracle',str(exc)))
    if update and not fail:
        for path,pack in packs:path.write_text(json.dumps(pack,ensure_ascii=False,indent=2),encoding='utf-8')
    result={'modules':len(packs),'skills':len(skills),'questions':len(items),'parsed_keys':parsed,'independent_calculations':checked,'teacher_reviewed':0,'student_validated':0,'failures':fail}
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--update',action='store_true');a=p.parse_args()
    result=validate(a.update);print(json.dumps(result,ensure_ascii=False,indent=2))
    sys.exit(bool(result['failures']))
