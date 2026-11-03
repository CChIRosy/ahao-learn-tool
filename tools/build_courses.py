"""Original authored assessment seeds. Build compact, locally routed course bundles."""
import json
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]
REF=BASE/'skill/campus-gap-diagnoser/references'
PACKS=[]

def pack(code,name,source):
    item={'id':code,'name':name,'source':source,'skills':[]};PACKS.append(item);return item

def add(p,key,name,teach,rows,prereq=(),aliases=(),extended=False):
    """Each line is a separately authored prompt~answer; trailing ! means explanation."""
    sid=p['id']+'.'+key;items=[]
    rows=[r.strip() for r in rows.strip().splitlines() if r.strip()]
    assert len(rows)==5,(sid,len(rows))
    for i,row in enumerate(rows):
        prompt,answer=row.rsplit('~',1)
        explanation=answer.endswith('!');answer=answer.rstrip('!')
        kind='choice' if answer in ('是','否') else 'open' if answer.startswith('@') else 'vector' if ',' in answer else 'expression'
        if kind=='open':answer=answer[1:]
        purpose=['diagnostic','diagnostic','learning','transfer','retention'][i]
        items.append({'id':sid+f'.{i+1}','skill_id':sid,'purpose':purpose,'family_id':sid+f'.family-{i+1}',
            'prompt':prompt,'answer':answer,'answer_type':kind,'requires_explanation':explanation,
            'requires_context': not p['id'].startswith('math') and kind in ('expression','vector'),
            'domain':'按题干给出的实数域、时间范围与假设；条件不足先确认',
            'context':{'assumptions': '按题面给定的模型、坐标和边界条件作答' if not p['id'].startswith('math') else '按题设定义域作答',
                       'units':'数值按题干所列单位填写' if not p['id'].startswith('math') else '按题干'},
            'hints':['先指出本题的对象、已知量与适用条件。',teach],
            'rubric':[answer,teach,'核对方法与适用条件；合理的其他表述由宿主复核'],
            'common_errors':['忽略条件或约定','机械套用公式，未解释当前步骤'],
            'difficulty':1 if i==2 else 2,'verification':{'key_parsed':False,'independent_oracle':False,'teacher_reviewed':False,'student_validated':False}})
        if kind=='choice':items[-1]['options']=['是','否']
    p['skills'].append({'id':sid,'name':name,'aliases':list(aliases)+[key],
        'prerequisites':list(prereq),'tier':'extension' if extended else 'core','teaching':teach,
        'misconceptions':['需通过两条独立证据区分偶发失误与规则理解问题'],
        'items':items,'quality':{'scope_mapped':True,'bank_available':True,'teacher_reviewed':False,'student_validated':False}})

UPPER='https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=62cdab46938b7cc2960eedb1'
LOWER='https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=62bc8b97938b7cc2960eebb7'

p=pack('math01','函数与极限',UPPER)
add(p,'function','映射、函数与定义域','先明确自变量集合；复合时同时满足内外层定义域。', '''sqrt(x-1)的实数定义域是x>=1吗？~是
log(x)能在x=0取实值吗？~否
f(x)=x²，求f(-2)。~4
f(x)=1/(x-2)，x=2属于定义域吗？~否
g(x)=sqrt(1-x²)，x=2时有实数函数值吗？~否''',aliases=['定义域','复合函数','映射'])
add(p,'sequence','数列极限与夹逼','数列收敛要求单一有限极限；单调有界可保证收敛，不能由有界单独推出。','''求n趋于无穷时1/n的极限。~0
数列(-1)^n有极限吗？~否
单调递增且有上界的实数列必收敛吗？~是
求n趋于无穷时(3n+1)/(n+2)的极限。~3
若|a_n|<=1/n，a_n的极限为多少？~0''')
add(p,'limit','函数极限与左右极限','双侧极限存在需要左右极限相等；极限与函数在该点是否定义不同。','''x趋于0时sin(x)/x极限为多少？~1
x趋于0时|x|/x的双侧极限存在吗？~否
x趋于1时(x²-1)/(x-1)的极限。~2
x趋于0时(1-cos(x))/x²的极限。~1/2
x趋于2时(x²-4)/(x-2)的极限。~4''',aliases=['两个重要极限','左右极限'])
add(p,'infinitesimal','无穷小比较与等价替换','等价替换常用于乘除结构；加减中须保留足够阶数，不能分别替换后消去主项。','''x趋于0时sin(x)与x等价吗？~是
x趋于0时1-cos(x)与x等价吗？~否
x趋于0时log(1+x)/x的极限。~1
x趋于0时(exp(x)-1-x)/x²的极限。~1/2
x趋于0时tan(x)/x的极限。~1''')
add(p,'continuity','连续、间断与闭区间性质','点处连续要求极限等于函数值；闭区间连续函数有界并取得最大最小值，零点判断需异号等条件。','''f(x)=sin(x)/x在0处补为多少才连续？~1
左右极限有限但不等属于可去间断吗？~否
闭区间上连续函数必取到最大值吗？~是
连续函数f在[a,b]满足f(a)f(b)<0，区间内必有零点吗？~是
在开区间连续就一定取到最大值吗？~否''',prereq=['math01.limit'])

