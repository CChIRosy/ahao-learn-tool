# 卡点侦探 · Campus Gap Diagnoser

通过短测、证据卡、定点补习和独立新题复测，帮助大学生定位高数与力学中的学习卡点。

当前版本为可运行的0.1.0主题级题库与诊断引擎：高数12章＋理论力学、材料力学、结构力学，15个数据模块、108个知识主题、540道原创题。每主题有两道诊断、一道补习例题、一道迁移和一道后续复测。范围细节见[覆盖矩阵](docs/coverage.md)；这不是教材逐页或所有学校大纲的完整认证覆盖。

## 获取 Skill

- 下载已打包的 [campus-gap-diagnoser-v0.1.0.zip](packages/campus-gap-diagnoser-v0.1.0.zip)。包根目录直接包含SKILL.md。
- 或使用源码目录 [skill/campus-gap-diagnoser](skill/campus-gap-diagnoser)。
- 原始需求与创建提示词保留在 [PROMPT.md](PROMPT.md)。

需要Python 3.10+与SymPy 1.14.0；解释、图片题意确认和开放回答审核使用宿主已有模型，不需要另一个模型API账号。此Skill需要宿主允许执行本地Python脚本；只能读提示词、不能运行脚本的宿主无法提供本地诊断引擎。

在仓库根目录创建环境：

```bash
python -m venv .venv
# Windows
.venv\Scripts\python -m pip install -r requirements.txt
# macOS / Linux
.venv/bin/python -m pip install -r requirements.txt
```

将Skill ZIP或解压后的Skill目录导入支持标准SKILL.md且允许脚本运行的宿主。CodeArts/OfficeAce的具体导入与脚本权限以当前客户端为准；本版本尚未在它们的真实会话中完成端到端验收。

## 命令行体验

在仓库根目录使用已安装依赖的解释器；以下以python表示该解释器：

```bash
python -X utf8 skill/campus-gap-diagnoser/scripts/diagnose.py search --query 链式法则
python -X utf8 skill/campus-gap-diagnoser/scripts/diagnose.py --profile demo start --skill math02.chain
python -X utf8 skill/campus-gap-diagnoser/scripts/diagnose.py --profile demo answer --answer "cos(x**2)"
python -X utf8 skill/campus-gap-diagnoser/scripts/diagnose.py --profile demo next
python -X utf8 skill/campus-gap-diagnoser/scripts/diagnose.py --profile demo report
```

宿主可接受：“这道题看了解析还是不懂”“找出我在梁挠度哪一步卡住了”“继续上次的卡点”“复测链式法则”。课程及技能ID见[course-manifest.json](skill/campus-gap-diagnoser/references/course-manifest.json)。更多路径见[演示说明](docs/demo.md)。

## 结果如何解释

- 状态区分本轮独立完成、提示后完成、需核验或补习、尚未测试；不生成未经校准的掌握百分比。
- pending表示需要进一步审核，不等于学生答错。开放证明、模型、单位与解释由宿主依据真实回答复核，复核保留原答与理由。
- 正式诊断/迁移/复测接口不暴露答案；提示单独记录。题池耗尽不会重复已见题冒充独立复测。
- 支持高数到力学的前置桥接，专业题补数学后须返回专业情境。力学图题必须先确认模型，结果不用于实际工程安全判断。

## 数据

必须显式提供档案名。默认档案位于当前用户数据目录下的campus-gap-diagnoser文件夹，可用--data-dir改到其他包外目录。每个档案包含原始作答、提示使用、复核和已见题。它是本地单写者工具，不是有认证的多人并发平台。档案、真实截图与报告不进入仓库或发布包。

## 验证与质量

已执行：49项自动测试；540个答案格式检查；224道参考结果的另写计算核对；Skill结构校验；15个模块的合成端到端流程；三类梁题核验入口和专业情境返回测试；已知单位换算与量纲拒绝测试。

尚未完成：教师题库审核、真实学生诊断/迁移/保持效果验证、CodeArts/OfficeAce宿主真实端到端试跑。540题不等于540题都经过独立计算，224道计算核对也不等于教师审核。逐题字段与实际记录见[验证报告](docs/validation.md)和[构建统计](docs/build-stats.json)。

## 复现开发检查

```bash
python -m pip install -r requirements-dev.txt
python tools/build_courses.py
python tools/validate_resources.py --update
python -m pytest -q
python tools/build_delivery.py
```

源码题库位于tools/build_courses.py、mechanics_seeds.py、supplemental_seeds.py。修改后重建并核对资源；独立计算表达式在tools/oracles.py。build_delivery.py默认将发布包写入仓库外的outputs目录，可通过--output-dir指定。它不会联网发布或自动同步GitHub。

未添加开源授权；仓库保持私有。开发与发布时保留来源与质量说明，不将合成案例当作真人数据。
