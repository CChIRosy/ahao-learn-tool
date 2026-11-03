import hashlib
import json
from pathlib import Path
import subprocess
import sys
import zipfile
from validate_resources import validate,BASE,ROOT

def main():
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--output-dir');args=parser.parse_args()
    result=validate(update=True)
    if result['failures']:raise SystemExit(json.dumps(result,ensure_ascii=False))
    manifest=json.loads((ROOT/'references/course-manifest.json').read_text(encoding='utf-8'))
    docs=BASE/'docs';docs.mkdir(exist_ok=True)
    lines=['# 课程覆盖矩阵','', '范围基准：同济第八版上下册及references/sources-and-review.md所列高校大纲。分母为本项目拆分的主题节点，不等于教材每页、每道例题或所有学校的教学要求。', '',
           f"实际数据：{result['modules']}个模块、{result['skills']}个主题、{result['questions']}道原创题；每主题2道诊断、1道补习、1道迁移、1道后续复测。", '',
           '每个题ID均可由diagnose.py inspect --skill读取。教师审核及真实学生验证均未完成。合成流程测试按模块执行，不表示每个节点都完成真实交互验证。', '',
           '|模块|技能ID与主题|层级|前置|诊断题|补习/迁移/后续复测|独立计算核对题数|教师/学生验证|',
           '|---|---|---|---|---|---|---|---|']
    for meta in manifest['courses']:
        pack=json.loads((ROOT/'references/courses'/meta['file']).read_text(encoding='utf-8'))
        for node in pack['skills']:
            q=node['items'];lines.append('|'+ '|'.join([meta['name'],node['id']+' '+node['name'],node['tier'],'、'.join(node['prerequisites']) or '本包未指定',','.join(x['id'] for x in q[:2]),','.join(x['id'] for x in q[2:]),str(sum(x['verification']['independent_oracle'] for x in q)),'未审核/未验证'])+'|')
    lines+=['','## 深度缺口与后续工作','','- 主题均有起始题池，但全书逐小节/定理/题型映射尚未由教师验收；每主题五题不等于穷尽全部难度。', '- 证明与论述自动评分不支持；需宿主按评分要点复核。', '- 跨题根因诊断为可解释启发式，尚未用真实学生数据校准。', '- 已实现全部模块的流程验收；尚无真实学生迁移、保持或学习成效数据。', '- 高等数学选学、三门力学进阶主题有明确层级，复杂空间结构与非线性工程分析未纳入自动核验。']
    (docs/'coverage.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    # Package allowlist: no caches, archives, real profiles, secrets, or local environments.
    files=sorted(p for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc')
    assert len(files)<=30 and sum(p.stat().st_size for p in files)<=40*1024*1024
    out=Path(args.output_dir).resolve() if args.output_dir else BASE.parents[1]/'outputs';out.mkdir(parents=True,exist_ok=True)
    archive=out/'campus-gap-diagnoser-v0.1.0.zip'
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
        for file in files:z.write(file,file.relative_to(ROOT).as_posix())
    with zipfile.ZipFile(archive) as z:
        assert 'SKILL.md' in z.namelist() and len(z.namelist())==len(files)
        assert z.testzip() is None
    stats=result|{'package_files':len(files),'uncompressed_bytes':sum(p.stat().st_size for p in files),'zip_bytes':archive.stat().st_size,'zip_sha256':hashlib.sha256(archive.read_bytes()).hexdigest()}
    (docs/'build-stats.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(stats,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
