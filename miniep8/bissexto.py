''' 
Programa que recebe um ano e devolve True se o ano for bissexto
e False caso contrario...

Um ano e bissexto se for divisivel por 4, mas nao divisivel por 100, 
exceto se ele for tambem divisivel por 400

'''

# funcao que verifica se o ano e bissexto
def check (ano):

    # ano divisivel por 4 mas nao por 100
    if ano % 4 == 0 and ano % 100 != 0:
        return True

    return False
