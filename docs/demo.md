# 演示与试用

以下为合成演示路径。命令在Skill目录运行，`python`须已安装SymPy。演示档案保存在包外数据目录，真实试用使用独立档案记录。

## 1. 复合求导遗漏

```bash
python -X utf8 scripts/diagnose.py --profile demo-chain start --skill math02.chain
python -X utf8 scripts/diagnose.py --profile demo-chain answer --answer "cos(x**2)"
python -X utf8 scripts/diagnose.py --profile demo-chain next
python -X utf8 scripts/diagnose.py --profile demo-chain answer --answer "cos(u)"
python -X utf8 scripts/diagnose.py --profile demo-chain next
python -X utf8 scripts/diagnose.py --profile demo-chain answer --answer "-sin(3*x)"
python -X utf8 scripts/diagnose.py --profile demo-chain next
python -X utf8 scripts/diagnose.py --profile demo-chain answer --answer "是"
python -X utf8 scripts/diagnose.py --profile demo-chain report
python -X utf8 scripts/diagnose.py --profile demo-chain learn --skill math02.chain
python -X utf8 scripts/diagnose.py --profile demo-chain transfer
```

预期：目标错题后转向基本求导，再用另一道目标题核验复合结构。报告保留逐题证据与待测内容。迁移题要求说明内层因子，表达式匹配后保留pending；宿主收到学生解释后再review。随后用retest获取另一道公开题面，答案留到复测完成后讲解。

## 2. 基本求导不稳

以math02.basic为目标，学生给sin(u)的导数误答sin(u)。下一题回溯math02.definition。只有该题出错的证据尚不足以认定定义不会；继续按程序分支核验，或在6题上限停止。补习basic后以未见迁移题复测。

## 3. 梁挠度的三种核验入口

共同目标materials.deflection；符号、支承、荷载和EI假设需先确认。

| 学生已有过程中的观察 | 起始focus | 要核验的假设 |
|---|---|---|
| 把固定端画成铰支座 | theory.model | 约束与受力模型可能不清 |
| 把2x的原函数写成2x² | math04.primitive | 可能存在基础积分错误 |
| 把简支端挠度和转角都设为零 | materials.boundary | 可能混淆边界条件 |

```bash
python -X utf8 scripts/diagnose.py --profile demo-beam start --skill materials.deflection --focus math04.primitive --context '{"routing_evidence":"学生把2x的原函数写成2x²"}'
python -X utf8 scripts/diagnose.py --profile demo-beam answer --answer "2*x**2"
python -X utf8 scripts/diagnose.py --profile demo-beam report
python -X utf8 scripts/diagnose.py --profile demo-beam learn --skill math04.primitive
python -X utf8 scripts/diagnose.py --profile demo-beam transfer --return-target
```

这些观察用于选择起始核验题，卡点判断依据后续回答。补习后回到悬臂端载迁移题，核对数值、模型、单位与边界。表达式解析存疑时保留pending，由宿主复核学生写法。

## 真实试用记录表

| 匿名档案 | 课程/目标 | 诊断题数和耗时 | 学生原始错误 | 助教复核意见 | 提示使用 | 独立迁移 | 后续未见题复测 | 再次使用 |
|---|---|---|---|---|---|---|---|---|

试用时用同一宿主模型的普通答疑做对照，控制时间、使用相近难度的不同新题并交替顺序。分别记录使用时表现、独立作答表现和满意度，以独立新题与后续复测评估学习结果。原始资料存包外，汇总使用去标识数据。
