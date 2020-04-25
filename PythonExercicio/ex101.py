from time import gmtime

def voto(ano):
    anoAtual = gmtime().tm_year
    idade = anoAtual - ano
    #print(f'Com {idade} anos: ', end='')
    if idade < 16:
        return "NEGADO", idade
    elif idade < 18:
        return "OPCIONAL", idade
    elif idade < 70:
        return "OBRIGATÓRIO", idade
    else:
        return "OPCIONAL", idade


# Progama Principal
print("-" *30)
anoNasc = int(input("Em que ano você nasceu? "))
situação, idade = voto(anoNasc)
print(f'Com {idade} anos: VOTO {situação}.')
