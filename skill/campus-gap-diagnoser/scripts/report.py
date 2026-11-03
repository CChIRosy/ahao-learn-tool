import argparse
import html
import json
from pathlib import Path
from diagnose import data_path,read_state,report,ROOT

def render(data):
    lines=['# 卡点证据卡',f"\n目标：{data['target']}",f"\n阶段：{data['phase']}"]
    for node in data['nodes']:
        lines.extend([f"\n## {node['name']}",f"\n状态：{node['status']}",f"\n{node['interpretation']}"])
        for ev in node['evidence']:
            # User-authored text remains literal: escape HTML and Markdown block markers.
            answer=html.escape(str(ev['answer'])).replace('\n',' / ').replace('`','\\`')
            lines.append(f"\n- 证据 {ev['id']}：{ev['question_id']}；回答：{answer}；判定：{ev['verdict']}；提示层级：{ev['hint_level']}")
    lines.append('\n待核验的前置知识：'+('、'.join(data['unmeasured_prerequisites']) or '本轮清单中的前置知识均已有作答记录'))
    lines.append('\n下一步：'+data['follow_up'])
    return '\n'.join(lines)+'\n'

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--profile',required=True);p.add_argument('--data-dir');p.add_argument('--output',required=True);a=p.parse_args()
    dest=Path(a.output).resolve()
    if ROOT==dest or ROOT in dest.parents:raise SystemExit('学习报告必须保存到Skill包之外')
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(render(report(read_state(data_path(a.profile,a.data_dir)))),encoding='utf-8')
    print(json.dumps({'report':str(dest)},ensure_ascii=False))