p=pack('math02','导数与微分',UPPER)
add(p,'definition','导数定义与可导性','导数是差商极限；可导必连续，连续未必可导。','''用定义求x²在x=2处导数。~4
|x|在x=0可导吗？~否
可导函数在该点必连续吗？~是
f(x)=x³，求f在x=1处导数。~3
函数连续是否足以保证可导？~否''',prereq=['math01.limit','math01.continuity'])
add(p,'basic','基本函数求导','核对函数和求导变量；三角、指数、对数的基本公式分别适用。','''sin(u)对u求导。~cos(u)
x²对x求导。~2*x
log(x)在x>0上求导。~1/x
exp(x)对x求导。~exp(x)
cos(x)对x求导。~-sin(x)''',prereq=['math02.definition'],aliases=['基本求导'])
add(p,'composition','复合函数结构识别','先把表达式拆成外层函数和内层变量；识别结构不等同于已会链式法则。','''sin(x²)的内层可取x²吗？~是
exp(3x)的外层是exp(u)吗？~是
解释log(1+x²)的内层和外层。~@内层u=1+x²，外层log(u)
(2x+1)^4的内层导数是多少？~2
sin(cos(x))的最外层是sin(u)吗？~是''',prereq=['math01.function'],aliases=['内外层','复合结构'])
add(p,'chain','链式法则','外层对内层求导，再乘内层对自变量的导数；这是变化率的复合。','''求sin(x²)对x的导数。~2*x*cos(x**2)
求cos(3x)对x的导数。~-3*sin(3*x)
求exp(2x)对x的导数。~2*exp(2*x)
求(3x-1)^4的导数，并说明内层因子来源。~12*(3*x-1)**3!
求log(1+x²)的导数。~2*x/(1+x**2)''',prereq=['math02.basic','math02.composition'],aliases=['复合求导','链式求导'])
add(p,'rules','和差、乘积与商求导','乘积导数有两项；商法则的分母为原分母平方，先确认分母不为零。','''求x*sin(x)的导数。~sin(x)+x*cos(x)
求x/(1+x)的导数，x不等于-1。~1/(1+x)**2
求x²+sin(x)的导数。~2*x+cos(x)
求x²*exp(x)的导数。~exp(x)*(2*x+x**2)
求sin(x)/x的导数，x不为0。~(x*cos(x)-sin(x))/x**2''',prereq=['math02.basic'])
add(p,'higher','高阶导数','高阶导数是重复求导；注意链式系数每次都会出现。','''求x³的二阶导数。~6*x
求sin(x)的二阶导数。~-sin(x)
求exp(2x)的二阶导数。~4*exp(2*x)
求x^4的三阶导数。~24*x
求cos(2x)的二阶导数。~-4*cos(2*x)''',prereq=['math02.chain','math02.rules'])
add(p,'implicit','隐函数、参数方程与微分','隐式求导时y是x的函数；参数方程dy/dx=(dy/dt)/(dx/dt)，分母须非零；微分为导数乘增量。','''x²+y²=1，在y不为0处求dy/dx。~-x/y
x=t²,y=t³且t不为0，求dy/dx。~3*t/2
y=x²，在x=2、dx=0.01时求dy。~0.04
x+y+y²=0，在1+2y不为0处求y'。~-1/(1+2*y)
x=exp(t),y=t，求dy/dx。~exp(-t)''',prereq=['math02.chain','math02.rules'])

