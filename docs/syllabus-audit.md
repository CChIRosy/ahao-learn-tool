# 课程逐项覆盖核查（0.3.0）

按出版社目录与高校公开大纲核查知识主题、讲解、前置关系与五阶段起始题。高数含上下册全部82节（含星号节）。力学按以下来源和专项补充逐项映射。钢结构与河海部分按用户确认范围建立主题级资源。

“已映射起始题库”表示该清单项有可检索节点、讲解与题目。教师对题型深度、逐个定理证明和教学效果的验收单独记录。

## 基准来源

- [同济高等数学第八版上册出版社目录](https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=62cdab46938b7cc2960eedb1)：第1—7章全部46节，含星号节；附录按工具基础补充。
- [同济高等数学第八版下册出版社目录](https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=62bc8b97938b7cc2960eebb7)：第8—12章全部36节，含星号节。
- [复旦大学理论力学范围](https://aero-mech.fudan.edu.cn/1b/8a/c26484a465802/page.htm)：静力学、运动学、牛顿动力学、分析力学。
- [常州工学院课程大纲中的理论力学章节](https://tjxy.czu.cn/_upload/article/files/ae/f3/a23c80de499191499ecd231b4c02/5419a14d-f6b0-40e8-8fb0-dca6eccd31ad.pdf)：PDF印刷页44—46的课程内容；平面空间力系、摩擦与运动学。
- [北方工业大学材料力学课程及实验大纲](https://jwc.ncut.edu.cn/DG7204311.pdf)：8个理论教学单元及实验项目；能量、疲劳等另列专项扩展。
- [清华大学出版社Structural Mechanics详细目录](https://www.tup.tsinghua.edu.cn/booksCenter/bookcatalog?id=10424501)：公开详细目录第1—11章；按全部小节建立对应资源。
- [湖南大学钢结构设计原理课程大纲](https://ce.hnu.edu.cn/info/1025/1809.htm)：材料、设计原理、连接、基本构件和普通钢屋架；体系、耐久与施工列为应用补充。
- [同济团队钢结构基本原理课程介绍](https://dxs.moe.gov.cn/zx/a/kskt_dxmk/240307/1746933.shtml)：材料、构件、连接与节点的工作性能和设计原理。
- [济南大学水力学教学大纲](https://zh.ujn.edu.cn/info/1079/4725.htm)：水静力、运动学、三大方程、阻力管流、明渠、堰闸、渗流及模型。
- [河海大学河流动力学课程团队大纲](https://www.icourse163.org/spoc/course/HHU-1461704163?tid=1462484444)：泥沙特性、起动、推移悬移、异重流、河床与河口演变。
- [河海大学海岸动力学课程团队大纲](https://www.icourse163.org/course/HHU-1206808802?tid=1476735446)：波浪、近岸流、海岸泥沙和岸滩变化；波浪相互作用与防护列应用节点。
- [河海大学港口水工建筑物课程团队大纲](https://www.icourse163.org/course/HHU-1206790814?tid=1473313475)：码头作用、重力式、高桩式、板桩式码头；布置、航道和疏浚列基础应用。

## 核查统计

```json
{
  "checklist_entries": 272,
  "math_publisher_sections": 82,
  "before_mapped": 70,
  "before_partial": 52,
  "before_missing": 150,
  "after_unmapped": 0,
  "skills": 286,
  "added_skills": 77,
  "previously_mapped_entries": 195,
  "new_entries": 77
}
```

## 逐项映射

|清单项|知识要求|节点|0.2.0回查|0.3.0|
|---|---|---|---|---|
|math.1.1|映射与函数|math01.function、math01.inverse、math01.function-properties|已有对应节点|已映射起始题库|
|math.1.2|数列的收敛定义和性质|math01.sequence、math01.quantifiers|已有对应节点|已映射起始题库|
|math.1.3|函数极限及其性质|math01.limit、math01.quantifiers|已有对应节点|已映射起始题库|
|math.1.4|无穷小和无穷大|math01.infinitesimal、math01.limit-laws|已有对应节点|已映射起始题库|
|math.1.5|极限运算|math01.limit-laws|已有对应节点|已映射起始题库|
|math.1.6|存在准则和重要极限|math01.sequence、math01.limit、math01.infinitesimal、math01.limit-laws|已有对应节点|已映射起始题库|
|math.1.7|无穷小阶比较|math01.infinitesimal|已有对应节点|已映射起始题库|
|math.1.8|连续与间断|math01.continuity|已有对应节点|已映射起始题库|
|math.1.9|连续性运算|math01.continuity、math01.uniform-continuity|已有对应节点|已映射起始题库|
|math.1.10|闭区间性质与一致连续|math01.continuity、math01.uniform-continuity|已有对应节点|已映射起始题库|
|math.2.1|导数含义和存在条件|math02.definition|已有对应节点|已映射起始题库|
|math.2.2|求导法则含反函数|math02.rules、math02.chain、math02.basic、math02.inverse-derivative|已有对应节点|已映射起始题库|
|math.2.3|高阶导数|math02.higher|已有对应节点|已映射起始题库|
|math.2.4|隐式参数求导与相关速率|math02.implicit、math02.related-rates、math02.parametric-second|已有对应节点|已映射起始题库|
|math.2.5|微分与近似|math02.differentials|已有对应节点|已映射起始题库|
|math.3.1|三类中值定理|math03.mvt、math03.proof|已有对应节点|已映射起始题库|
|math.3.2|不定式求极限|math03.lhopital|已有对应节点|已映射起始题库|
|math.3.3|泰勒展开与余项|math03.taylor、math03.remainders|已有对应节点|已映射起始题库|
|math.3.4|单调凹凸|math03.extrema、math03.curvature|已有对应节点|已映射起始题库|
|math.3.5|极值和最值|math03.extrema|已有对应节点|已映射起始题库|
|math.3.6|函数图形|math03.asymptote|已有对应节点|已映射起始题库|
|math.3.7|曲率及相关几何|math03.curvature、math03.evolute|已有对应节点|已映射起始题库|
|math.3.8|方程数值求根|math03.root-finding|已有对应节点|已映射起始题库|
|math.4.1|原函数与不定积分|math04.primitive|已有对应节点|已映射起始题库|
|math.4.2|换元|math04.substitution|已有对应节点|已映射起始题库|
|math.4.3|分部|math04.parts|已有对应节点|已映射起始题库|
|math.4.4|有理化积分|math04.rational、math04.trig-rational|已有对应节点|已映射起始题库|
|math.4.5|查表和校验|math04.integral-table|已有对应节点|已映射起始题库|
|math.5.1|积分定义性质与近似|math05.definition、math05.riemann、math05.quadrature|已有对应节点|已映射起始题库|
|math.5.2|微积分基本关系|math05.ftc|已有对应节点|已映射起始题库|
|math.5.3|积分计算方法|math05.methods|已有对应节点|已映射起始题库|
|math.5.4|反常积分|math05.improper|已有对应节点|已映射起始题库|
|math.5.5|积分判敛与Gamma|math05.gamma|已有对应节点|已映射起始题库|
|math.6.1|微元建模|math06.area|已有对应节点|已映射起始题库|
|math.6.2|面积体积和弧长|math06.area、math06.volume、math06.arc|已有对应节点|已映射起始题库|
|math.6.3|功压力和引力|math06.physics|已有对应节点|已映射起始题库|
|math.7.1|方程解与初值|math07.concept|已有对应节点|已映射起始题库|
|math.7.2|变量分离|math07.separable|已有对应节点|已映射起始题库|
|math.7.3|一阶齐次型及转化|math07.separable、math07.homogeneous-reducible|已有对应节点|已映射起始题库|
|math.7.4|线性与伯努利|math07.linear、math07.bernoulli|已有对应节点|已映射起始题库|
|math.7.5|高阶方程降阶|math07.reduction|已有对应节点|已映射起始题库|
|math.7.6|线性解结构与变易法|math07.order、math07.variation-systems|已有对应节点|已映射起始题库|
|math.7.7|常系数齐次|math07.order|已有对应节点|已映射起始题库|
|math.7.8|常系数非齐次|math07.nonhomogeneous|已有对应节点|已映射起始题库|
|math.7.9|欧拉型|math07.exact-euler|已有对应节点|已映射起始题库|
|math.7.10|常系数系统|math07.variation-systems|已有对应节点|已映射起始题库|
|math.8.1|向量线性计算|math08.vectors|已有对应节点|已映射起始题库|
|math.8.2|三类向量乘积|math08.products、math08.mixed|已有对应节点|已映射起始题库|
|math.8.3|空间平面|math08.planes|已有对应节点|已映射起始题库|
|math.8.4|空间直线与距离角度|math08.planes、math08.metric|已有对应节点|已映射起始题库|
|math.8.5|曲面|math08.surfaces|已有对应节点|已映射起始题库|
|math.8.6|空间曲线与投影|math08.surfaces、math08.mixed|已有对应节点|已映射起始题库|
|math.9.1|多元极限和点集|math09.limits|已有对应节点|已映射起始题库|
|math.9.2|偏导|math09.partial|已有对应节点|已映射起始题库|
|math.9.3|全微分|math09.partial、math09.differentiability|已有对应节点|已映射起始题库|
|math.9.4|多元复合求导|math09.chain|已有对应节点|已映射起始题库|
|math.9.5|隐函数与方程组|math09.chain、math09.normal、math09.implicit-systems|已有对应节点|已映射起始题库|
|math.9.6|空间微分几何|math09.geometry、math09.vector-curves|已有对应节点|已映射起始题库|
|math.9.7|方向导数梯度|math09.geometry|已有对应节点|已映射起始题库|
|math.9.8|无约束和约束极值|math09.extrema|已有对应节点|已映射起始题库|
|math.9.9|二元泰勒|math09.taylor|已有对应节点|已映射起始题库|
|math.9.10|最小二乘|math09.least-squares|已有对应节点|已映射起始题库|
|math.10.1|二重积分性质|math10.double|已有对应节点|已映射起始题库|
|math.10.2|二重积分计算与换元|math10.double、math10.polar|已有对应节点|已映射起始题库|
|math.10.3|三重积分|math10.triple|已有对应节点|已映射起始题库|
|math.10.4|几何物理应用|math10.applications、math10.surface-gravity|已有对应节点|已映射起始题库|
|math.10.5|参数积分|math10.parameter|已有对应节点|已映射起始题库|
|math.11.1|弧长积分|math11.line1|已有对应节点|已映射起始题库|
|math.11.2|有向线积分与两类联系|math11.line2、math11.line-connections|已有对应节点|已映射起始题库|
|math.11.3|格林公式与势函数|math11.potential|已有对应节点|已映射起始题库|
|math.11.4|面积积分|math11.surface1|已有对应节点|已映射起始题库|
|math.11.5|定向面积积分与两类联系|math11.surface-orientation|已有对应节点|已映射起始题库|
|math.11.6|高斯与散度|math11.gauss|已有对应节点|已映射起始题库|
|math.11.7|斯托克斯与旋度|math11.stokes、math11.line-connections|已有对应节点|已映射起始题库|
|math.12.1|常数项级数及柯西准则|math12.series、math12.cauchy|已有对应节点|已映射起始题库|
|math.12.2|常数项判敛|math12.positive、math12.alternating|已有对应节点|已映射起始题库|
|math.12.3|幂级数域与运算|math12.power|已有对应节点|已映射起始题库|
|math.12.4|展开|math12.expansion|已有对应节点|已映射起始题库|
|math.12.5|近似方程级数解和欧拉公式|math12.power-applications|已有对应节点|已映射起始题库|
|math.12.6|一致收敛|math12.uniform|已有对应节点|已映射起始题库|
|math.12.7|傅里叶与半区间展开|math12.fourier、math12.half-range|已有对应节点|已映射起始题库|
|math.12.8|一般周期与复形式|math12.fourier、math12.half-range|已有对应节点|已映射起始题库|
|structures.1.1|目录1.1：结构计算模型、杆系分类与荷载分类|structures.overview|已有对应节点|已映射起始题库|
|structures.1.2|目录1.2：结构计算模型、杆系分类与荷载分类|structures.overview|已有对应节点|已映射起始题库|
|structures.1.3|目录1.3：结构计算模型、杆系分类与荷载分类|structures.overview|已有对应节点|已映射起始题库|
|structures.1.4|目录1.4：结构计算模型、杆系分类与荷载分类|structures.overview|已有对应节点|已映射起始题库|
|structures.2.1|目录2.1：几何组成、约束与计算简图|structures.geometry|已有对应节点|已映射起始题库|
|structures.2.2|目录2.2：几何组成规则、瞬变体系与自由度|structures.geometry-rules|已有对应节点|已映射起始题库|
|structures.2.3|目录2.3：几何组成规则、瞬变体系与自由度|structures.geometry-rules|已有对应节点|已映射起始题库|
|structures.2.4|目录2.4：几何组成、约束与计算简图；力法、基本体系与协调方程|structures.geometry、structures.force|已有对应节点|已映射起始题库|
|structures.3.1|目录3.1：静定梁、刚架与内力校核|structures.determinate|已有对应节点|已映射起始题库|
|structures.3.2|目录3.2：多跨静定梁、内铰与分层传力|structures.gerber|已有对应节点|已映射起始题库|
|structures.3.3|目录3.3：静定刚架的分段内力与节点平衡|structures.frame|已有对应节点|已映射起始题库|
|structures.3.4|目录3.4：桁架节点法、截面法与零杆|structures.truss-methods|已有对应节点|已映射起始题库|
|structures.3.5|目录3.5：三铰拱、水平推力与合理拱轴|structures.arch|已有对应节点|已映射起始题库|
|structures.3.6|目录3.6：组合结构与静定结构特性|structures.mixed|已有对应节点|已映射起始题库|
|structures.4.1|目录4.1：虚功、位移计算与互等定理|structures.virtual|已有对应节点|已映射起始题库|
|structures.4.2|目录4.2：虚功、位移计算与互等定理|structures.virtual|已有对应节点|已映射起始题库|
|structures.4.3|目录4.3：虚功、位移计算与互等定理；单位荷载法、图乘法与弯矩面积|structures.virtual、structures.diagram-product|已有对应节点|已映射起始题库|
|structures.4.4|目录4.4：单位荷载法、图乘法与弯矩面积|structures.diagram-product|已有对应节点|已映射起始题库|
|structures.4.5|目录4.5：温度、支座移动与非荷载作用|structures.loads|已有对应节点|已映射起始题库|
|structures.4.6|目录4.6：功、位移、反力与柔度互等|structures.reciprocity|已有对应节点|已映射起始题库|
|structures.5.1|目录5.1：影响线、移动荷载与包络|structures.influence|已有对应节点|已映射起始题库|
|structures.5.2|目录5.2：影响线、移动荷载与包络|structures.influence|已有对应节点|已映射起始题库|
|structures.5.3|目录5.3：间接荷载、桁架与结点荷载影响线|structures.indirect-influence|已有对应节点|已映射起始题库|
|structures.5.4|目录5.4：间接荷载、桁架与结点荷载影响线|structures.indirect-influence|已有对应节点|已映射起始题库|
|structures.5.5|目录5.5：机动法、最不利布载与绝对最大弯矩|structures.muller|已有对应节点|已映射起始题库|
|structures.5.6|目录5.6：机动法、最不利布载与绝对最大弯矩|structures.muller|已有对应节点|已映射起始题库|
|structures.5.7|目录5.7：机动法、最不利布载与绝对最大弯矩|structures.muller|已有对应节点|已映射起始题库|
|structures.6.1|目录6.1：力法、基本体系与协调方程|structures.force|已有对应节点|已映射起始题库|
|structures.6.2|目录6.2：力法、基本体系与协调方程|structures.force|已有对应节点|已映射起始题库|
|structures.6.3|目录6.3：力法协调、对称性与内力校核|structures.force-details|已有对应节点|已映射起始题库|
|structures.6.4|目录6.4：力法协调、对称性与内力校核|structures.force-details|已有对应节点|已映射起始题库|
|structures.6.5|目录6.5：温度、支座移动与非荷载作用；力法协调、对称性与内力校核|structures.loads、structures.force-details|已有对应节点|已映射起始题库|
|structures.6.6|目录6.6：力法协调、对称性与内力校核|structures.force-details|已有对应节点|已映射起始题库|
|structures.6.7|目录6.7：力法协调、对称性与内力校核|structures.force-details|已有对应节点|已映射起始题库|
|structures.6.8|目录6.8：力法协调、对称性与内力校核|structures.force-details|已有对应节点|已映射起始题库|
|structures.6.9|目录6.9：转角位移方程、固端弯矩与杆端刚度|structures.slope-deflection|已有对应节点|已映射起始题库|
|structures.7.1|目录7.1：位移法与转角位移方程|structures.displacement|已有对应节点|已映射起始题库|
|structures.7.2|目录7.2：位移法与转角位移方程；位移法基本未知量、侧移与对称简化|structures.displacement、structures.sway|已有对应节点|已映射起始题库|
|structures.7.3|目录7.3：位移法与转角位移方程；转角位移方程、固端弯矩与杆端刚度|structures.displacement、structures.slope-deflection|已有对应节点|已映射起始题库|
|structures.7.4|目录7.4：位移法与转角位移方程；位移法基本未知量、侧移与对称简化|structures.displacement、structures.sway|已有对应节点|已映射起始题库|
|structures.8.1|目录8.1：矩阵位移法与线性代数桥接|structures.matrix|已有对应节点|已映射起始题库|
|structures.8.2|目录8.2：单元刚度、坐标变换、组装与边界|structures.matrix-assembly|已有对应节点|已映射起始题库|
|structures.8.3|目录8.3：单元刚度、坐标变换、组装与边界|structures.matrix-assembly|已有对应节点|已映射起始题库|
|structures.8.4|目录8.4：单元刚度、坐标变换、组装与边界|structures.matrix-assembly|已有对应节点|已映射起始题库|
|structures.8.5|目录8.5：单元刚度、坐标变换、组装与边界|structures.matrix-assembly|已有对应节点|已映射起始题库|
|structures.8.6|目录8.6：单元刚度、坐标变换、组装与边界|structures.matrix-assembly|已有对应节点|已映射起始题库|
|structures.9.1|目录9.1：结构动力与单自由度响应|structures.dynamics|已有对应节点|已映射起始题库|
|structures.9.2|目录9.2：结构动力与单自由度响应|structures.dynamics|已有对应节点|已映射起始题库|
|structures.9.3|目录9.3：结构动力与单自由度响应|structures.dynamics|已有对应节点|已映射起始题库|
|structures.9.4|目录9.4：阻尼受迫响应、振型分解与参与系数|structures.forced-modal|已有对应节点|已映射起始题库|
|structures.9.5|目录9.5：多自由度自由振动、频率与振型|structures.modal|已有对应节点|已映射起始题库|
|structures.9.6|目录9.6：阻尼受迫响应、振型分解与参与系数|structures.forced-modal|已有对应节点|已映射起始题库|
|structures.9.7|目录9.7：阻尼受迫响应、振型分解与参与系数|structures.forced-modal|已有对应节点|已映射起始题库|
|structures.9.8|目录9.8：瑞利法、集中质量与频率近似|structures.rayleigh|已有对应节点|已映射起始题库|
|structures.10.1|目录10.1：极限荷载与塑性机构|structures.plastic|已有对应节点|已映射起始题库|
|structures.10.2|目录10.2：塑性铰、极限分析上下限定理|structures.plastic-bounds|已有对应节点|已映射起始题库|
|structures.10.3|目录10.3：梁、连续梁与刚架的塑性机构|structures.plastic-mechanisms|已有对应节点|已映射起始题库|
|structures.10.4|目录10.4：塑性铰、极限分析上下限定理|structures.plastic-bounds|已有对应节点|已映射起始题库|
|structures.10.5|目录10.5：梁、连续梁与刚架的塑性机构|structures.plastic-mechanisms|已有对应节点|已映射起始题库|
|structures.10.6|目录10.6：梁、连续梁与刚架的塑性机构|structures.plastic-mechanisms|已有对应节点|已映射起始题库|
|structures.11.1|目录11.1：结构稳定与临界荷载|structures.stability|已有对应节点|已映射起始题库|
|structures.11.2|目录11.2：结构稳定的静力法、能量法与弹性支承|structures.elastic-stability|已有对应节点|已映射起始题库|
|structures.11.3|目录11.3：结构稳定的静力法、能量法与弹性支承|structures.elastic-stability|已有对应节点|已映射起始题库|
|structures.11.4|目录11.4：结构稳定的静力法、能量法与弹性支承|structures.elastic-stability|已有对应节点|已映射起始题库|
|structures.11.5|目录11.5：变截面、剪切影响与组合压杆稳定|structures.advanced-buckling|已有对应节点|已映射起始题库|
|structures.11.6|目录11.6：变截面、剪切影响与组合压杆稳定|structures.advanced-buckling|已有对应节点|已映射起始题库|
|structures.11.7|目录11.7：变截面、剪切影响与组合压杆稳定|structures.advanced-buckling|已有对应节点|已映射起始题库|
|theory.unit.1|静力学公理、等效和各类平面力系|theory.force-systems、theory.model、theory.force、theory.balance|已有对应节点|已映射起始题库|
|theory.unit.2|空间力系、主矢主矩与空间平衡|theory.space|已有对应节点|已映射起始题库|
|theory.unit.3|物体系受力与约束、支反力|theory.model、theory.balance|已有对应节点|已映射起始题库|
|theory.unit.4|摩擦、摩擦角、自锁及滚动摩阻|theory.friction、theory.friction-angle|已有对应节点|已映射起始题库|
|theory.unit.5|重心与组合体|theory.centroid|已有对应节点|已映射起始题库|
|theory.unit.6|点的位置速度加速度、自然与极坐标|theory.point、theory.polar|已有对应节点|已映射起始题库|
|theory.unit.7|刚体平动和定轴转动|theory.rigid|已有对应节点|已映射起始题库|
|theory.unit.8|平面刚体基点法、瞬心及加速度|theory.rigid、theory.planar-acceleration|已有对应节点|已映射起始题库|
|theory.unit.9|点合成运动及科氏项|theory.relative、theory.coriolis|已有对应节点|已映射起始题库|
|theory.unit.10|惯性与非惯性系质点动力学|theory.newton、theory.relative-dynamics|已有对应节点|已映射起始题库|
|theory.unit.11|质点系动量、冲量与质心运动|theory.momentum、theory.newton|已有对应节点|已映射起始题库|
|theory.unit.12|动量矩、冲量矩及定轴动力学|theory.angular、theory.rigid-dynamics|已有对应节点|已映射起始题库|
|theory.unit.13|质量转动惯量与惯性积|theory.inertia|已有对应节点|已映射起始题库|
|theory.unit.14|功、势能、动能与柯尼希分解|theory.energy、theory.konig|已有对应节点|已映射起始题库|
|theory.unit.15|刚体平面动力学与普遍定理综合|theory.rigid-dynamics|已有对应节点|已映射起始题库|
|theory.unit.16|碰撞与恢复系数|theory.impact|已有对应节点|已映射起始题库|
|theory.unit.17|动静法和轴承动反力|theory.dalembert、theory.rotor-balance|已有对应节点|已映射起始题库|
|theory.unit.18|完整非完整约束、自由度与广义坐标|theory.constraints|已有对应节点|已映射起始题库|
|theory.unit.19|虚位移、理想约束与广义力|theory.virtual-work|已有对应节点|已映射起始题库|
|theory.unit.20|拉格朗日第二类方程及首次积分|theory.lagrange|已有对应节点|已映射起始题库|
|theory.unit.21|平衡位置稳定性和单自由度振动|theory.equilibrium-stability、theory.analytical、theory.damped-forced|已有对应节点|已映射起始题库|
|theory.unit.22|定点转动与陀螺入门扩展|theory.gyroscope|已有对应节点|已映射起始题库|
|theory.unit.23|变质量动力学扩展|theory.variable-mass|已有对应节点|已映射起始题库|
|materials.unit.1|变形体基本假设与三类设计目标|materials.basics、materials.section|已有对应节点|已映射起始题库|
|materials.unit.2|拉压内力、斜截面应力与弹性变形|materials.axial、materials.oblique|已有对应节点|已映射起始题库|
|materials.unit.3|材料性能、拉压试验及安全系数|materials.properties、materials.design|已有对应节点|已映射起始题库|
|materials.unit.4|剪切与挤压连接|materials.shear|已有对应节点|已映射起始题库|
|materials.unit.5|圆轴与薄壁圆筒扭转、功率及刚度|materials.torsion、materials.thin-wall、materials.shaft-power|已有对应节点|已映射起始题库|
|materials.unit.6|梁剪力弯矩与正剪应力分布|materials.moment、materials.bending、materials.shear-flow|已有对应节点|已映射起始题库|
|materials.unit.7|梁挠度、转角、积分法与刚度|materials.deflection、materials.boundary|已有对应节点|已映射起始题库|
|materials.unit.8|平面空间应力、应变与强度准则|materials.stress、materials.mohr、materials.generalized-hooke、materials.criteria、materials.brittle-criteria|已有对应节点|已映射起始题库|
|materials.unit.9|拉弯、弯扭、斜弯与偏心核心|materials.combined、materials.unsymmetric、materials.core|已有对应节点|已映射起始题库|
|materials.unit.10|欧拉、柔度区间和稳定设计|materials.stability、materials.stability-design|已有对应节点|已映射起始题库|
|materials.unit.11|拉伸扭转和弯曲实验与电测|materials.experiments、materials.rosette|已有对应节点|已映射起始题库|
|materials.unit.12|截面静矩、惯性积、主轴和平行轴|materials.geometry、materials.principal-inertia|已有对应节点|已映射起始题库|
|materials.unit.13|能量法、卡氏定理与单位载荷|materials.energy、materials.castigliano|已有对应节点|已映射起始题库|
|materials.unit.14|超静定、温度和装配协调|materials.indeterminate、materials.thermal|已有对应节点|已映射起始题库|
|materials.unit.15|落重、动载、疲劳循环与缺口|materials.fatigue、materials.impact、materials.fatigue-detail、materials.concentration|已有对应节点|已映射起始题库|
|materials.unit.16|非圆及开口翘曲、多室薄壁扩展|materials.noncircular、materials.thin-wall|已有对应节点|已映射起始题库|
|materials.unit.17|薄壁容器与强度应用扩展|materials.pressure-vessels|已有对应节点|已映射起始题库|
|engineering.steel.design|钢结构体系、极限状态与设计原则|steel.design|新增课程主题|已映射起始题库|
|engineering.steel.materials|钢材应力应变、韧性与疲劳性能|steel.materials|新增课程主题|已映射起始题库|
|engineering.steel.selection|钢材选用、厚度效应与质量保证|steel.selection|新增课程主题|已映射起始题库|
|engineering.steel.welding|焊缝形式、焊接缺陷与残余应力|steel.welding|新增课程主题|已映射起始题库|
|engineering.steel.butt-weld|对接焊缝的有效截面与验算|steel.butt-weld|新增课程主题|已映射起始题库|
|engineering.steel.fillet-weld|角焊缝有效焊喉与强度|steel.fillet-weld|新增课程主题|已映射起始题库|
|engineering.steel.weld-group|偏心焊缝群的力与力矩分配|steel.weld-group|新增课程主题|已映射起始题库|
|engineering.steel.bearing-bolts|普通螺栓剪切、承压与净截面|steel.bearing-bolts|新增课程主题|已映射起始题库|
|engineering.steel.friction-bolts|高强螺栓摩擦型、承压型与预拉力|steel.friction-bolts|新增课程主题|已映射起始题库|
|engineering.steel.bolt-group|受拉与偏心螺栓群、连接撬力|steel.bolt-group|新增课程主题|已映射起始题库|
|engineering.steel.tension|轴心受拉构件、剪滞与块体剪切|steel.tension|新增课程主题|已映射起始题库|
|engineering.steel.column|轴心受压构件、整体稳定与柱曲线|steel.column|新增课程主题|已映射起始题库|
|engineering.steel.builtup|格构柱、缀条缀板与分肢稳定|steel.builtup|新增课程主题|已映射起始题库|
|engineering.steel.local-buckling|板件局部屈曲、宽厚比与有效截面|steel.local-buckling|新增课程主题|已映射起始题库|
|engineering.steel.beam-strength|钢梁抗弯、抗剪、局压与正常使用|steel.beam-strength|新增课程主题|已映射起始题库|
|engineering.steel.beam-stability|钢梁侧扭屈曲与侧向支承|steel.beam-stability|新增课程主题|已映射起始题库|
|engineering.steel.plate-girder|组合钢梁腹板、加劲肋与拼接|steel.plate-girder|新增课程主题|已映射起始题库|
|engineering.steel.beam-column|拉弯压弯、二阶效应与双向受力|steel.beam-column|新增课程主题|已映射起始题库|
|engineering.steel.truss|钢屋架、腹杆弦杆与支撑体系|steel.truss|新增课程主题|已映射起始题库|
|engineering.steel.joints|梁柱节点、节点板与连接刚度|steel.joints|新增课程主题|已映射起始题库|
|engineering.steel.bases|柱脚、底板承压与锚栓|steel.bases|新增课程主题|已映射起始题库|
|engineering.steel.industrial|单层厂房、吊车梁与空间支撑|steel.industrial|新增课程主题|已映射起始题库|
|engineering.steel.portal|门式刚架、檩条与围护协同|steel.portal|新增课程主题|已映射起始题库|
|engineering.steel.fatigue|钢结构疲劳、细节分类与断裂|steel.fatigue|新增课程主题|已映射起始题库|
|engineering.steel.fire-corrosion|钢结构防火、防腐与全寿命维护|steel.fire-corrosion|新增课程主题|已映射起始题库|
|engineering.steel.fabrication|制造安装、误差、检验与临时稳定|steel.fabrication|新增课程主题|已映射起始题库|
|engineering.hydraulics.properties|流体密度、黏性、压缩性与连续介质|hydraulics.properties|新增课程主题|已映射起始题库|
|engineering.hydraulics.hydrostatics|静水压强、测压管与压强基准|hydraulics.hydrostatics|新增课程主题|已映射起始题库|
|engineering.hydraulics.surface-pressure|静水总压力、压力中心与浮力|hydraulics.surface-pressure|新增课程主题|已映射起始题库|
|engineering.hydraulics.kinematics|流线、迹线、恒定流与流场描述|hydraulics.kinematics|新增课程主题|已映射起始题库|
|engineering.hydraulics.continuity|连续方程、流量与控制体|hydraulics.continuity|新增课程主题|已映射起始题库|
|engineering.hydraulics.energy|伯努利、总流能量方程与水头线|hydraulics.energy|新增课程主题|已映射起始题库|
|engineering.hydraulics.momentum|动量方程、水流作用力与修正系数|hydraulics.momentum|新增课程主题|已映射起始题库|
|engineering.hydraulics.similarity|量纲分析、雷诺弗劳德与模型相似|hydraulics.similarity|新增课程主题|已映射起始题库|
|engineering.hydraulics.resistance|层紊流、沿程局部损失与边界层|hydraulics.resistance|新增课程主题|已映射起始题库|
|engineering.hydraulics.pipes|长短管、串并联管网与泵工况|hydraulics.pipes|新增课程主题|已映射起始题库|
|engineering.hydraulics.open-uniform|明渠均匀流、曼宁与最佳断面|hydraulics.open-uniform|新增课程主题|已映射起始题库|
|engineering.hydraulics.critical|断面比能、临界水深与水流分区|hydraulics.critical|新增课程主题|已映射起始题库|
|engineering.hydraulics.gradually-varied|渐变流水面线与边界控制|hydraulics.gradually-varied|新增课程主题|已映射起始题库|
|engineering.hydraulics.jump|水跃、共轭水深与消能|hydraulics.jump|新增课程主题|已映射起始题库|
|engineering.hydraulics.weir-orifice|孔口、管嘴、堰流与闸孔|hydraulics.weir-orifice|新增课程主题|已映射起始题库|
|engineering.hydraulics.seepage|达西渗流、渗透系数与地下水|hydraulics.seepage|新增课程主题|已映射起始题库|
|engineering.hydraulics.transient|非恒定流、水击与圣维南方程|hydraulics.transient|新增课程主题|已映射起始题库|
|engineering.hydraulics.measurement|水位、流速流量与水力实验|hydraulics.measurement|新增课程主题|已映射起始题库|
|engineering.river.sediment-properties|泥沙粒径、密度、级配与床沙孔隙|river.sediment-properties|新增课程主题|已映射起始题库|
|engineering.river.settling|泥沙沉速、颗粒雷诺数与絮凝|river.settling|新增课程主题|已映射起始题库|
|engineering.river.bed-shear|床面切应力、摩阻流速与Shields参数|river.bed-shear|新增课程主题|已映射起始题库|
|engineering.river.entrainment|泥沙起动、临界切应力与起动流速|river.entrainment|新增课程主题|已映射起始题库|
|engineering.river.bedload|推移质、单宽输沙率与经验适用域|river.bedload|新增课程主题|已映射起始题库|
|engineering.river.suspended|悬移质、含沙量、扩散与Rouse分布|river.suspended|新增课程主题|已映射起始题库|
|engineering.river.sediment-continuity|泥沙连续、Exner方程与冲淤|river.sediment-continuity|新增课程主题|已映射起始题库|
|engineering.river.bedforms|沙纹沙垄、平床与水沙阻力|river.bedforms|新增课程主题|已映射起始题库|
|engineering.river.channel-evolution|河床演变、弯道、分汊与河型|river.channel-evolution|新增课程主题|已映射起始题库|
|engineering.river.regulation|河道整治、护岸、丁坝与桥墩冲刷|river.regulation|新增课程主题|已映射起始题库|
|engineering.river.density-current|异重流、分层、掺混与水库泥沙|river.density-current|新增课程主题|已映射起始题库|
|engineering.river.estuary|河口径流潮汐、盐水入侵与最大浑浊带|river.estuary|新增课程主题|已映射起始题库|
|engineering.coastal.wave-linear|波高周期波长与线性波理论|coastal.wave-linear|新增课程主题|已映射起始题库|
|engineering.coastal.dispersion|色散、深浅水与相位群速度|coastal.dispersion|新增课程主题|已映射起始题库|
|engineering.coastal.energy|波能密度、能流与辐射应力|coastal.energy|新增课程主题|已映射起始题库|
|engineering.coastal.transform|浅化、折射、绕射与反射|coastal.transform|新增课程主题|已映射起始题库|
|engineering.coastal.breaking|破波、爬高、越浪与增水|coastal.breaking|新增课程主题|已映射起始题库|
|engineering.coastal.random-waves|随机波、波谱与有效波高|coastal.random-waves|新增课程主题|已映射起始题库|
|engineering.coastal.tides|天文潮、潮差、潮流与潮量|coastal.tides|新增课程主题|已映射起始题库|
|engineering.coastal.surge-currents|风暴潮、近岸流、离岸流与波流作用|coastal.surge-currents|新增课程主题|已映射起始题库|
|engineering.coastal.coast-sediment|波流输沙、岸滩剖面与海岸演变|coastal.coast-sediment|新增课程主题|已映射起始题库|
|engineering.coastal.wave-loads|波浪荷载、Morison与绕射适用性|coastal.wave-loads|新增课程主题|已映射起始题库|
|engineering.coastal.breakwater|斜坡式与直立式防波堤、稳定与消浪|coastal.breakwater|新增课程主题|已映射起始题库|
|engineering.coastal.revetment|海堤、护岸、反滤与堤脚防冲|coastal.revetment|新增课程主题|已映射起始题库|
|engineering.coastal.harbor-layout|港口选址、总平面与港池静稳|coastal.harbor-layout|新增课程主题|已映射起始题库|
|engineering.coastal.navigation|航道水深、富裕水深、宽度与通航|coastal.navigation|新增课程主题|已映射起始题库|
|engineering.coastal.gravity-quay|重力式码头、土压力与基底受力|coastal.gravity-quay|新增课程主题|已映射起始题库|
|engineering.coastal.piled-quay|高桩码头、桩台与空间传力|coastal.piled-quay|新增课程主题|已映射起始题库|
|engineering.coastal.sheet-pile|板桩码头、锚拉与嵌固深度|coastal.sheet-pile|新增课程主题|已映射起始题库|
|engineering.coastal.mooring|系泊、靠泊能量与护舷|coastal.mooring|新增课程主题|已映射起始题库|
|engineering.coastal.dredging|疏浚、回淤、工程量与维护|coastal.dredging|新增课程主题|已映射起始题库|
|engineering.coastal.physical-models|河口海岸物理模型与数值模型核验|coastal.physical-models|新增课程主题|已映射起始题库|
|engineering.coastal.environment|河海工程生态、监测与不确定性|coastal.environment|新增课程主题|已映射起始题库|
|specialist.math02.composition|专项补充：复合函数结构识别|math02.composition|已有对应节点|已映射起始题库|
|specialist.math06.revolution-area|专项补充：旋转曲面的面积|math06.revolution-area|已有对应节点|已映射起始题库|
|specialist.structures.truss|专项补充：桁架与拱|structures.truss|已有对应节点|已映射起始题库|
|specialist.structures.distribution|专项补充：力矩分配、分配系数与传递|structures.distribution|已有对应节点|已映射起始题库|
|specialist.structures.algebra-bridge|专项补充：矩阵方程桥接基础|structures.algebra-bridge|已有对应节点|已映射起始题库|
|specialist.structures.distribution-details|专项补充：力矩分配、传递系数与迭代收敛|structures.distribution-details|已有对应节点|已映射起始题库|

## 资源深度与验收

每节点包含两道诊断题、一道补习题、一条迁移与一条后续复测。开放推导、实验方案、复杂图形题由宿主按评分要点复核。所有teacher_reviewed与student_validated保留false，计算核对数量独立统计。

学校自选章节、教材附录、完整实验操作流程和研究生专题会因课程而异；本报告以已列目录和大纲为验收基准。需要某校逐周对齐时使用该校正式大纲扩展清单。
