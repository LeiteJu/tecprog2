import bissexto

def teste_1 ():
    assert bissexto.check(2020) == True

def teste_2 ():
    assert bissexto.check(1800) == False

def teste_3 ():
    assert bissexto.check(2000) == True

def teste_4 ():
    assert bissexto.check(1732) == True

def teste_5 ():
    assert bissexto.check(1742) == False
