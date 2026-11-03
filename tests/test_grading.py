import pytest
from grade import expression,grade

@pytest.mark.parametrize('value',["__import__('os').system('whoami')",'x.__class__','[x for x in range(4)]','x[0]','2**999','1/0','sqrt(1).__class__','open(1)','x**x','1e999','sin(x, y)'])
def test_rejects_non_math_or_unbounded_input(value):
    with pytest.raises(Exception):expression(value)

def test_equivalent_forms_and_missing_chain_factor():
    item={'answer':'2*x*cos(x**2)','answer_type':'expression'}
    assert grade(item,'cos(x^2)*x*2')['verdict']=='correct'
    assert grade(item,'cos(x**2)')['verdict']=='incorrect'

def test_context_and_reason_required_even_when_number_matches():
    assert grade({'answer':'3','answer_type':'expression','requires_context':True},'3')['verdict']=='pending'
    assert grade({'answer':'1/3','answer_type':'expression','requires_explanation':True},'0.333333333')['verdict']=='pending'
    assert grade({'answer':'1,2','answer_type':'vector','requires_context':True},'1,2')['verdict']=='pending'

def test_proof_is_not_graded_by_string_similarity():
    assert grade({'answer_type':'open','answer':'完整证明'},'完整证明')['verdict']=='pending'

def test_invalid_or_unsupported_answer_does_not_become_wrong():
    assert grade({'answer':'1','answer_type':'expression'},'看不懂')['verdict']=='pending'
    assert grade({'answer':'1,2','answer_type':'vector'},'1')['verdict']=='pending'

def test_engineering_unit_conversion_and_dimension_rejection():
    item={'answer':'10','answer_type':'expression','unit':'MPa','requires_context':True}
    result=grade(item,'0.01 GPa')
    assert result['verdict']=='pending' and result['numeric_match'] and result['unit_converted']
    assert grade(item,'10 N')['verdict']=='incorrect'
    assert grade(item,'10000000 Pa')['numeric_match']

def test_moment_conversion_keeps_model_review():
    item={'answer':'6','answer_type':'expression','unit':'N*m','requires_context':True}
    assert grade(item,'6000 N*mm')['numeric_match']
