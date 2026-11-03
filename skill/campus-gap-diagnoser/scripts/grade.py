"""Bounded AST-to-SymPy conversion; never eval/sympify user input."""
import ast
import json
import re
import sys
import unicodedata
import sympy as s

FUNCTIONS = {k: getattr(s, k) for k in ('sin','cos','tan','exp','log','sqrt','Abs','asin','acos','atan')}
UNITS={'Pa':('pressure',s.Integer(1)),'kPa':('pressure',s.Integer(1000)),'MPa':('pressure',s.Integer(1000000)),'GPa':('pressure',s.Integer(1000000000)),
       'N':('force',s.Integer(1)),'kN':('force',s.Integer(1000)),
       'm':('length',s.Integer(1)),'cm':('length',s.Rational(1,100)),'mm':('length',s.Rational(1,1000)),
       'N*m':('moment',s.Integer(1)),'kN*m':('moment',s.Integer(1000)),'N*mm':('moment',s.Rational(1,1000))}
SYMBOLS = {k: s.Symbol(k, real=True) for k in ('x','y','z','t','u','v','a','b','c','L','E','I','P','q','F','N','A','r','h','n','m','k','G','J','omega','mu')}

def expression(text):
    text = unicodedata.normalize('NFKC', str(text)).strip().replace('^','**').replace('π','pi').replace('−','-')
    if len(text)>200: raise ValueError('表达式过长')
    tree=ast.parse(text, mode='eval')
    if len(list(ast.walk(tree)))>90: raise ValueError('表达式过于复杂')
    def visit(node, depth=0):
        if depth>12: raise ValueError('嵌套过深')
        v=lambda n:visit(n,depth+1)
        if isinstance(node,ast.Constant) and type(node.value) in (int,float):
            if abs(node.value)>1000000000000000: raise ValueError('数值超限')
            return s.Rational(str(node.value))
        if isinstance(node,ast.Name):
            if node.id in SYMBOLS:return SYMBOLS[node.id]
            if node.id=='pi':return s.pi
            raise ValueError('未知变量')
        if isinstance(node,ast.UnaryOp) and isinstance(node.op,(ast.USub,ast.UAdd)):
            return -v(node.operand) if isinstance(node.op,ast.USub) else v(node.operand)
        if isinstance(node,ast.BinOp):
            left,right=v(node.left),v(node.right)
            if isinstance(node.op,ast.Add):return left+right
            if isinstance(node.op,ast.Sub):return left-right
            if isinstance(node.op,ast.Mult):return left*right
            if isinstance(node.op,ast.Div):
                if right==0: raise ValueError('除零')
                return left/right
            if isinstance(node.op,ast.Pow):
                if not right.is_number or abs(right)>10:raise ValueError('指数须为绝对值不大于10的常数')
                return s.Pow(left,right)
        if isinstance(node,ast.Call) and isinstance(node.func,ast.Name) and node.func.id in FUNCTIONS and len(node.args)==1 and not node.keywords:
            return FUNCTIONS[node.func.id](v(node.args[0]))
        raise ValueError('请使用数字、变量和允许的数学函数')
    result=visit(tree.body)
    if result.has(s.zoo,s.nan,s.oo,-s.oo):raise ValueError('非有限表达式')
    return result

def normalize(text):return unicodedata.normalize('NFKC',str(text)).strip().casefold().replace(' ','')

def vector(text):
    text=unicodedata.normalize('NFKC',str(text)).strip()
    if len(text)>600:raise ValueError('向量表达式过长')
    tree=ast.parse(text,mode='eval').body
    if not isinstance(tree,(ast.Tuple,ast.List)) or not 1<=len(tree.elts)<=12:raise ValueError('请用逗号分隔各分量')
    return [expression(ast.unparse(node)) for node in tree.elts]

def grade(item, answer):
    kind=item.get('answer_type','text')
    if kind=='open': return {'verdict':'pending','reason':'请宿主依据评分要点审核论证、条件与解释。'}
    if kind in ('choice','text'):
        values=[item['answer']]+item.get('aliases',[])
        if normalize(answer) in [normalize(x) for x in values]:return {'verdict':'correct','reason':'与题库核对答案一致'}
        if kind=='choice' and normalize(answer) not in [normalize(x) for x in item.get('options',['是','否'])]:
            return {'verdict':'pending','reason':'请从题目选项中选择，或补充你的判断理由'}
        return {'verdict':'pending' if kind=='text' else 'incorrect','reason':'自由文本需依据要点复核' if kind=='text' else '选项不符'}
    if kind=='vector':
        try:
            parts=vector(answer); keys=vector(item['answer'])
            if len(parts)!=len(keys):return {'verdict':'pending','reason':'请用英文逗号分隔各分量'}
            if item.get('vector_equivalence')=='parallel':
                if all(a.is_zero is True for a in parts):return {'verdict':'incorrect','reason':'方向向量须为非零向量'}
                if not any(a.is_zero is False for a in parts):return {'verdict':'pending','reason':'请确认该方向向量为非零向量'}
                ok=all(s.simplify(parts[i]*keys[j]-parts[j]*keys[i])==0 for i in range(len(parts)) for j in range(i+1,len(parts)))
            else:ok=all(s.simplify(a-b)==0 for a,b in zip(parts,keys))
            return {'verdict':('pending' if item.get('requires_context') or item.get('requires_explanation') else 'correct') if ok else 'incorrect','reason':'向量满足题设的等价关系' if ok else '向量与题设结果不符，请核对方向和各分量'}
        except (ValueError,SyntaxError,TypeError):return {'verdict':'pending','reason':'表达式格式需确认'}
    try:
        supplied_unit=None;raw=str(answer).strip()
        if item.get('unit'):
            match=re.fullmatch(r'(.+?)\s*(kN\*m|N\*mm|N\*m|GPa|MPa|kPa|Pa|kN|N|mm|cm|m)',raw)
            if match:
                raw,supplied_unit=match.groups()
                if UNITS[supplied_unit][0]!=UNITS[item['unit']][0]:return {'verdict':'incorrect','reason':'单位量纲与所求量不一致，请核对题设单位'}
        actual,expected=expression(raw),expression(item['answer'])
        if supplied_unit:actual=actual*UNITS[supplied_unit][1]/UNITS[item['unit']][1]
        same=s.simplify(actual-expected)==0
        if same:
            if item.get('requires_explanation') or item.get('requires_context'):
                return {'verdict':'pending','numeric_match':True,'unit_converted':bool(supplied_unit),'reason':'结果吻合（已按题设单位换算），还须核对理由、模型或边界条件' if supplied_unit else '表达式吻合，还须核对理由、模型、单位或边界条件'}
            return {'verdict':'correct','reason':'表达式化简结果一致'}
        if not actual.free_symbols and not expected.free_symbols:
            tolerance=item.get('tolerance',1e-8)
            if abs(float(actual-expected))<=tolerance:
                return {'verdict':'pending' if item.get('requires_context') or item.get('requires_explanation') else 'correct','reason':'在题设容差内；模型与单位仍须按题目确认'}
        return {'verdict':'incorrect','reason':'结果与题设参考结果不同；若使用另一约定或方法，请申请复核'}
    except Exception:
        return {'verdict':'pending','reason':'请按评分要点复核表达式、条件与解题过程'}

if __name__=='__main__':
    try:
        payload=json.load(sys.stdin); print(json.dumps(grade(payload['item'],payload['answer']),ensure_ascii=False))
    except Exception: print(json.dumps({'verdict':'pending','reason':'输入格式需确认'},ensure_ascii=False))
