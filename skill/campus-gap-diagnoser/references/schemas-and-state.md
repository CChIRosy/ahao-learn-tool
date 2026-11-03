# 课程与状态格式

课程清单只含技能元数据，脚本按file加载一个数据包。数据包字段为id/name/source/skills；每个技能包含id、name、aliases、prerequisites、tier、teaching、items、quality。前置依赖构成DAG；相关与应用关系独立记录，不能强制作为先修。

每技能五道原创题分别用于diagnostic、diagnostic、learning、transfer、retention。每道题含独立ID、题面、题型、答案、要点、提示、适用条件与审核字段。公开接口不返回答案或提示；请求提示后单独披露，学习接口明确展示例题。

档案必须显式命名，按当前操作系统用户隔离存储；它不是多用户服务的身份认证机制。文件保存version/profile/created_at/updated_at、当前session_id、目标target、focus、return_target、phase、diagnostic_count、当前题、hint_level、已见题ID、全部attempts、复核corrections和旧会话摘要history。不要存储姓名、学校、学号等非必要信息。

阶段为diagnostic/evidence_ready/learning/transfer/retention/paused/complete。每轮诊断最多6题；学习和复测不消耗诊断题额度。展示过的题进入seen，重开会话不清空；学习例题也会标记为已见。暂停保留当前题和阶段，恢复不丢失。

诊断中有pending作答时，next返回awaiting_review和待复核记录ID，完成复核后再选题。复核历史作答会保留当前待答题。pause可重复调用，resume恢复第一次暂停前的阶段；暂停期间next返回暂停状态。

verdict为correct/assisted/incorrect/pending/skip。有提示的正确结果记assisted。pending需宿主依据真实回答复核，不能直接等同错误。review保留修改前记录，正确复核也不能消除提示使用。report为每个技能显示最近一次涉及该技能的诊断会话证据，完整历史仍保留；复测表现另列，不把旧错题记录抹掉。

状态原子写入；新建会话保留历史。当前实现是本地单写者工具，同一档案不应由多个进程同时编辑；不同使用者应选不同档案名与数据目录。多人并发服务需要额外的认证、锁与数据存储设计。

数学评分器仅接受受限AST，不调用eval或对用户文本调用sympify；自动评分在子进程中最多运行4秒。允许基本算术、常数pi、指定变量和单参数函数sin/cos/tan/exp/log/sqrt/Abs/asin/acos/atan，要求显式乘号。长表达式、任意属性访问、下标、外部函数、过大指数等交给宿主复核。工程单位和符号约定不由字符相等自动判断。

带unit字段的题目支持Pa/kPa/MPa/GPa、N/kN、m/cm/mm、N*m/kN*m/N*mm的精确单位换算，并检查这些已知单位的量纲。其余单位语法交给宿主复核。按题目要求只输入数值时使用题设单位；换算吻合后，专业题仍保留模型与边界复核。单位识别不是通用自然语言物理量解析器。

向量支持逗号分量、圆括号和方括号。标记vector_equivalence=parallel的题目按非零平行向量核对，接受法向量、直线方向向量的非零倍数；其他向量题按分量比较。涉及同向、单位长度或正向的题目仍按各自要求核验。