p=pack('math03','微分中值定理与导数应用',UPPER)
add(p,'mvt','罗尔、拉格朗日与柯西中值定理','先检查闭区间连续、开区间可导及端点条件；结论是存在性，不要求唯一。','''f(x)=x²在[0,2]应用拉格朗日定理，求c。~1
罗尔定理需要两端函数值相等吗？~是
f(x)=x²-1在[-1,1]的罗尔点c。~0
|x|在[-1,1]满足罗尔定理全部条件吗？~否
柯西中值定理可在未核验分母导数条件时任意写导数比吗？~否''',prereq=['math02.definition'])
add(p,'lhopital','洛必达法则与不定式','先确认0/0或无穷比无穷型及可导等条件；不能直接用于任意比值。','''x趋于0时(exp(x)-1)/x极限。~1
x趋于0时sin(x)/x可满足洛必达的适用条件吗？~是
x趋于正无穷时log(x)/x极限。~0
x趋于0时(log(1+x)-x)/x²极限。~-1/2
分子分母极限分别为1和2时，能直接用导数比替代原比吗？~否''',prereq=['math02.basic','math01.limit'])
add(p,'taylor','泰勒公式与余项','展开中心、阶数和余项必须匹配；近似计算与精确等式要区分。','''exp(x)在0处二阶泰勒多项式。~1+x+x**2/2
sin(x)在0处三阶泰勒多项式。~x-x**3/6
cos(x)在0处二阶多项式。~1-x**2/2
log(1+x)在0处二阶多项式。~x-x**2/2
泰勒截断多项式对所有x都等于原函数吗？~否''',prereq=['math02.higher'])
add(p,'extrema','单调、极值、最值与图形','驻点只是候选；最值还要比较区间端点，图形分析需结合定义域和渐近行为。','''x³-3x的正驻点是多少？~1
导数等于0的点必为极值点吗？~否
x²在[-1,2]的最大值。~4
x³在0处有极值吗？~否
1/x在正半轴上单调递减吗？~是''',prereq=['math02.rules'])
add(p,'curvature','凹凸、拐点与曲率','凹凸用二阶导数符号；拐点要求凹凸改变。曲率分母为(1+y′²)^(3/2)。','''y=x³的拐点横坐标。~0
y=x^4在0处二阶导为0，所以0一定是拐点吗？~否
y=x²在0处的曲率。~2
y=2x的曲率。~0
y''=0是否足以判定拐点？~否''',prereq=['math02.higher'],aliases=['曲率','凹凸','拐点'])

p=pack('math04','不定积分',UPPER)
add(p,'primitive','原函数与基本积分','不定积分是一族原函数；未写任意常数的标准化答案只用于题目明确要求时。','''忽略积分常数，求∫2x dx。~x**2
忽略常数，求∫cos(x) dx。~sin(x)
两个原函数在同一区间上必相差常数吗？~是
忽略常数，在x>0上求∫1/x dx。~log(x)
忽略常数，求∫exp(x) dx。~exp(x)''',prereq=['math02.basic'])
add(p,'substitution','第一、第二换元积分','换元要同步改变微分；定积分还需同步改变上下限。','''忽略常数，求∫2x*cos(x²) dx。~sin(x**2)
忽略常数，求∫exp(3x) dx。~exp(3*x)/3
忽略常数，求∫2x/(1+x²) dx。~log(1+x**2)
忽略常数，求∫cos(2x) dx。~sin(2*x)/2
用x=sin(t)代换时dx等于dt吗？~否''',prereq=['math02.chain','math04.primitive'])
add(p,'parts','分部积分','用∫u dv=uv-∫v du；选择u时考虑求导后能否简化。','''忽略常数，求∫x*exp(x) dx。~(x-1)*exp(x)
忽略常数，x>0时求∫log(x) dx。~x*log(x)-x
忽略常数，求∫x*cos(x) dx。~x*sin(x)+cos(x)
忽略常数，求∫x*sin(x) dx。~-x*cos(x)+sin(x)
分部积分公式中uv后应减去∫v du吗？~是''',prereq=['math02.rules','math04.primitive'])
add(p,'rational','有理函数与三角代换','先比较分子分母次数，再分解因式；部分分式及三角代换需保留定义域。','''忽略常数，求∫1/(1+x²) dx。~atan(x)
1/(x(x+1))等于1/x-1/(x+1)吗？~是
忽略常数，在x>0求∫(1+1/x) dx。~x+log(x)
忽略常数，在x>1求∫1/(x²-1) dx。~log((x-1)/(x+1))/2
对sqrt(1-x²)采用x=sin(t)时需要限制t区间以确定根号符号吗？~是''',prereq=['math04.substitution'])

