"""File-backed adaptive evidence workflow; CLI emits one public question at a time."""
import argparse
import copy
from datetime import datetime,timezone
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parents[1]
REF=ROOT/'references'
STATES={'correct':'本轮独立完成','assisted':'提示后完成','incorrect':'需继续核验或补习','pending':'需继续核验或补习','skip':'尚未测试'}
def now():return datetime.now(timezone.utc).isoformat()
def load(path):return json.loads(Path(path).read_text(encoding='utf-8'))
def manifest():return load(REF/'course-manifest.json')
def catalog():return manifest()['skills']
def bundles():
    for pack in manifest()['courses']:yield load(REF/'courses'/pack['file'])
def skill(sid):
    meta=next((x for x in catalog() if x['id']==sid),None)
    if meta is None:raise ValueError('未知技能ID')
    pack=load(REF/'courses'/meta['file'])
    return next(x for x in pack['skills'] if x['id']==sid)
def search(query,course=None):
    words=[x for x in re.split(r'\s+',query.casefold()) if x]
    ranked=[]
    for x in catalog():
        if course and x['course']!=course:continue
        hay=' '.join([x['id'],x['name']]+x.get('aliases',[])).casefold()
        score=sum(4 if w in x['name'].casefold() else 1 for w in words if w in hay)
        if score:ranked.append((score,x))
    return [x for _,x in sorted(ranked,key=lambda z:(-z[0],z[1]['id']))[:12]]
def public(item):
    return {k:copy.deepcopy(item[k]) for k in ('id','skill_id','purpose','prompt','answer_type','options','context','domain') if k in item}
def evidence(state,sid):
    rows=[x for x in state['attempts'] if x['skill_id']==sid and x['phase']=='diagnostic' and not x.get('superseded') and x['verdict']!='skip']
    if not rows:return []
    latest=rows[-1]['session_id']
    return [x for x in rows if x['session_id']==latest]
def status(state,sid):
    seen=evidence(state,sid)
    if not seen:return '尚未测试'
    if any(x['verdict'] in ('incorrect','pending') for x in seen):return '需继续核验或补习'
    if any(x['hint_level'] for x in seen):return '提示后完成'
    return '本轮独立完成'
def data_path(profile,data_dir=None):
    if not re.fullmatch(r'[A-Za-z0-9_-]{1,64}',profile):raise ValueError('档案名只用英文字母、数字、短横线或下划线')
    if profile.upper() in {'CON','PRN','AUX','NUL'}|{f'{prefix}{i}' for prefix in ('COM','LPT') for i in range(1,10)}:
        raise ValueError('请换一个档案名，当前名称被操作系统保留')
    base=Path(data_dir).resolve() if data_dir else Path(os.environ.get('LOCALAPPDATA',Path.home()/'.local/share'))/'campus-gap-diagnoser'
    if ROOT.resolve()==base or ROOT.resolve() in base.parents:raise ValueError('学习档案必须位于Skill包之外')
    base.mkdir(parents=True,exist_ok=True);return base/(profile+'.json')
def save(path,state):
    state['updated_at']=now();path=Path(path)
    fd,name=tempfile.mkstemp(prefix='.state-',suffix='.tmp',dir=path.parent)
    try:
        with os.fdopen(fd,'w',encoding='utf-8') as f:json.dump(state,f,ensure_ascii=False,indent=2)
        os.replace(name,path)
    finally:
        if os.path.exists(name):os.unlink(name)
def read_state(path):
    if not Path(path).exists():raise ValueError('档案不存在；先用 start 创建')
    return load(path)
def start(profile,target,existing=None,context=None,focus=None):
    skill(target)
    if context is None:context={}
    if not isinstance(context,dict):raise ValueError('context须为JSON对象，例如 {"routing_evidence":"实际观察"}')
    if focus and focus!=target:
        if not context.get('routing_evidence'):raise ValueError('请提供已有解题过程中的观察，以确定起始核验点')
        allowed=set()
        def ancestors(sid):
            for parent in skill(sid)['prerequisites']:
                if parent not in allowed:allowed.add(parent);ancestors(parent)
        ancestors(target)
        if focus not in allowed:raise ValueError('起始核验点必须是目标的前置技能')
    state=existing or {'version':1,'profile':profile,'created_at':now(),'attempts':[],'corrections':[],'history':[],'seen':[]}
    if existing:state['history'].append({k:copy.deepcopy(existing.get(k)) for k in ('session_id','target','phase','diagnostic_count','context','updated_at')})
    state.update({'session_id':now(),'target':target,'focus':focus or target,'phase':'diagnostic','diagnostic_count':0,'current':None,'hint_level':0,'context':context})
    state['return_target']=target
    return state
