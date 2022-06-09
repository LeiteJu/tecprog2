import bissexto

def teste_1 ():
    assert bissexto.check(2020) == True

def teste_2 ():
    assert bissexto.check(1800) == False

def teste_3 ():
    assert bissexto.check(2000) == True