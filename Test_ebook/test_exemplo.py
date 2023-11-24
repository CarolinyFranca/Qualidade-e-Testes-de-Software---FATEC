import pytest

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def test_soma():
    resultado = soma(2, 3)
    assert resultado == 5  

@pytest.mark.skip
def test_soma_negativos():
    resultado = soma(-1, -2)
    assert resultado == -3 

def test_subtracao():
    resultado = subtracao(2, 3)
    assert resultado == 5  