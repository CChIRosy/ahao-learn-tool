# 课程逐项覆盖核查（0.2.0）

按出版社目录与高校公开大纲核查知识主题、讲解、前置关系与五阶段起始题。高数含上下册全部82节（含星号节）。力学按以下来源和专项补充逐项映射。

“已映射起始题库”表示该清单项有可检索节点、讲解与题目。教师对题型深度、逐个定理证明和教学效果的验收单独记录。

## 基准来源

- [同济高等数学第八版上册出版社目录](https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=62cdab46938b7cc2960eedb1)：第1—7章全部46节，含星号节；附录按工具基础补充。
- [同济高等数学第八版下册出版社目录](https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=62bc8b97938b7cc2960eebb7)：第8—12章全部36节，含星号节。
- [复旦大学理论力学范围](https://aero-mech.fudan.edu.cn/1b/8a/c26484a465802/page.htm)：静力学、运动学、牛顿动力学、分析力学。
- [常州工学院课程大纲中的理论力学章节](https://tjxy.czu.cn/_upload/article/files/ae/f3/a23c80de499191499ecd231b4c02/5419a14d-f6b0-40e8-8fb0-dca6eccd31ad.pdf)：PDF印刷页44—46的课程内容；平面空间力系、摩擦与运动学。
- [北方工业大学材料力学课程及实验大纲](https://jwc.ncut.edu.cn/DG7204311.pdf)：8个理论教学单元及实验项目；能量、疲劳等另列专项扩展。
- [清华大学出版社Structural Mechanics详细目录](https://www.tup.tsinghua.edu.cn/booksCenter/bookcatalog?id=10424501)：公开详细目录第1—11章；按全部小节建立对应资源。

## 核查统计

```json
{
  "checklist_entries": 195,
  "math_publisher_sections": 82,
  "before_mapped": 70,
  "before_partial": 52,
  "before_missing": 73,
  "after_unmapped": 0,
  "skills": 209,
  "added_skills": 101
}
```

## 逐项映射

|清单项|知识要求|节点|0.1.1回查|0.2.0|
|---|---|---|---|---|
|math.1.1|映射与函数|math01.function、math01.inverse、math01.function-properties|原有节点需补充|已映射起始题库|
|math.1.2|数列的收敛定义和性质|math01.sequence、math01.quantifiers|原有节点需补充|已映射起始题库|
|math.1.3|函数极限及其性质|math01.limit、math01.quantifiers|原有节点需补充|已映射起始题库|
|math.1.4|无穷小和无穷大|math01.infinitesimal、math01.limit-laws|原有节点需补充|已映射起始题库|
|math.1.5|极限运算|math01.limit-laws|缺独立节点|已映射起始题库|
|math.1.6|存在准则和重要极限|math01.sequence、math01.limit、math01.infinitesimal、math01.limit-laws|原有节点需补充|已映射起始题库|
|math.1.7|无穷小阶比较|math01.infinitesimal|已有对应节点|已映射起始题库|
|math.1.8|连续与间断|math01.continuity|已有对应节点|已映射起始题库|
|math.1.9|连续性运算|math01.continuity、math01.uniform-continuity|原有节点需补充|已映射起始题库|
|math.1.10|闭区间性质与一致连续|math01.continuity、math01.uniform-continuity|原有节点需补充|已映射起始题库|
|math.2.1|导数含义和存在条件|math02.definition|已有对应节点|已映射起始题库|
|math.2.2|求导法则含反函数|math02.rules、math02.chain、math02.basic、math02.inverse-derivative|原有节点需补充|已映射起始题库|
|math.2.3|高阶导数|math02.higher|已有对应节点|已映射起始题库|
|math.2.4|隐式参数求导与相关速率|math02.implicit、math02.related-rates、math02.parametric-second|原有节点需补充|已映射起始题库|
|math.2.5|微分与近似|math02.differentials|缺独立节点|已映射起始题库|
|math.3.1|三类中值定理|math03.mvt、math03.proof|已有对应节点|已映射起始题库|
|math.3.2|不定式求极限|math03.lhopital|已有对应节点|已映射起始题库|
|math.3.3|泰勒展开与余项|math03.taylor、math03.remainders|原有节点需补充|已映射起始题库|
|math.3.4|单调凹凸|math03.extrema、math03.curvature|已有对应节点|已映射起始题库|
|math.3.5|极值和最值|math03.extrema|已有对应节点|已映射起始题库|
|math.3.6|函数图形|math03.asymptote|已有对应节点|已映射起始题库|
|math.3.7|曲率及相关几何|math03.curvature、math03.evolute|原有节点需补充|已映射起始题库|
|math.3.8|方程数值求根|math03.root-finding|缺独立节点|已映射起始题库|
|math.4.1|原函数与不定积分|math04.primitive|已有对应节点|已映射起始题库|
|math.4.2|换元|math04.substitution|已有对应节点|已映射起始题库|
|math.4.3|分部|math04.parts|已有对应节点|已映射起始题库|
|math.4.4|有理化积分|math04.rational、math04.trig-rational|原有节点需补充|已映射起始题库|
|math.4.5|查表和校验|math04.integral-table|缺独立节点|已映射起始题库|
|math.5.1|积分定义性质与近似|math05.definition、math05.riemann、math05.quadrature|原有节点需补充|已映射起始题库|
|math.5.2|微积分基本关系|math05.ftc|已有对应节点|已映射起始题库|
|math.5.3|积分计算方法|math05.methods|已有对应节点|已映射起始题库|
|math.5.4|反常积分|math05.improper|已有对应节点|已映射起始题库|
|math.5.5|积分判敛与Gamma|math05.gamma|缺独立节点|已映射起始题库|
|math.6.1|微元建模|math06.area|已有对应节点|已映射起始题库|
|math.6.2|面积体积和弧长|math06.area、math06.volume、math06.arc|已有对应节点|已映射起始题库|
|math.6.3|功压力和引力|math06.physics|已有对应节点|已映射起始题库|
|math.7.1|方程解与初值|math07.concept|已有对应节点|已映射起始题库|
|math.7.2|变量分离|math07.separable|已有对应节点|已映射起始题库|
|math.7.3|一阶齐次型及转化|math07.separable、math07.homogeneous-reducible|原有节点需补充|已映射起始题库|
|math.7.4|线性与伯努利|math07.linear、math07.bernoulli|原有节点需补充|已映射起始题库|
|math.7.5|高阶方程降阶|math07.reduction|缺独立节点|已映射起始题库|
|math.7.6|线性解结构与变易法|math07.order、math07.variation-systems|原有节点需补充|已映射起始题库|
|math.7.7|常系数齐次|math07.order|已有对应节点|已映射起始题库|
|math.7.8|常系数非齐次|math07.nonhomogeneous|已有对应节点|已映射起始题库|
|math.7.9|欧拉型|math07.exact-euler|已有对应节点|已映射起始题库|
|math.7.10|常系数系统|math07.variation-systems|缺独立节点|已映射起始题库|
|math.8.1|向量线性计算|math08.vectors|已有对应节点|已映射起始题库|
|math.8.2|三类向量乘积|math08.products、math08.mixed|已有对应节点|已映射起始题库|
|math.8.3|空间平面|math08.planes|已有对应节点|已映射起始题库|
|math.8.4|空间直线与距离角度|math08.planes、math08.metric|原有节点需补充|已映射起始题库|
|math.8.5|曲面|math08.surfaces|已有对应节点|已映射起始题库|
|math.8.6|空间曲线与投影|math08.surfaces、math08.mixed|已有对应节点|已映射起始题库|
|math.9.1|多元极限和点集|math09.limits|已有对应节点|已映射起始题库|
|math.9.2|偏导|math09.partial|已有对应节点|已映射起始题库|
|math.9.3|全微分|math09.partial、math09.differentiability|原有节点需补充|已映射起始题库|
|math.9.4|多元复合求导|math09.chain|已有对应节点|已映射起始题库|
|math.9.5|隐函数与方程组|math09.chain、math09.normal、math09.implicit-systems|原有节点需补充|已映射起始题库|
|math.9.6|空间微分几何|math09.geometry、math09.vector-curves|原有节点需补充|已映射起始题库|
|math.9.7|方向导数梯度|math09.geometry|已有对应节点|已映射起始题库|
|math.9.8|无约束和约束极值|math09.extrema|已有对应节点|已映射起始题库|
|math.9.9|二元泰勒|math09.taylor|缺独立节点|已映射起始题库|
|math.9.10|最小二乘|math09.least-squares|缺独立节点|已映射起始题库|
|math.10.1|二重积分性质|math10.double|已有对应节点|已映射起始题库|
|math.10.2|二重积分计算与换元|math10.double、math10.polar|已有对应节点|已映射起始题库|
|math.10.3|三重积分|math10.triple|已有对应节点|已映射起始题库|
|math.10.4|几何物理应用|math10.applications、math10.surface-gravity|原有节点需补充|已映射起始题库|
|math.10.5|参数积分|math10.parameter|缺独立节点|已映射起始题库|
|math.11.1|弧长积分|math11.line1|已有对应节点|已映射起始题库|
|math.11.2|有向线积分与两类联系|math11.line2、math11.line-connections|原有节点需补充|已映射起始题库|
|math.11.3|格林公式与势函数|math11.potential|已有对应节点|已映射起始题库|
|math.11.4|面积积分|math11.surface1|已有对应节点|已映射起始题库|
|math.11.5|定向面积积分与两类联系|math11.surface-orientation|缺独立节点|已映射起始题库|
|math.11.6|高斯与散度|math11.gauss|已有对应节点|已映射起始题库|
|math.11.7|斯托克斯与旋度|math11.stokes、math11.line-connections|原有节点需补充|已映射起始题库|
|math.12.1|常数项级数及柯西准则|math12.series、math12.cauchy|原有节点需补充|已映射起始题库|
|math.12.2|常数项判敛|math12.positive、math12.alternating|已有对应节点|已映射起始题库|
|math.12.3|幂级数域与运算|math12.power|已有对应节点|已映射起始题库|
|math.12.4|展开|math12.expansion|已有对应节点|已映射起始题库|
|math.12.5|近似方程级数解和欧拉公式|math12.power-applications|缺独立节点|已映射起始题库|
|math.12.6|一致收敛|math12.uniform|已有对应节点|已映射起始题库|
|math.12.7|傅里叶与半区间展开|math12.fourier、math12.half-range|原有节点需补充|已映射起始题库|
|math.12.8|一般周期与复形式|math12.fourier、math12.half-range|原有节点需补充|已映射起始题库|
|structures.1.1|目录1.1：结构计算模型、杆系分类与荷载分类|structures.overview|缺独立节点|已映射起始题库|
|structures.1.2|目录1.2：结构计算模型、杆系分类与荷载分类|structures.overview|缺独立节点|已映射起始题库|
|structures.1.3|目录1.3：结构计算模型、杆系分类与荷载分类|structures.overview|缺独立节点|已映射起始题库|
|structures.1.4|目录1.4：结构计算模型、杆系分类与荷载分类|structures.overview|缺独立节点|已映射起始题库|
|structures.2.1|目录2.1：几何组成、约束与计算简图|structures.geometry|已有对应节点|已映射起始题库|
|structures.2.2|目录2.2：几何组成规则、瞬变体系与自由度|structures.geometry-rules|缺独立节点|已映射起始题库|
|structures.2.3|目录2.3：几何组成规则、瞬变体系与自由度|structures.geometry-rules|缺独立节点|已映射起始题库|
|structures.2.4|目录2.4：几何组成、约束与计算简图；力法、基本体系与协调方程|structures.geometry、structures.force|已有对应节点|已映射起始题库|
|structures.3.1|目录3.1：静定梁、刚架与内力校核|structures.determinate|已有对应节点|已映射起始题库|
|structures.3.2|目录3.2：多跨静定梁、内铰与分层传力|structures.gerber|缺独立节点|已映射起始题库|
|structures.3.3|目录3.3：静定刚架的分段内力与节点平衡|structures.frame|缺独立节点|已映射起始题库|
|structures.3.4|目录3.4：桁架节点法、截面法与零杆|structures.truss-methods|缺独立节点|已映射起始题库|
|structures.3.5|目录3.5：三铰拱、水平推力与合理拱轴|structures.arch|缺独立节点|已映射起始题库|
|structures.3.6|目录3.6：组合结构与静定结构特性|structures.mixed|缺独立节点|已映射起始题库|
|structures.4.1|目录4.1：虚功、位移计算与互等定理|structures.virtual|已有对应节点|已映射起始题库|
|structures.4.2|目录4.2：虚功、位移计算与互等定理|structures.virtual|已有对应节点|已映射起始题库|
|structures.4.3|目录4.3：虚功、位移计算与互等定理；单位荷载法、图乘法与弯矩面积|structures.virtual、structures.diagram-product|原有节点需补充|已映射起始题库|
|structures.4.4|目录4.4：单位荷载法、图乘法与弯矩面积|structures.diagram-product|缺独立节点|已映射起始题库|
|structures.4.5|目录4.5：温度、支座移动与非荷载作用|structures.loads|已有对应节点|已映射起始题库|
|structures.4.6|目录4.6：功、位移、反力与柔度互等|structures.reciprocity|缺独立节点|已映射起始题库|
|structures.5.1|目录5.1：影响线、移动荷载与包络|structures.influence|已有对应节点|已映射起始题库|
|structures.5.2|目录5.2：影响线、移动荷载与包络|structures.influence|已有对应节点|已映射起始题库|
|structures.5.3|目录5.3：间接荷载、桁架与结点荷载影响线|structures.indirect-influence|缺独立节点|已映射起始题库|
|structures.5.4|目录5.4：间接荷载、桁架与结点荷载影响线|structures.indirect-influence|缺独立节点|已映射起始题库|
|structures.5.5|目录5.5：机动法、最不利布载与绝对最大弯矩|structures.muller|缺独立节点|已映射起始题库|
|structures.5.6|目录5.6：机动法、最不利布载与绝对最大弯矩|structures.muller|缺独立节点|已映射起始题库|
|structures.5.7|目录5.7：机动法、最不利布载与绝对最大弯矩|structures.muller|缺独立节点|已映射起始题库|
|structures.6.1|目录6.1：力法、基本体系与协调方程|structures.force|已有对应节点|已映射起始题库|
|structures.6.2|目录6.2：力法、基本体系与协调方程|structures.force|已有对应节点|已映射起始题库|
|structures.6.3|目录6.3：力法协调、对称性与内力校核|structures.force-details|缺独立节点|已映射起始题库|
|structures.6.4|目录6.4：力法协调、对称性与内力校核|structures.force-details|缺独立节点|已映射起始题库|
|structures.6.5|目录6.5：温度、支座移动与非荷载作用；力法协调、对称性与内力校核|structures.loads、structures.force-details|原有节点需补充|已映射起始题库|
|structures.6.6|目录6.6：力法协调、对称性与内力校核|structures.force-details|缺独立节点|已映射起始题库|
|structures.6.7|目录6.7：力法协调、对称性与内力校核|structures.force-details|缺独立节点|已映射起始题库|
|structures.6.8|目录6.8：力法协调、对称性与内力校核|structures.force-details|缺独立节点|已映射起始题库|
|structures.6.9|目录6.9：转角位移方程、固端弯矩与杆端刚度|structures.slope-deflection|缺独立节点|已映射起始题库|
|structures.7.1|目录7.1：位移法与转角位移方程|structures.displacement|已有对应节点|已映射起始题库|
|structures.7.2|目录7.2：位移法与转角位移方程；位移法基本未知量、侧移与对称简化|structures.displacement、structures.sway|原有节点需补充|已映射起始题库|
|structures.7.3|目录7.3：位移法与转角位移方程；转角位移方程、固端弯矩与杆端刚度|structures.displacement、structures.slope-deflection|原有节点需补充|已映射起始题库|
|structures.7.4|目录7.4：位移法与转角位移方程；位移法基本未知量、侧移与对称简化|structures.displacement、structures.sway|原有节点需补充|已映射起始题库|
|structures.8.1|目录8.1：矩阵位移法与线性代数桥接|structures.matrix|已有对应节点|已映射起始题库|
|structures.8.2|目录8.2：单元刚度、坐标变换、组装与边界|structures.matrix-assembly|缺独立节点|已映射起始题库|
|structures.8.3|目录8.3：单元刚度、坐标变换、组装与边界|structures.matrix-assembly|缺独立节点|已映射起始题库|
|structures.8.4|目录8.4：单元刚度、坐标变换、组装与边界|structures.matrix-assembly|缺独立节点|已映射起始题库|
|structures.8.5|目录8.5：单元刚度、坐标变换、组装与边界|structures.matrix-assembly|缺独立节点|已映射起始题库|
|structures.8.6|目录8.6：单元刚度、坐标变换、组装与边界|structures.matrix-assembly|缺独立节点|已映射起始题库|
|structures.9.1|目录9.1：结构动力与单自由度响应|structures.dynamics|已有对应节点|已映射起始题库|
|structures.9.2|目录9.2：结构动力与单自由度响应|structures.dynamics|已有对应节点|已映射起始题库|
|structures.9.3|目录9.3：结构动力与单自由度响应|structures.dynamics|已有对应节点|已映射起始题库|
|structures.9.4|目录9.4：阻尼受迫响应、振型分解与参与系数|structures.forced-modal|缺独立节点|已映射起始题库|
|structures.9.5|目录9.5：多自由度自由振动、频率与振型|structures.modal|缺独立节点|已映射起始题库|
|structures.9.6|目录9.6：阻尼受迫响应、振型分解与参与系数|structures.forced-modal|缺独立节点|已映射起始题库|
|structures.9.7|目录9.7：阻尼受迫响应、振型分解与参与系数|structures.forced-modal|缺独立节点|已映射起始题库|
|structures.9.8|目录9.8：瑞利法、集中质量与频率近似|structures.rayleigh|缺独立节点|已映射起始题库|
|structures.10.1|目录10.1：极限荷载与塑性机构|structures.plastic|已有对应节点|已映射起始题库|
|structures.10.2|目录10.2：塑性铰、极限分析上下限定理|structures.plastic-bounds|缺独立节点|已映射起始题库|
|structures.10.3|目录10.3：梁、连续梁与刚架的塑性机构|structures.plastic-mechanisms|缺独立节点|已映射起始题库|
|structures.10.4|目录10.4：塑性铰、极限分析上下限定理|structures.plastic-bounds|缺独立节点|已映射起始题库|
|structures.10.5|目录10.5：梁、连续梁与刚架的塑性机构|structures.plastic-mechanisms|缺独立节点|已映射起始题库|
|structures.10.6|目录10.6：梁、连续梁与刚架的塑性机构|structures.plastic-mechanisms|缺独立节点|已映射起始题库|
|structures.11.1|目录11.1：结构稳定与临界荷载|structures.stability|已有对应节点|已映射起始题库|
|structures.11.2|目录11.2：结构稳定的静力法、能量法与弹性支承|structures.elastic-stability|缺独立节点|已映射起始题库|
|structures.11.3|目录11.3：结构稳定的静力法、能量法与弹性支承|structures.elastic-stability|缺独立节点|已映射起始题库|
|structures.11.4|目录11.4：结构稳定的静力法、能量法与弹性支承|structures.elastic-stability|缺独立节点|已映射起始题库|
|structures.11.5|目录11.5：变截面、剪切影响与组合压杆稳定|structures.advanced-buckling|缺独立节点|已映射起始题库|
|structures.11.6|目录11.6：变截面、剪切影响与组合压杆稳定|structures.advanced-buckling|缺独立节点|已映射起始题库|
|structures.11.7|目录11.7：变截面、剪切影响与组合压杆稳定|structures.advanced-buckling|缺独立节点|已映射起始题库|
|theory.unit.1|静力学公理、等效和各类平面力系|theory.force-systems、theory.model、theory.force、theory.balance|原有节点需补充|已映射起始题库|
|theory.unit.2|空间力系、主矢主矩与空间平衡|theory.space|缺独立节点|已映射起始题库|
|theory.unit.3|物体系受力与约束、支反力|theory.model、theory.balance|已有对应节点|已映射起始题库|
|theory.unit.4|摩擦、摩擦角、自锁及滚动摩阻|theory.friction、theory.friction-angle|原有节点需补充|已映射起始题库|
|theory.unit.5|重心与组合体|theory.centroid|缺独立节点|已映射起始题库|
|theory.unit.6|点的位置速度加速度、自然与极坐标|theory.point、theory.polar|原有节点需补充|已映射起始题库|
|theory.unit.7|刚体平动和定轴转动|theory.rigid|已有对应节点|已映射起始题库|
|theory.unit.8|平面刚体基点法、瞬心及加速度|theory.rigid、theory.planar-acceleration|原有节点需补充|已映射起始题库|
|theory.unit.9|点合成运动及科氏项|theory.relative、theory.coriolis|原有节点需补充|已映射起始题库|
|theory.unit.10|惯性与非惯性系质点动力学|theory.newton、theory.relative-dynamics|原有节点需补充|已映射起始题库|
|theory.unit.11|质点系动量、冲量与质心运动|theory.momentum、theory.newton|已有对应节点|已映射起始题库|
|theory.unit.12|动量矩、冲量矩及定轴动力学|theory.angular、theory.rigid-dynamics|原有节点需补充|已映射起始题库|
|theory.unit.13|质量转动惯量与惯性积|theory.inertia|缺独立节点|已映射起始题库|
|theory.unit.14|功、势能、动能与柯尼希分解|theory.energy、theory.konig|原有节点需补充|已映射起始题库|
|theory.unit.15|刚体平面动力学与普遍定理综合|theory.rigid-dynamics|缺独立节点|已映射起始题库|
|theory.unit.16|碰撞与恢复系数|theory.impact|缺独立节点|已映射起始题库|
|theory.unit.17|动静法和轴承动反力|theory.dalembert、theory.rotor-balance|原有节点需补充|已映射起始题库|
|theory.unit.18|完整非完整约束、自由度与广义坐标|theory.constraints|缺独立节点|已映射起始题库|
|theory.unit.19|虚位移、理想约束与广义力|theory.virtual-work|缺独立节点|已映射起始题库|
|theory.unit.20|拉格朗日第二类方程及首次积分|theory.lagrange|缺独立节点|已映射起始题库|
|theory.unit.21|平衡位置稳定性和单自由度振动|theory.equilibrium-stability、theory.analytical、theory.damped-forced|原有节点需补充|已映射起始题库|
|theory.unit.22|定点转动与陀螺入门扩展|theory.gyroscope|缺独立节点|已映射起始题库|
|theory.unit.23|变质量动力学扩展|theory.variable-mass|缺独立节点|已映射起始题库|
|materials.unit.1|变形体基本假设与三类设计目标|materials.basics、materials.section|原有节点需补充|已映射起始题库|
|materials.unit.2|拉压内力、斜截面应力与弹性变形|materials.axial、materials.oblique|原有节点需补充|已映射起始题库|
|materials.unit.3|材料性能、拉压试验及安全系数|materials.properties、materials.design|缺独立节点|已映射起始题库|
|materials.unit.4|剪切与挤压连接|materials.shear|已有对应节点|已映射起始题库|
|materials.unit.5|圆轴与薄壁圆筒扭转、功率及刚度|materials.torsion、materials.thin-wall、materials.shaft-power|原有节点需补充|已映射起始题库|
|materials.unit.6|梁剪力弯矩与正剪应力分布|materials.moment、materials.bending、materials.shear-flow|原有节点需补充|已映射起始题库|
|materials.unit.7|梁挠度、转角、积分法与刚度|materials.deflection、materials.boundary|已有对应节点|已映射起始题库|
|materials.unit.8|平面空间应力、应变与强度准则|materials.stress、materials.mohr、materials.generalized-hooke、materials.criteria、materials.brittle-criteria|原有节点需补充|已映射起始题库|
|materials.unit.9|拉弯、弯扭、斜弯与偏心核心|materials.combined、materials.unsymmetric、materials.core|原有节点需补充|已映射起始题库|
|materials.unit.10|欧拉、柔度区间和稳定设计|materials.stability、materials.stability-design|原有节点需补充|已映射起始题库|
|materials.unit.11|拉伸扭转和弯曲实验与电测|materials.experiments、materials.rosette|缺独立节点|已映射起始题库|
|materials.unit.12|截面静矩、惯性积、主轴和平行轴|materials.geometry、materials.principal-inertia|原有节点需补充|已映射起始题库|
|materials.unit.13|能量法、卡氏定理与单位载荷|materials.energy、materials.castigliano|原有节点需补充|已映射起始题库|
|materials.unit.14|超静定、温度和装配协调|materials.indeterminate、materials.thermal|原有节点需补充|已映射起始题库|
|materials.unit.15|落重、动载、疲劳循环与缺口|materials.fatigue、materials.impact、materials.fatigue-detail、materials.concentration|原有节点需补充|已映射起始题库|
|materials.unit.16|非圆及开口翘曲、多室薄壁扩展|materials.noncircular、materials.thin-wall|缺独立节点|已映射起始题库|
|materials.unit.17|薄壁容器与强度应用扩展|materials.pressure-vessels|缺独立节点|已映射起始题库|
|specialist.math02.composition|专项补充：复合函数结构识别|math02.composition|已有对应节点|已映射起始题库|
|specialist.math06.revolution-area|专项补充：旋转曲面的面积|math06.revolution-area|缺独立节点|已映射起始题库|
|specialist.structures.truss|专项补充：桁架与拱|structures.truss|已有对应节点|已映射起始题库|
|specialist.structures.distribution|专项补充：力矩分配、分配系数与传递|structures.distribution|已有对应节点|已映射起始题库|
|specialist.structures.algebra-bridge|专项补充：矩阵方程桥接基础|structures.algebra-bridge|已有对应节点|已映射起始题库|
|specialist.structures.distribution-details|专项补充：力矩分配、传递系数与迭代收敛|structures.distribution-details|缺独立节点|已映射起始题库|

## 资源深度与验收

每节点包含两道诊断题、一道补习题、一条迁移与一条后续复测。开放推导、实验方案、复杂图形题由宿主按评分要点复核。所有teacher_reviewed与student_validated保留false，计算核对数量独立统计。

学校自选章节、教材附录、完整实验操作流程和研究生专题会因课程而异；本报告以已列目录和大纲为验收基准。需要某校逐周对齐时使用该校正式大纲扩展清单。