p=pack('math05','定积分',UPPER)
add(p,'definition','定积分概念、性质与估值','定积分是带符号累积量；反向上下限变号，积分存在与原函数存在不同。','''∫从0到1的2x dx。~1
∫从1到0的2x dx。~-1
奇函数在[-a,a]可积，其积分为多少？~0
∫从0到2的3 dx。~6
定积分一定非负吗？~否''',prereq=['math01.continuity'])
add(p,'ftc','微积分基本定理与变上限函数','连续被积函数下，变上限积分求导用基本定理再用链式法则。','''对∫从0到x的sin(t)dt求导。~sin(x)
对∫从0到x²的exp(t)dt求导。~2*x*exp(x**2)
∫从0到1的3x² dx。~1
对∫从x到1的t²dt求导。~-x**2
∫从0到pi的sin(x)dx。~2''',prereq=['math02.chain','math04.primitive'])
add(p,'methods','定积分换元与分部','换元后上下限应换成新变量值；分部积分包含边界项。','''∫从0到1的2x*exp(x²)dx。~exp(1)-1
∫从0到1的x*exp(x)dx。~1
∫从0到pi/2的sin(x)dx。~1
∫从0到1的x*cos(x²)dx。~sin(1)/2
换元后仍保留原变量上下限而直接代新原函数正确吗？~否''',prereq=['math04.substitution','math04.parts','math05.ftc'])
add(p,'improper','无穷区间与无界函数反常积分','将奇点或无穷端点定义为极限；多个奇点逐个检查，主值不等同于通常收敛。','''∫从1到无穷的1/x² dx。~1
∫从1到无穷的1/x dx收敛吗？~否
∫从0到1的1/sqrt(x) dx。~2
∫从0到1的1/x² dx收敛吗？~否
∫从1到无穷的exp(-x)dx。~exp(-1)''',prereq=['math01.limit','math05.ftc'])

p=pack('math06','定积分应用',UPPER)
add(p,'area','微元法与平面面积','面积以非负微元累积；先确定交点、上下曲线及是否分段。','''x与x²在[0,1]围成的面积。~1/6
对有交叉的上下曲线，可以不分段直接积分差并当面积吗？~否
y=2与x轴在x=0到3间的面积。~6
y=x²在[0,2]与x轴围成面积。~8/3
面积微元(上-下)dx要求先判断上、下关系吗？~是''',prereq=['math05.definition','math05.ftc'])
add(p,'volume','旋转体与截面体积','圆盘法用pi乘半径平方；壳层法与圆盘法对应不同微元。','''y=x在[0,1]绕x轴旋转体积。~pi/3
半径2、高3的圆柱体积。~12*pi
圆盘法的微元是pi*y² dx吗？~是
y=sqrt(x)在[0,2]绕x轴旋转体积。~2*pi
截面面积恒为5、长度为4的棱柱体积。~20''',prereq=['math06.area'])
add(p,'arc','平面曲线弧长','弧长微元sqrt(1+y′²)dx；参数曲线使用速度向量模。','''y=x在[0,1]的弧长。~sqrt(2)
参数x=3t,y=4t，t从0到2的弧长。~10
单位圆上从0到pi的半圆弧长。~pi
y=2x在[0,3]的弧长。~3*sqrt(5)
弧长能用∫y dx直接计算吗？~否''',prereq=['math02.rules','math05.ftc'])
add(p,'physics','功、压力与引力积分','先给出物理模型和单位，再写微元；静水压力按深度变化，引力按距离与方向分解。','''F(x)=2x牛，沿x从0到3米，功的数值（焦）。~9
弹簧k=10牛/米，从0拉到0.2米，功（焦）。~1/5
竖直矩形闸门上缘在水面，宽b高h，流体密度r，重力加速度取a，合力表达式。~r*a*b*h**2/2
质点引力的方向分解在对称体积分中可以省略而不说明吗？~否
沿位移方向恒力5牛作用2米的功（焦）。~10''',prereq=['math06.area','math05.ftc'])

