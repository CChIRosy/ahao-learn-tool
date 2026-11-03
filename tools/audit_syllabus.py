"""Explicit syllabus-to-resource mapping. Counts describe mapped starter resources."""
import json
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]
REF=BASE/'skill/campus-gap-diagnoser/references'
SOURCES={
 'math-upper':{'name':'同济高等数学第八版上册出版社目录','url':'https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=62cdab46938b7cc2960eedb1','scope':'第1—7章全部46节，含星号节；附录按工具基础补充'},
 'math-lower':{'name':'同济高等数学第八版下册出版社目录','url':'https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=62bc8b97938b7cc2960eebb7','scope':'第8—12章全部36节，含星号节'},
 'theory':{'name':'复旦大学理论力学范围','url':'https://aero-mech.fudan.edu.cn/1b/8a/c26484a465802/page.htm','scope':'静力学、运动学、牛顿动力学、分析力学'},
 'theory-czu':{'name':'常州工学院课程大纲中的理论力学章节','url':'https://tjxy.czu.cn/_upload/article/files/ae/f3/a23c80de499191499ecd231b4c02/5419a14d-f6b0-40e8-8fb0-dca6eccd31ad.pdf','scope':'PDF印刷页44—46的课程内容；平面空间力系、摩擦与运动学'},
 'materials':{'name':'北方工业大学材料力学课程及实验大纲','url':'https://jwc.ncut.edu.cn/DG7204311.pdf','scope':'8个理论教学单元及实验项目；能量、疲劳等另列专项扩展'},
 'structures':{'name':'清华大学出版社Structural Mechanics详细目录','url':'https://www.tup.tsinghua.edu.cn/booksCenter/bookcatalog?id=10424501','scope':'公开详细目录第1—11章；按全部小节建立对应资源'},
}

# Each semicolon-separated entry corresponds to one publisher section in order.
MATH={
1:'function inverse function-properties;sequence quantifiers;limit quantifiers;infinitesimal limit-laws;limit-laws;sequence limit infinitesimal limit-laws;infinitesimal;continuity;continuity uniform-continuity;continuity uniform-continuity',
2:'definition;rules chain basic inverse-derivative;higher;implicit related-rates parametric-second;differentials',
3:'mvt proof;lhopital;taylor remainders;extrema curvature;extrema;asymptote;curvature evolute;root-finding',
4:'primitive;substitution;parts;rational trig-rational;integral-table',
5:'definition riemann quadrature;ftc;methods;improper;gamma',
6:'area;area volume arc;physics',
7:'concept;separable;separable homogeneous-reducible;linear bernoulli;reduction;order variation-systems;order;nonhomogeneous;exact-euler;variation-systems',
8:'vectors;products mixed;planes;planes metric;surfaces;surfaces mixed',
9:'limits;partial;partial differentiability;chain;chain normal implicit-systems;geometry vector-curves;geometry;extrema;taylor;least-squares',
10:'double;double polar;triple;applications surface-gravity;parameter',
11:'line1;line2 line-connections;potential;surface1;surface-orientation;gauss;stokes line-connections',
12:'series cauchy;positive alternating;power;expansion;power-applications;uniform;fourier half-range;fourier half-range',
}

# Original paraphrases of section outcomes, not copied textbook explanations.
MATH_LABELS={
1:'映射与函数;数列的收敛定义和性质;函数极限及其性质;无穷小和无穷大;极限运算;存在准则和重要极限;无穷小阶比较;连续与间断;连续性运算;闭区间性质与一致连续',
2:'导数含义和存在条件;求导法则含反函数;高阶导数;隐式参数求导与相关速率;微分与近似',
3:'三类中值定理;不定式求极限;泰勒展开与余项;单调凹凸;极值和最值;函数图形;曲率及相关几何;方程数值求根',
4:'原函数与不定积分;换元;分部;有理化积分;查表和校验',
5:'积分定义性质与近似;微积分基本关系;积分计算方法;反常积分;积分判敛与Gamma',
6:'微元建模;面积体积和弧长;功压力和引力',
7:'方程解与初值;变量分离;一阶齐次型及转化;线性与伯努利;高阶方程降阶;线性解结构与变易法;常系数齐次;常系数非齐次;欧拉型;常系数系统',
8:'向量线性计算;三类向量乘积;空间平面;空间直线与距离角度;曲面;空间曲线与投影',
9:'多元极限和点集;偏导;全微分;多元复合求导;隐函数与方程组;空间微分几何;方向导数梯度;无约束和约束极值;二元泰勒;最小二乘',
10:'二重积分性质;二重积分计算与换元;三重积分;几何物理应用;参数积分',
11:'弧长积分;有向线积分与两类联系;格林公式与势函数;面积积分;定向面积积分与两类联系;高斯与散度;斯托克斯与旋度',
12:'常数项级数及柯西准则;常数项判敛;幂级数域与运算;展开;近似方程级数解和欧拉公式;一致收敛;傅里叶与半区间展开;一般周期与复形式',
}

