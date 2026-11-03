---
name: campus-gap-diagnoser
description: 用短测定位大学高数、理论力学、材料力学、结构力学的学习卡点，提供带答题证据的补习与独立复测。适用于“看了解析仍不懂”“卡在哪一步”“继续上次卡点”、梁挠度等专业题回溯数学前置的请求。
---

# 卡点侦探

## 开始一次学习

宿主模型负责解释、图像确认和开放回答审核，Python脚本负责题库、分支与学习档案。需要Python 3.10+和`requirements.txt`中的依赖。先确认本次使用的档案名；每位使用者保存独立档案，示例中用`demo`。

1. 获取用户题目和已有过程。截图先确认识别文字；力学图题确认支座、连接、荷载、尺寸、坐标、正号与单位。识别有疑点时，请用户补充图文。
2. 用课程目录和搜索寻找目标，再读取该技能与必要前置。候选相近时请用户确认课程和目标。
3. 由脚本一次发一道诊断题，展示公开题面。最多6道，接受“不会”、提示、跳过和暂停。作答记录使用学生的实际回答。
4. 根据逐题证据输出卡点卡，标明观察、候选解释和下一道核验题；用文字描述本轮表现。
5. 选择优先补习技能，用短解释和题库例题讲解，随后给未见迁移题；专业课补了数学前置后，再返回专业情境迁移。
6. 下次使用未见题后续复测；题池耗尽时补充审核后的新题。当前实现保存复测进度，由用户下次发起；设置提醒需另行调用宿主的调度工具并确认成功。

## 脚本调用

在本Skill目录执行，`python`替换为当前可用Python解释器。命令输出UTF-8 JSON；Windows建议加`-X utf8`。

```bash
python -X utf8 scripts/diagnose.py courses
python -X utf8 scripts/diagnose.py search --query 链式法则
python -X utf8 scripts/diagnose.py inspect --skill math02.chain
python -X utf8 scripts/diagnose.py --profile demo start --skill math02.chain
python -X utf8 scripts/diagnose.py --profile demo answer --answer "cos(x**2)"
python -X utf8 scripts/diagnose.py --profile demo next
python -X utf8 scripts/diagnose.py --profile demo hint
python -X utf8 scripts/diagnose.py --profile demo report
python -X utf8 scripts/diagnose.py --profile demo learn --skill math02.chain
python -X utf8 scripts/diagnose.py --profile demo transfer
python -X utf8 scripts/diagnose.py --profile demo retest
```

`inspect`和`learn`包含答案，供宿主备课或补习使用。诊断和独立复测只展示`next/start/transfer/retest`返回的公开题面，将讲解与答案留到补习阶段。

暂停用`pause`、恢复用`resume`、跳过用`skip`。新一轮`start`保留历史和已见题。`--data-dir`可指定包外数据目录；默认使用当前用户数据目录，文件名为显式档案名。通过`export --output <包外路径>`导出。状态细节见[schemas-and-state.md](references/schemas-and-state.md)。

## 判分与复核

程序按受限数学语法核对结果。`pending`表示待复核，常见于自由文本、证明、单位、模型和解释。利用`inspect`读取评分要点，逐项检查学生的实际回答；缺少理由或条件时请学生补充，然后调用：

```bash
python -X utf8 scripts/diagnose.py --profile demo review --attempt 1 --verdict correct --reason "记录实际核验的条件、步骤或单位证据"
```

允许的复核结论为`correct/incorrect/pending/skip`。原答、旧判分和复核理由均保存；有提示的正确答案记录为“提示后完成”。比较等价方法时先对齐符号约定。证明题审核假设、关键步骤与结论；力学题审核数值、模型、单位、边界与适用假设。

表达式支持显式乘法`2*x`、幂`x**2`或`x^2`、允许的基本函数、英文变量、逗号分量。解析存疑或计算超时交给宿主复核；评分器只处理允许的数学语法。

## 跨课程回溯

先区分建模、物理概念、方法、数学计算、单位和符号，再按证据选择补习节点。依赖与应用关系见[cross-course-bridges.json](references/cross-course-bridges.json)。代数桥接补习矩阵位移法所需的矩阵方程知识。

```bash
python -X utf8 scripts/diagnose.py --profile demo start --skill materials.deflection
python -X utf8 scripts/diagnose.py --profile demo learn --skill math04.primitive
python -X utf8 scripts/diagnose.py --profile demo transfer --return-target
```

输出“观察—证据—待核验—下一步”，分别呈现本轮表现和历史记录。评价对象是具体答题步骤。专业题采用教材中的理想化模型，服务课程学习；实际工程安全评估应使用相应工程流程。

已有解题过程指出具体疑点时，在`start`附加`--focus <目标的前置技能>`及`--context '{"routing_evidence":"学生过程中的实际观察"}'`，从该节点开始核验。观察用于选择测试顺序，卡点判断依据后续作答。图中支座识别错误可先测`theory.model`，原函数积分错误可先测`math04.primitive`，边界错误可先测`materials.boundary`；目标仍为`materials.deflection`，补习后返回该目标。

## 支持范围与质量

目录位于[course-manifest.json](references/course-manifest.json)：高数12章及三门力学的主题级资源。按清单中的`file`读取相应`courses/`数据包。题目核对状态逐题记录；来源、覆盖粒度和验证状态集中见[sources-and-review.md](references/sources-and-review.md)。