p=pack('math07','微分方程',UPPER)
add(p,'concept','阶、通解、特解与初值','阶由最高阶导数决定；把候选解代回方程与初值分别核验。','''y''+y=0是二阶方程吗？~是
y=exp(x)满足y'=y吗？~是
y'=2x且y(0)=1，求y。~x**2+1
y=0是y'=y的解吗？~是
满足微分方程的函数一定满足指定初值吗？~否''',prereq=['math02.higher'])
add(p,'separable','可分离变量与齐次一阶方程','分离变量前注意被除函数为零的特殊解；齐次型y′=F(y/x)可令y=ux。','''y'=2y且y(0)=1，求y。~exp(2*x)
y'=y²，分离时除以y²会遗漏零解吗？~是
y'=x且y(0)=0，求y。~x**2/2
y'=1+y/x是否为y'=F(y/x)型？~是
y'=3x²且y(0)=2，求y。~x**3+2''',prereq=['math04.primitive','math07.concept'])
add(p,'linear','一阶线性方程','识别y′+P(x)y=Q(x)；积分因子由P决定，并保留初值求常数。','''y'+y=0且y(0)=2，求y。~2*exp(-x)
y'+2y=4且y(0)=0，求y。~2-2*exp(-2*x)
y'+y=1的常数特解。~1
y'-y=0且y(0)=3，求y。~3*exp(x)
一阶线性非齐次通解可写为齐次通解加一个特解吗？~是''',prereq=['math07.separable'])
add(p,'order','降阶与高阶常系数线性方程','缺y或缺x的方程可尝试降阶；常系数线性方程先解特征方程，再处理重根和共振。','''y''=0且y(0)=1,y'(0)=2，求y。~1+2*x
y''-3y'+2y=0的特征根是1和2吗？~是
y''+y=0且y(0)=0,y'(0)=1，求y。~sin(x)
y''-2y'+y=0在重根1时，第二个独立解可取x*exp(x)吗？~是
y''+y=sin(x)可直接试A*sin(x)+B*cos(x)作特解吗？~否''',prereq=['math07.linear','math02.higher'])
add(p,'exact-euler','全微分方程与欧拉方程','恰当性检查偏导相等和区域条件；欧拉方程在x>0上可试x^m。','''2x dx+2y dy=0的势函数可取x²+y²吗？~是
M=y,N=x，M_y=N_x吗？~是
x²y''+xy'-y=0试y=x^m，特征根是1和-1吗？~是
y dx+2x dy=0直接视为全微分d(xy)=0正确吗？~否
x²y''+xy'=0在x>0时log(x)是解吗？~是''',prereq=['math07.order'],extended=True)

p=pack('math08','向量代数与空间解析几何',LOWER)
add(p,'vectors','向量线性运算、模与投影','分量运算与几何方向对应；投影需要指定方向及是否为有向标量。','''向量(3,4,0)的模。~5
(1,2,3)+(2,0,-1)的分量，用逗号分隔。~3,2,2
(3,4,0)在x轴正向的标量投影。~3
单位向量的模等于多少？~1
与(0,0,2)同向的单位向量。~0,0,1''')
add(p,'products','数量积、向量积与混合积','点积输出标量，叉积输出向量并遵守右手规则；混合积检验共面。','''(1,2,0)点乘(3,0,0)。~3
(1,0,0)叉乘(0,1,0)。~0,0,1
非零向量垂直时点积为多少？~0
交换叉积顺序，结果变号吗？~是
标准基i,j,k的混合积。~1''',prereq=['math08.vectors'])
add(p,'planes','平面方程、直线及夹角','平面法向量与直线方向向量不同；夹角公式明确取锐角或有向角。','''平面2x+3y-z=1的一个法向量。~2,3,-1
直线(x,y,z)=(1,0,0)+t(2,1,0)的方向向量。~2,1,0
点(0,0,3)到平面z=0的距离。~3
直线方向与平面法向量平行，直线和平面垂直吗？~是
两个平面法向量平行则两平面一定重合吗？~否''',prereq=['math08.products'])
add(p,'surfaces','曲面、二次曲面与空间曲线投影','方程先判定几何对象；投影需消元并保留实数可行范围。','''x²+y²+z²=4的球半径。~2
x²+y²=1在三维中是圆柱面吗？~是
曲线x²+y²=1,z=x投影到xy面为单位圆吗？~是
z=x²+y²是双曲抛物面吗？~否
曲线x=cos(t),y=sin(t),z=t位于单位圆柱面上吗？~是''',prereq=['math08.planes'])