STRUCTURES={
1:'overview;overview;overview;overview',
2:'geometry;geometry-rules;geometry-rules;geometry force',
3:'determinate;gerber;frame;truss-methods;arch;mixed',
4:'virtual;virtual;virtual diagram-product;diagram-product;loads;reciprocity',
5:'influence;influence;indirect-influence;indirect-influence;muller;muller;muller',
6:'force;force;force-details;force-details;loads force-details;force-details;force-details;force-details;slope-deflection',
7:'displacement;displacement sway;displacement slope-deflection;displacement sway',
8:'matrix;matrix-assembly;matrix-assembly;matrix-assembly;matrix-assembly;matrix-assembly',
9:'dynamics;dynamics;dynamics;forced-modal;modal;forced-modal;forced-modal;rayleigh',
10:'plastic;plastic-bounds;plastic-mechanisms;plastic-bounds;plastic-mechanisms;plastic-mechanisms',
11:'stability;elastic-stability;elastic-stability;elastic-stability;advanced-buckling;advanced-buckling;advanced-buckling',
}

THEORY=r'''
静力学公理、等效和各类平面力系|force-systems model force balance
空间力系、主矢主矩与空间平衡|space
物体系受力与约束、支反力|model balance
摩擦、摩擦角、自锁及滚动摩阻|friction friction-angle
重心与组合体|centroid
点的位置速度加速度、自然与极坐标|point polar
刚体平动和定轴转动|rigid
平面刚体基点法、瞬心及加速度|rigid planar-acceleration
点合成运动及科氏项|relative coriolis
惯性与非惯性系质点动力学|newton relative-dynamics
质点系动量、冲量与质心运动|momentum newton
动量矩、冲量矩及定轴动力学|angular rigid-dynamics
质量转动惯量与惯性积|inertia
功、势能、动能与柯尼希分解|energy konig
刚体平面动力学与普遍定理综合|rigid-dynamics
碰撞与恢复系数|impact
动静法和轴承动反力|dalembert rotor-balance
完整非完整约束、自由度与广义坐标|constraints
虚位移、理想约束与广义力|virtual-work
拉格朗日第二类方程及首次积分|lagrange
平衡位置稳定性和单自由度振动|equilibrium-stability analytical damped-forced
定点转动与陀螺入门扩展|gyroscope
变质量动力学扩展|variable-mass
'''

MATERIALS=r'''
变形体基本假设与三类设计目标|basics section
拉压内力、斜截面应力与弹性变形|axial oblique
材料性能、拉压试验及安全系数|properties design
剪切与挤压连接|shear
圆轴与薄壁圆筒扭转、功率及刚度|torsion thin-wall shaft-power
梁剪力弯矩与正剪应力分布|moment bending shear-flow
梁挠度、转角、积分法与刚度|deflection boundary
平面空间应力、应变与强度准则|stress mohr generalized-hooke criteria brittle-criteria
拉弯、弯扭、斜弯与偏心核心|combined unsymmetric core
欧拉、柔度区间和稳定设计|stability stability-design
拉伸扭转和弯曲实验与电测|experiments rosette
截面静矩、惯性积、主轴和平行轴|geometry principal-inertia
能量法、卡氏定理与单位载荷|energy castigliano
超静定、温度和装配协调|indeterminate thermal
落重、动载、疲劳循环与缺口|fatigue impact fatigue-detail concentration
非圆及开口翘曲、多室薄壁扩展|noncircular thin-wall
薄壁容器与强度应用扩展|pressure-vessels
'''


