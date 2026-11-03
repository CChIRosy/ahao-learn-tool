import hashlib
import json
from pathlib import Path
import zipfile
from validate_resources import validate,BASE,ROOT

def main():
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--output-dir');args=parser.parse_args()
    result=validate(update=True)
    if result['failures']:raise SystemExit(json.dumps(result,ensure_ascii=False))
    from audit_syllabus import build
    build()
    manifest=json.loads((ROOT/'references/course-manifest.json').read_text(encoding='utf-8'))
    docs=BASE/'docs';docs.mkdir(exist_ok=True)
    lines=['# 课程覆盖矩阵','', '范围基准：同济高数、三门力学、钢结构与用户确认的河流海岸工程；来源见references/sources-and-review.md。逐项对照见docs/syllabus-audit.md及包内references/syllabus-audit.json。映射粒度为知识主题与起始题库。', '',
           f"实际数据：{result['modules']}个模块、{result['skills']}个主题、{result['questions']}道原创题；每主题2道诊断、1道补习、1道迁移、1道后续复测。", '',
           '题目可通过diagnose.py inspect --skill读取。每模块已执行一条合成完整流程；各主题的题量和计算核对数量列在下表。教师与学生验证状态逐行记录。', '',
           '|模块|技能ID与主题|层级|前置|诊断题|补习/迁移/后续复测|独立计算核对题数|教师/学生验证|',
           '|---|---|---|---|---|---|---|---|']
    for meta in manifest['courses']:
        pack=json.loads((ROOT/'references/courses'/meta['file']).read_text(encoding='utf-8'))
        for node in pack['skills']:
            q=node['items'];lines.append('|'+ '|'.join([meta['name'],node['id']+' '+node['name'],node['tier'],'、'.join(node['prerequisites']) or '本包未指定',','.join(x['id'] for x in q[:2]),','.join(x['id'] for x in q[2:]),str(sum(x['verification']['independent_oracle'] for x in q)),'未审核/未验证'])+'|')
    lines+=['','## 后续验收','','- 请教师逐节审核知识映射、评分要点与题型深度，并扩充各主题题池。', '- 证明与论述由宿主按评分要点审核。', '- 通过真实学生作答校准诊断分支，测量迁移和后续保持。', '- 专业题按题设模型、单位、边界和公式适用范围核验；规范查表需记录版本和依据。', '- 统一的来源、适用范围与质量字段见references/sources-and-review.md。']
    (docs/'coverage.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    # Package allowlist: no caches, archives, real profiles, secrets, or local environments.
    files=sorted(p for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc')
    assert len(files)<=30 and sum(p.stat().st_size for p in files)<=40*1024*1024
    out=Path(args.output_dir).resolve() if args.output_dir else BASE.parents[1]/'outputs';out.mkdir(parents=True,exist_ok=True)
    archive=out/f"campus-gap-diagnoser-v{manifest['version']}.zip"
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
        for file in files:z.write(file,file.relative_to(ROOT).as_posix())
    with zipfile.ZipFile(archive) as z:
        assert 'SKILL.md' in z.namelist() and len(z.namelist())==len(files)
        assert z.testzip() is None
    stats=result|{'version':manifest['version'],'package_files':len(files),'uncompressed_bytes':sum(p.stat().st_size for p in files),'zip_bytes':archive.stat().st_size,'zip_sha256':hashlib.sha256(archive.read_bytes()).hexdigest()}
    (docs/'build-stats.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(stats,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