p=pack('math09','多元函数微分法及其应用',LOWER)
add(p,'limits','多元极限、连续与平面点集','不同路径结果不等可否定极限，有限条路径相等不能证明存在。','''xy/(x²+y²)在原点有极限吗？~否
x²+y²在原点的极限。~0
只沿x轴、y轴趋近得到相同值就能证明二元极限存在吗？~否
闭圆盘x²+y²<=1包含边界吗？~是
f(x,y)=x+y在整个平面连续吗？~是''',prereq=['math01.limit'])
add(p,'partial','偏导、高阶偏导与全微分','求偏导时其他自变量固定；偏导存在不保证全微分存在，连续偏导是充分条件之一。','''f=x²y，求f_x。~2*x*y
f=sin(xy)，求f_y。~x*cos(x*y)
f=x²+y²在(1,2)处全微分为2dx+4dy吗？~是
f=x²y³，求f_xy。~6*x*y**2
某点两个一阶偏导存在足以保证该点可微吗？~否''',prereq=['math02.chain','math09.limits'])
add(p,'chain','多元链式法则与隐函数','列清依赖路径，沿每条路径相乘再求和；隐函数求导检查相应偏导非零。','''z=x²+y²,x=t,y=2t，求dz/dt。~10*t
z=xy,x=t²,y=t，求dz/dt。~3*t**2
F=x²+y²+z²-1=0,z不为0，求z_x。~-x/z
z=f(x,y),x=x(t),y=y(t)，总导数只包含f_x*x'吗？~否
z=exp(x+y),x=t,y=-t，求dz/dt。~0''',prereq=['math09.partial','math02.chain'])
add(p,'geometry','切平面、法线、方向导数与梯度','方向导数使用单位方向；梯度给出局部最快增加方向，切平面以偏导构造。','''f=x²+y²在(1,2)处梯度。~2,4
f=x+y在方向(1,1)上的单位方向导数。~sqrt(2)
曲面z=x²+y²在(1,0)处切平面z=2x-1吗？~是
f=x²+y²在(0,0)梯度为零，任意单位方向导数均为零吗？~是
求f=3x+4y在单位方向上的最大方向导数。~5''',prereq=['math09.partial','math08.vectors'])
add(p,'extrema','多元极值与拉格朗日乘数','驻点需分类；条件极值核对约束及异常点，紧集最值还考虑边界。','''x²+y²在平面上的最小值。~0
f=x²-y²在原点为局部极小吗？~否
x+y=2约束下x²+y²的最小值。~2
单位圆上x+y的最大值。~sqrt(2)
拉格朗日方程解出候选点后可不检查约束直接接受吗？~否''',prereq=['math09.partial'])

p=pack('math10','重积分',LOWER)
add(p,'double','二重积分、区域与换序','先描述积分区域，再决定内外积分变量；换序通常需要重写边界。','''单位正方形上∬(x+y)dA。~1
区域0<=y<=x<=1的面积。~1/2
区域0<=y<=x<=1换序后可写0<=y<=1,y<=x<=1吗？~是
矩形0<=x<=2,0<=y<=3上∬xy dA。~9
任意非常数区域都能不改上下限交换积分次序吗？~否''',prereq=['math05.ftc'])
add(p,'polar','极坐标与一般变量代换','面积元要乘雅可比绝对值；极坐标为r dr dtheta，范围需覆盖且避免重复。','''半径2圆盘上∬1 dA。~4*pi
极坐标面积元可以只写dr dtheta吗？~否
单位圆盘上∬(x²+y²)dA。~pi/2
x=2u,y=3v的面积雅可比绝对值。~6
单位圆盘第一象限的面积。~pi/4''',prereq=['math10.double','math08.surfaces'])
add(p,'triple','三重积分与柱球坐标','体积元取雅可比；球坐标约定极角和方位角，不能漏r²sin(phi)。','''单位立方体上∭1 dV。~1
半径1球体的体积。~4*pi/3
柱坐标体积元含径向因子r吗？~是
半径2、高3的圆柱上∭1 dV。~12*pi
球坐标体积元通常含r²*sin(phi)吗？~是''',prereq=['math10.polar'])
add(p,'applications','重积分质量、质心与转动惯量','密度乘面积元或体积元得到质量；质心用一阶矩除总质量，惯量用到轴距离平方。','''单位正方形均匀薄片的质心坐标。~1/2,1/2
面积3、面密度2的薄片质量。~6
矩形[0,2]×[0,1]单位面密度，对y轴转动惯量。~8/3
关于y轴对称、质量非零的薄片，其质心x坐标为0吗？~是
质量2的质点距轴3，其转动惯量数值。~18''',prereq=['math10.double'])