def next_question(state):
    if state['phase']=='paused':return {'phase':'paused','message':'学习已暂停，使用 resume 继续当前题。'}
    if state['phase']=='diagnostic':
        pending=[x['id'] for x in state['attempts'] if x['session_id']==state['session_id'] and x['phase']=='diagnostic' and x['verdict']=='pending']
        if pending:return {'phase':'awaiting_review','attempt_ids':pending,'message':'先复核待确认的作答，再选择下一道诊断题。'}
    if state.get('current'):return public(state['current'])
    phase=state['phase']
    if phase in ('paused','complete','evidence_ready'):return {'phase':phase,'message':'可生成证据卡；补习使用 learn，迁移使用 transfer，后续复测使用 retest。'}
    if phase=='diagnostic' and state['diagnostic_count']>=6:
        state['phase']='evidence_ready';return {'phase':state['phase'],'message':'本轮已完成6道诊断题，现可查看证据卡并选择补习内容。'}
    candidates=[state.get('focus',state['target'])]
    if phase=='diagnostic':
        recent=[x for x in state['attempts'] if x['session_id']==state['session_id'] and not x.get('superseded') and x['phase']=='diagnostic']
        if recent:
            last=recent[-1]
            if last['verdict'] in ('incorrect','pending','assisted'):
                parents=skill(last['skill_id'])['prerequisites']
                candidates=[p for p in parents if not evidence(state,p)]+[last['skill_id']]+candidates
            elif last['skill_id']!=state['target']:
                candidates=[state['target']]+candidates
        target_events=[x for x in recent if x['skill_id']==state['target'] and x['verdict']!='skip']
        if len(target_events)>=2 and all(x['verdict']=='correct' and not x['hint_level'] for x in target_events):
            state['phase']='evidence_ready';return {'phase':'evidence_ready','message':'本轮目标两道独立诊断题已完成，可进入迁移练习。'}
    for sid in dict.fromkeys(candidates):
        desired='diagnostic' if phase=='diagnostic' else phase
        for item in skill(sid)['items']:
            if item['purpose']==desired and item['id'] not in state['seen']:
                state['current']=copy.deepcopy(item);state['hint_level']=0
                state['seen'].append(item['id'])
                return public(item)
    state['phase']='evidence_ready' if phase=='diagnostic' else 'complete'
    return {'phase':state['phase'],'message':'当前题池已用完。可查看已有证据，或补充审核后的新题再复测。'}
def safe_grade(item,answer):
    try:
        result=subprocess.run([sys.executable,'-X','utf8',str(ROOT/'scripts'/'grade.py')],input=json.dumps({'item':item,'answer':answer},ensure_ascii=False),capture_output=True,text=True,encoding='utf-8',timeout=4)
        if result.returncode:return {'verdict':'pending','reason':'自动判分不可用，交给宿主复核'}
        return json.loads(result.stdout)
    except (subprocess.TimeoutExpired,ValueError,OSError):return {'verdict':'pending','reason':'自动核验超时或结果异常，交给宿主复核'}
def submit(state,answer,skip=False):
    if state['phase']=='paused':raise ValueError('当前已暂停，请先恢复')
    item=state.get('current')
    if not item:raise ValueError('先获取当前问题')
    result={'verdict':'skip','reason':'已跳过，本题保留为未测试'} if skip else safe_grade(item,answer)
    verdict='assisted' if result['verdict']=='correct' and state['hint_level'] else result['verdict']
    event={'id':len(state['attempts'])+1,'session_id':state['session_id'],'question_id':item['id'],'skill_id':item['skill_id'],'phase':state['phase'],'answer':answer,'verdict':verdict,'reason':result['reason'],'hint_level':state['hint_level'],'at':now()}
    state['attempts'].append(event)
    if item['id'] not in state['seen']:state['seen'].append(item['id'])
    state['current']=None
    if state['phase']=='diagnostic':state['diagnostic_count']+=1
    else:state['phase']='complete'
    return event
def hint(state):
    if state['phase']=='paused':raise ValueError('当前已暂停，请先恢复')
    item=state.get('current')
    if not item:raise ValueError('无当前题目')
    hints=item.get('hints',[]);level=state['hint_level']
    if level>=len(hints):return {'hint':'没有更多提示；可回答不会或申请讲解。'}
    state['hint_level']+=1;return {'hint':hints[level],'level':state['hint_level']}
def amend(state,attempt_id,verdict,reason):
    if verdict not in ('correct','incorrect','pending','skip'):raise ValueError('无效复核结论')
    if not reason.strip():raise ValueError('复核需要理由与证据')
    original=next((x for x in state['attempts'] if x['id']==attempt_id),None)
    if not original:raise ValueError('找不到答题记录')
    effective='assisted' if verdict=='correct' and original['hint_level'] else verdict
    state['corrections'].append({'attempt_id':attempt_id,'before':copy.deepcopy(original),'verdict':effective,'reason':reason,'at':now()})
    original['verdict']=effective;original['reason']=reason
    return original
