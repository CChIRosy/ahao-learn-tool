# ahao-learn tool · 卡点侦探

通过短测、证据卡、定点补习和独立新题复测，帮助大学生定位高数与力学中的学习卡点。

0.1.1提供高数12章和理论力学、材料力学、结构力学的诊断引擎与题库，共15个数据模块、108个知识主题、540道原创题。每主题有两道诊断、一道补习例题、一道迁移和一道后续复测。范围按知识主题组织，具体节点与前置关系见[覆盖矩阵](docs/coverage.md)。

## 获取 Skill

- 下载已打包的 [campus-gap-diagnoser-v0.1.1.zip](packages/campus-gap-diagnoser-v0.1.1.zip)。包根目录直接包含SKILL.md。
- 或使用源码目录 [skill/campus-gap-diagnoser](skill/campus-gap-diagnoser)。
- 原始需求与创建提示词保留在 [PROMPT.md](PROMPT.md)。

运行需要Python 3.10+、SymPy 1.14.0，以及允许执行本地Python脚本的Skill宿主。解释、图片题意确认和开放回答审核使用宿主已有模型。

在仓库根目录创建环境：

```bash
python -m venv .venv
# Windows
.venv\Scripts\python -m pip install -r requirements.txt
# macOS / Linux
.venv/bin/python -m pip install -r requirements.txt
```

将Skill ZIP或解压后的Skill目录导入支持标准SKILL.md且允许脚本运行的宿主。CodeArts/OfficeAce的导入方式和脚本权限按当前客户端配置。

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

- 状态分为本轮独立完成、提示后完成、需核验或补习、尚未测试，并展示对应答题证据与下一步建议。
- pending表示待审核。开放证明、模型、单位与解释由宿主依据真实回答复核，保存原答与复核理由。
- 诊断与复测展示题面，讲解留到补习阶段；提示使用单独记录。题池耗尽后补充审核的新题。
- 高数与力学通过前置技能关联；补完数学节点后返回专业情境复测。

## 数据

用--profile指定独立档案名。默认档案位于当前用户数据目录下的campus-gap-diagnoser文件夹，可用--data-dir指定其他包外目录。每个档案保存原始作答、提示使用、复核和已见题；同一档案按本地单写者方式使用。档案、真实截图与报告保存在源码和发布包之外。

## 验证与质量

已完成脚本回归测试、540个答案格式检查、224道参考结果的另写计算核对，以及安装包解压运行检查。完整结果见[验证报告](docs/validation.md)和[本轮检查报告](docs/review-report.md)。

验证按层记录：程序检查已完成；教师题库审核、真实学生效果验证和CodeArts/OfficeAce宿主实机验收待执行。内容采用知识主题粒度和教材理想化力学模型。逐题状态、范围与适用条件集中见[来源与审核说明](skill/campus-gap-diagnoser/references/sources-and-review.md)。

## 复现开发检查

```bash
python -m pip install -r requirements-dev.txt
python tools/build_courses.py
python tools/validate_resources.py --update
python -m pytest -q
python tools/build_delivery.py
```

源码题库位于tools/build_courses.py、mechanics_seeds.py、supplemental_seeds.py。修改后重建并核对资源；另写计算表达式在tools/oracles.py。build_delivery.py将发布包写入仓库外的outputs目录，可通过--output-dir指定。GitHub同步使用独立发布步骤。

仓库已公开，当前未设置开源许可证。演示案例标注为合成数据，真实试用另行记录。
