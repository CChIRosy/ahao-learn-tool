# 来源与审核状态

本包0.1.1包含高数上下册12章与理论力学、材料力学、结构力学的主题级原创题库。教材与高校大纲用于确定课程范围，题目与讲解由本项目编写。验证状态按下列字段记录。

## 范围来源

- 同济高等数学第八版上下册配套目录：https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=63af1979938b7cc2960ef745
- 同济高等数学第八版下册：https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=62bc8b97938b7cc2960eebb7
- 理论力学范围：https://aero-mech.fudan.edu.cn/1b/8a/c26484a465802/page.htm
- 材料力学大纲：https://me.sjtu.edu.cn/bkjx/upload/file/20220926/20220926103825.pdf
- 结构力学见土木工程大纲汇编的对应课程章节：https://cec.hrbeu.edu.cn/_upload/article/files/4a/00/2bbccea0465ea0f94fe98f8a1a6a/3a639add-0f08-449e-ad50-1bbf1b9c19f4.pdf
- 结构力学扩展内容：https://www.tup.tsinghua.edu.cn/booksCenter/book_10424501.html

核对日期为2026-11-03。配套目录在前期选题中已查阅，本轮刷新超时；下册出版社页面、材料力学PDF、理论力学页面与结构力学汇编可获取。结构力学范围取自汇编中的对应课程章节。学校和教材版本差异通过主题映射处理。

## 逐题质量字段

- `key_parsed`：参考结果通过受限数学语法或选项/开放答案格式检查。
- `independent_oracle`：开发过程中另写计算表达式，用SymPy或直接代数核对指定题目的参考结果。它记录参考数值或表达式的核对情况。
- `teacher_reviewed`：本版本均为false。
- `student_validated`：本版本均为false。

全部题目由同一开发过程编写与复核；教师审核和真实学生验证待执行。开放证明、物理模型和单位由宿主依据评分要点审核，待补充证据的回答保留pending。程序检查、教师审核与学习成效是三个独立层级。

## 范围和深度

108个节点按知识主题组织，部分节点合并相邻教材小节；每节点提供五道起始题，题型深度与逐小节映射待教师验收。题池耗尽后补充审核的新题。线性代数部分聚焦矩阵位移法所需的矩阵方程；完整线性代数、概率论和复变函数留给各自课程模块。

专业题采用明确的教材理想化模型与基本原理。复杂空间结构、非线性分析、真实结构安全与施工决策需要相应工程分析流程。图形理解与开放论证由宿主处理；脚本负责已确认题意后的测试流程和结果核对。

程序验证记录见仓库docs/validation.md和docs/review-report.md。后续真实试用需测量诊断一致性、独立迁移和隔日保持，再更新student_validated及相应证据。