def learn(state,sid=None):
    selected=skill(sid or state.get('focus',state['target']))
    state.update({'focus':selected['id'],'current':None,'hint_level':0,'phase':'learning'})
    example=next(x for x in selected['items'] if x['purpose']=='learning')
    if example['id'] not in state['seen']:state['seen'].append(example['id'])
    return {'skill':selected['name'],'explanation':selected['teaching'],'example':example,'next':'请选择 transfer 进行未展示答案的迁移题；专业题可设置 --return-target 返回原情境。'}
def report(state):
    active=[x for x in state['attempts'] if not x.get('superseded')]
    ids=list(dict.fromkeys([state['target']]+[x['skill_id'] for x in active]))
    nodes=[]
    for sid in ids:
        ev=evidence(state,sid);wrong=[x for x in ev if x['verdict']=='incorrect']
        pending=sum(x['verdict']=='pending' for x in ev)
        if not ev:interpretation='该知识点尚未作答，可安排核验题。'
        elif pending:interpretation=f'有{pending}条作答待复核，先确认这些回答，再选择补习内容。'
        elif len({x['question_id'] for x in wrong})>=2:interpretation='两道独立题出现错误，建议优先补习，并核对共同出错的步骤。'
        elif wrong:interpretation='本轮有一道错题，建议用另一题核对同一技能。'
        elif any(x['hint_level'] for x in ev):interpretation='已借助提示完成练习，下一步独立完成迁移题。'
        else:interpretation=f'本轮{len(ev)}道题独立完成，下一步进行迁移练习。'
        nodes.append({'id':sid,'name':skill(sid)['name'],'status':status(state,sid),'evidence':ev,'interpretation':interpretation})
    return {'profile':state['profile'],'target':state['target'],'phase':state['phase'],'nodes':nodes,'unmeasured_prerequisites':[x for x in skill(state['target'])['prerequisites'] if not evidence(state,x)],'transfer_results':[x for x in active if x['phase'] in ('transfer','retention')],'follow_up':'用未见迁移题检查当前理解，下次再记录一道复测题的表现。','scheduled_reminder':False}

def main():
    p=argparse.ArgumentParser(description='卡点侦探本地诊断引擎')
    p.add_argument('--profile');p.add_argument('--data-dir')
    p.add_argument('command',choices=['courses','search','inspect','start','next','answer','hint','skip','review','learn','transfer','retest','pause','resume','report','export'])
    p.add_argument('--query',default='');p.add_argument('--course');p.add_argument('--skill');p.add_argument('--focus');p.add_argument('--answer',default='');p.add_argument('--attempt',type=int);p.add_argument('--verdict');p.add_argument('--reason',default='');p.add_argument('--return-target',action='store_true');p.add_argument('--context');p.add_argument('--output')
    a=p.parse_args();cmd=a.command
    if cmd=='courses':out=manifest()['courses']
    elif cmd=='search':out=search(a.query,a.course)
    elif cmd=='inspect':out=skill(a.skill)
    else:
        if not a.profile:raise ValueError('请用 --profile 指定本次使用的学习档案')
        path=data_path(a.profile,a.data_dir)
        if cmd=='start':
            state=start(a.profile,a.skill,load(path) if path.exists() else None,json.loads(a.context) if a.context else None,a.focus);out=next_question(state)
        else:
            state=read_state(path)
            if cmd=='next':out=next_question(state)
            elif cmd=='answer':out=submit(state,a.answer)
            elif cmd=='skip':out=submit(state,'不会/跳过',True)
            elif cmd=='hint':out=hint(state)
            elif cmd=='review':out=amend(state,a.attempt,a.verdict,a.reason)
            elif cmd=='learn':out=learn(state,a.skill)
            elif cmd in ('transfer','retest'):
                if a.return_target:state['focus']=state['return_target']
                if a.skill:state['focus']=a.skill
                state.update({'phase':'transfer' if cmd=='transfer' else 'retention','current':None,'hint_level':0});out=next_question(state)
            elif cmd=='pause':
                if state['phase']!='paused':state['resume_phase']=state['phase'];state['phase']='paused'
                out={'phase':'paused'}
            elif cmd=='resume':
                if state['phase']=='paused':state['phase']=state.pop('resume_phase','diagnostic')
                out=next_question(state)
            elif cmd=='report':out=report(state)
            elif cmd=='export':
                if not a.output:raise ValueError('导出需要 --output')
                dest=Path(a.output).resolve()
                if ROOT==dest or ROOT in dest.parents:raise ValueError('档案不可导出到Skill源码目录')
                dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(json.dumps(state,ensure_ascii=False,indent=2),encoding='utf-8');out={'exported':str(dest)}
        save(path,state)
    print(json.dumps(out,ensure_ascii=False,indent=2))

if __name__=='__main__':
    try:main()
    except (ValueError,KeyError,StopIteration,json.JSONDecodeError,OSError) as exc:
        print(json.dumps({'error':str(exc)},ensure_ascii=False));sys.exit(2)
