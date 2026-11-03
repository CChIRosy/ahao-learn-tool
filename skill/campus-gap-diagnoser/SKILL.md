---
name: campus-gap-diagnoser
description: 用短测定位大学高数、理论力学、材料力学、结构力学的学习卡点，提供带答题证据的补习与独立复测。适用于“看了解析仍不懂”“卡在哪一步”“继续上次卡点”、梁挠度等专业题回溯数学前置的请求。
---

# 卡点侦探

## 开始一次学习

使用宿主已有模型进行解释、图像确认和开放回答审核；使用本包Python脚本管理题库、分支与学习档案。需要Python 3.10+和`requirements.txt`中的依赖。先确认用户选择的本地档案名，示例中用`demo`；不要自动混用其他人的档案。

1. 获取用户题目和已有过程。截图先确认识别文字；力学图题确认支座、连接、荷载、尺寸、坐标、正号与单位。无法确认就先补充，不猜测图形。
2. 用课程目录和搜索寻找支持的目标，再读该技能及必要前置；不要一次加载全部题库。候选相近时请用户确认课程和目标。
3. 由脚本一次发一道诊断题；只展示公开题面。最多6道，接受“不会”、提示、跳过和暂停。已有过程可辅助选目标，但不能伪造用户作答记录。
4. 根据答题证据输出卡点卡；证据不足就保留多个候选，不以一道错题确定根因，不给未经校准的掌握百分比。
5. 选择优先补习技能，用短解释和题库例题讲解，随后给未见迁移题；专业课补了数学前置后，再返回专业情境迁移。
6. 下次使用未见题后续复测；题池耗尽时说明需要新增审核题，不重复已展示题冒充独立复测。没有调度工具时不声称设置了提醒。

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

`inspect`和`learn`包含答案，供宿主备课或明确的补习使用，不能将其内容提前展示为诊断或独立复测题。`next/start/transfer/retest`只返回公开题面。

暂停用`pause`、恢复用`resume`、跳过用`skip`。新一轮`start`保留历史和已见题，不擅自清空旧档案。`--data-dir`可以指定包外数据目录；默认使用当前用户数据目录，文件名为显式档案名。通过`export --output <包外路径>`导出。状态细节见[schemas-and-state.md](references/schemas-and-state.md)。

## 判分与复核

程序按受限数学语法做结果核对。`pending`不是错误：可能是自由文本、证明、单位、模型或解释需核验。利用`inspect`读取评分要点，逐项检查学生的实际回答；需要用户补充时先问，不代填学生解释。然后调用：

```bash
python -X utf8 scripts/diagnose.py --profile demo review --attempt 1 --verdict correct --reason "记录实际核验的条件、步骤或单位证据"
```

允许的复核结论为`correct/incorrect/pending/skip`。原答、旧判分和复核理由均保存；有提示的正确答案仍为“提示后完成”。等价方法和不同符号约定先对齐，不能因与参考写法不同直接判错。证明题检查假设、关键步骤、结论，不用数值一致代替证明。力学数值结果吻合后仍须核对模型、单位、边界与假设。

表达式支持显式乘法`2*x`、幂`x**2`或`x^2`、允许的基本函数、英文变量、逗号分量。无法可靠解析或计算超时交给宿主复核，不执行用户代码。

## 跨课程回溯

先区分建模、物理概念、方法、数学计算、单位和符号；只有证据支持时才回到数学补习。依赖与应用关系见[cross-course-bridges.json](references/cross-course-bridges.json)。矩阵位移法的代数桥接不代表完整线性代数课程。

```bash
python -X utf8 scripts/diagnose.py --profile demo start --skill materials.deflection
python -X utf8 scripts/diagnose.py --profile demo learn --skill math04.primitive
python -X utf8 scripts/diagnose.py --profile demo transfer --return-target
```

输出“观察—证据—待核验—下一步”，明确本轮表现与历史，不因新题答对就自动确认全部前置掌握。卡点不用于评价智力或人格；本包专业题用于课程学习，不提供实际工程安全结论。

已有解题过程指出具体疑点时，可以在`start`附加`--focus <目标的前置技能>`及`--context '{"routing_evidence":"学生过程中的实际观察"}'`，从该节点开始核验。它只改变核验顺序，不表示已确诊。图中支座识别错误可先测`theory.model`，原函数积分错误可先测`math04.primitive`，边界错误可先测`materials.boundary`；目标仍为`materials.deflection`，补习后返回该目标。

## 支持范围与质量

目录位于[course-manifest.json](references/course-manifest.json)：高数12章及三门力学的主题级资源。按清单中的`file`读取相应`courses/`数据包。题目核对状态逐题记录；[sources-and-review.md](references/sources-and-review.md)说明来源、审核边界和未覆盖的深度。没有教师审核或真实学生试用时，如实说明，不以脚本测试冒充学习效果。