p=pack('math11','曲线积分与曲面积分',LOWER)
add(p,'line1','第一类曲线积分','ds是非负弧长元；第一类积分通常与行进方向无关。','''沿单位圆一周∫1 ds。~2*pi
反转曲线方向会使∫1 ds变号吗？~否
线段(0,0)到(3,4)上∫2 ds。~10
单位上半圆∫1 ds。~pi
将ds直接写成dx而不考虑曲线斜率正确吗？~否''',prereq=['math06.arc'])
add(p,'line2','第二类曲线积分与格林公式','Pdx+Qdy依赖方向；格林公式需区域、边界正向和光滑性等条件。','''逆时针单位圆上∮(-y dx+x dy)。~2*pi
反向曲线积分∫Pdx+Qdy一般变号吗？~是
单位正方形正向边界∮x dy。~1
沿x轴从0到2的∫x dx。~2
格林公式可不检查内部奇点直接用于穿孔场吗？~否''',prereq=['math10.double','math11.line1'])
add(p,'potential','路径无关与全微分','势函数存在可推出路径无关；仅旋度为零还需核对区域拓扑等条件。','''场(2x,2y)的势函数可取x²+y²吗？~是
∫(2x dx+2y dy)从(0,0)到(1,2)。~5
单连通区域内光滑场满足Q_x=P_y，可推出路径无关吗？~是
穿孔平面上旋度零必然存在全局单值势函数吗？~否
梯度场沿闭合曲线的积分。~0''',prereq=['math09.partial','math11.line2'])
add(p,'surface1','第一类曲面积分','曲面面积元按参数叉积模或图形sqrt(1+z_x²+z_y²)计算。','''单位球面上∬1 dS。~4*pi
平面z=0上单位正方形∬2 dS。~2
曲面翻转法向会改变第一类曲面积分吗？~否
z=x+y在单位正方形上方的面积。~sqrt(3)
半径2球面的面积。~16*pi''',prereq=['math09.partial','math08.products'])
add(p,'gauss','第二类曲面积分、高斯公式与散度','通量需选法向；高斯公式连接闭曲面外向通量与体积分，检查场内部光滑性。','''F=(x,y,z)的散度。~3
F=(x,y,z)穿出单位球的通量。~4*pi
翻转法向时通量变号吗？~是
F=(0,0,2)穿过z=0单位正方形向上的通量。~2
高斯公式可忽略曲面内部场的奇点吗？~否''',prereq=['math10.triple','math11.surface1'])
add(p,'stokes','斯托克斯公式、环流与旋度','边界方向与法向按右手规则一致；旋度为向量，散度为标量。','''F=(-y,x,0)的旋度。~0,0,2
单位圆从z正向看逆时针，对应法向向上吗？~是
F=(-y,x,0)沿单位圆正向环流。~2*pi
将曲面法向反转却保持边界方向不变仍可直接用斯托克斯吗？~否
光滑梯度场的旋度为零向量吗？~是''',prereq=['math11.line2','math11.gauss'])