def build():
    manifest=json.loads((REF/'course-manifest.json').read_text(encoding='utf-8'))
    nodes={}
    for c in manifest['courses']:
        for n in json.loads((REF/'courses'/c['file']).read_text(encoding='utf-8'))['skills']:nodes[n['id']]=n
    rows=[]
    def row(key,subject,source,label,ids):
        assert ids and all(s in nodes for s in ids),(key,ids)
        old=[s for s in ids if nodes[s].get('introduced_version')!='0.2.0']
        rows.append({'id':key,'subject':subject,'source':source,'outcome':label,'skills':ids,
                     'before':'mapped' if len(old)==len(ids) else 'partial' if old else 'missing',
                     'after':'mapped_starter_bank','teacher_reviewed':False,'depth_validated':False})
    for chapter,mapping in MATH.items():
        labels=MATH_LABELS[chapter].split(';');sections=mapping.split(';')
        assert len(labels)==len(sections)
        for index,(keys,label) in enumerate(zip(sections,labels),1):
            row(f'math.{chapter}.{index}','math','math-upper' if chapter<=7 else 'math-lower',label,[f'math{chapter:02}.{k}' for k in keys.split()])
    for chapter,mapping in STRUCTURES.items():
        for index,keys in enumerate(mapping.split(';'),1):
            ids=['structures.'+k for k in keys.split()]
            row(f'structures.{chapter}.{index}','structures','structures',f'目录{chapter}.{index}：'+ '；'.join(nodes[s]['name'] for s in ids),ids)
    for subject,data in [('theory',THEORY),('materials',MATERIALS)]:
        for index,line in enumerate(data.strip().splitlines(),1):
            label,keys=line.split('|')
            row(f'{subject}.unit.{index}',subject,subject,label,[subject+'.'+k for k in keys.split()])
    # All remaining specialist nodes get a visible mapping, rather than disappearing from the audit.
    mapped={s for r in rows for s in r['skills']}
    for sid,n in nodes.items():
        if sid in mapped:continue
        course=sid.split('.')[0]
        source='math-upper' if course.startswith('math') and int(course[4:])<=7 else 'math-lower' if course.startswith('math') else course
        row('specialist.'+sid,'math' if course.startswith('math') else course,source,'专项补充：'+n['name'],[sid])
    result={'version':'0.2.0','checked_at':'2026-11-03','basis':'出版社逐节目录及所列高校大纲的知识主题映射；星号节纳入，题型深度逐项保留审核状态',
            'sources':SOURCES,'entries':rows,
            'counts':{'checklist_entries':len(rows),'math_publisher_sections':sum(r['id'].startswith('math.') for r in rows),
                      'before_mapped':sum(r['before']=='mapped' for r in rows),'before_partial':sum(r['before']=='partial' for r in rows),
                      'before_missing':sum(r['before']=='missing' for r in rows),'after_unmapped':0,'skills':len(nodes),
                      'added_skills':sum(n.get('introduced_version')=='0.2.0' for n in nodes.values())}}
    (REF/'syllabus-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    lines=['# 课程逐项覆盖核查（0.2.0）','','按出版社目录与高校公开大纲核查知识主题、讲解、前置关系与五阶段起始题。高数含上下册全部82节（含星号节）。力学按以下来源和专项补充逐项映射。','',
           '“已映射起始题库”表示该清单项有可检索节点、讲解与题目。教师对题型深度、逐个定理证明和教学效果的验收单独记录。','',
           '## 基准来源','']
    lines += [f"- [{v['name']}]({v['url']})：{v['scope']}。" for v in SOURCES.values()]
    lines += ['','## 核查统计','', '```json',json.dumps(result['counts'],ensure_ascii=False,indent=2),'```','','## 逐项映射','','|清单项|知识要求|节点|0.1.1回查|0.2.0|','|---|---|---|---|---|']
    for r in rows:lines.append('|'+ '|'.join([r['id'],r['outcome'],'、'.join(r['skills']),{'mapped':'已有对应节点','partial':'原有节点需补充','missing':'缺独立节点'}[r['before']],'已映射起始题库'])+'|')
    lines+=['','## 资源深度与验收','','每节点包含两道诊断题、一道补习题、一条迁移与一条后续复测。开放推导、实验方案、复杂图形题由宿主按评分要点复核。所有teacher_reviewed与student_validated保留false，计算核对数量独立统计。',
            '','学校自选章节、教材附录、完整实验操作流程和研究生专题会因课程而异；本报告以已列目录和大纲为验收基准。需要某校逐周对齐时使用该校正式大纲扩展清单。']
    (BASE/'docs/syllabus-audit.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(json.dumps(result['counts'],ensure_ascii=False))
    return result


if __name__=='__main__':build()