p=pack('math12','无穷级数',LOWER)
add(p,'series','级数概念与必要条件','级数收敛看部分和极限；通项趋零必要但不充分，有限项改动不改变敛散性。','''级数∑从n=1到无穷的1/2^n的和。~1
∑1/n的通项趋于0，所以级数收敛吗？~否
收敛级数的通项必趋于0吗？~是
改变有限项会改变级数敛散性吗？~否
公比绝对值小于1的几何级数必收敛吗？~是''',prereq=['math01.sequence'])
add(p,'positive','正项级数比较、比值与根值审敛','先确认正项；比值或根值极限为1时不能据此判敛散。','''∑1/n²收敛吗？~是
比值判别极限为1就一定发散吗？~否
∑从n=1到无穷的1/3^n的和。~1/2
∑1/sqrt(n)收敛吗？~否
正项级数通项最终小于某收敛正项级数通项，可判收敛吗？~是''',prereq=['math12.series','math05.improper'])
add(p,'alternating','交错、绝对与条件收敛','莱布尼茨条件含单调趋零；绝对收敛推出收敛，反向不成立。','''∑(-1)^(n-1)/n收敛吗？~是
该交错调和级数绝对收敛吗？~否
绝对收敛必收敛吗？~是
∑(-1)^n/n²绝对收敛吗？~是
把条件收敛级数任意重排仍必保和吗？~否''',prereq=['math12.positive'])
add(p,'power','幂级数收敛半径、端点与运算','先求半径，再分别检查端点；逐项求导积分需处于合法范围。','''∑从n=0到无穷的x^n的收敛半径。~1
∑x^n在x=1收敛吗？~否
∑x^n/n!的收敛半径有限吗？~否
∑从n=1到无穷的x^n/n在x=-1收敛吗？~是
只算收敛半径就能确定两个端点都收敛吗？~否''',prereq=['math12.positive'])
add(p,'expansion','幂级数展开及应用','函数等于其泰勒级数需要余项趋零或相应条件；写清展开中心及收敛范围。','''1/(1-x)在0展开的x³系数。~1
exp(x)在0展开的x³系数。~1/6
sin(x)在0展开的x³系数。~-1/6
log(1+x)在0展开的x²系数。~-1/2
函数有任意阶导数就必等于其泰勒级数吗？~否''',prereq=['math03.taylor','math12.power'])
add(p,'fourier','傅里叶级数、正交与一般周期','明确周期、区间及系数约定；跳跃点在满足条件时收敛到左右极限平均。','''2pi周期函数f(x)=1，按a0/2约定，其a0是多少？~2
在[-pi,pi]上奇函数的余弦系数均为0吗？~是
∫从-pi到pi的sin(x)cos(x)dx。~0
周期为2L时基频角频率。~pi/L
跳跃点左右极限为1和3，满足狄利克雷条件时傅里叶和为多少？~2''',prereq=['math05.methods','math12.series'])
add(p,'uniform','函数项级数一致收敛','一致收敛需要对整个集合统一控制余项；逐点收敛不足以交换极限或积分。','''x^n在[0,1)逐点趋0，是否在该区间一致收敛？~否
x^n在[0,1/2]上一致趋0吗？~是
若|f_n(x)|<=1/2^n，∑f_n可由M判别法判一致收敛吗？~是
连续函数列一致收敛的极限函数连续吗？~是
仅逐点收敛是否足以保证极限函数连续？~否''',prereq=['math12.power'],extended=True)

def finish():
    manifest={'version':'0.3.0','scope_basis':'同济高数、三门力学、钢结构与用户确认的河流海岸工程范围；来源与主题映射见references/syllabus-audit.json', 'courses':[],'skills':[]}
    for p in PACKS:
        filename=p['id']+'.json'
        manifest['courses'].append({'id':p['id'],'name':p['name'],'file':filename,'source':p['source'],'skill_count':len(p['skills']),'question_count':sum(len(s['items']) for s in p['skills'])})
        for s in p['skills']:
            units={'materials.axial.1':'MPa','materials.axial.3':'mm','materials.shear.1':'MPa','materials.torsion.2':'Pa','materials.bending.2':'MPa',
                   'theory.force.1':'N*m','theory.force.3':'N*m','theory.balance.3':'N*m','theory.balance.4':'N','materials.moment.1':'N*m','materials.moment.4':'N*m'}
            for item in s['items']:
                if item['id'] in units:item['unit']=units[item['id']]
                if item['id'] in ('math08.planes.1','math08.planes.2','math09.vector-curves.1','math09.vector-curves.3'):item['vector_equivalence']='parallel'
            manifest['skills'].append({k:s[k] for k in ('id','name','aliases','prerequisites','tier')}|{'file':filename,'course':p['id']})
        dest=REF/'courses'/filename;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(json.dumps(p,ensure_ascii=False,indent=2),encoding='utf-8')
    (REF/'course-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    return manifest

if __name__=='__main__':
    import mechanics_seeds
    mechanics_seeds.populate(pack,add)
    import supplemental_seeds
    supplemental_seeds.populate(PACKS,add)
    import coverage_seeds
    coverage_seeds.populate(PACKS,add)
    import engineering_seeds
    engineering_seeds.populate(pack,add)
    print(json.dumps({'modules':len(PACKS),'skills':sum(len(p['skills']) for p in PACKS),'questions':sum(len(s['items']) for p in PACKS for s in p['skills'])}))
    finish()
    import audit_syllabus
    audit_syllabus.build()
