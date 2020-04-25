def dobro(num, formatado=True):
    if formatado:
        return moeda(num *2)
    else:
        return num * 2

def metade(num, formatado=True):
    if formatado:
        return moeda(num / 2)
    else:
        return num / 2

def aumentar(num, percentual, formatado=True):
    if formatado:
        return moeda(num * (100 + percentual) / 100)
    else:
        return num * (100 + percentual) / 100

def diminuir(num, percentual, formatado=True):
    if formatado:
        return moeda(num * (100 - percentual) / 100)
    else:
        return num * (100 - percentual) / 100

def moeda(num):
    a = '{:,.2f}'.format(float(num))
    b = a.replace(',', 'v')
    c = b.replace('.', ',')
    return 'R$' + c.replace('v', '.')

def resumo(num, aumento, redução):
    print('-' * 30)
    print('        RESUMO DO VALOR')
    print('-' * 30)
    print(f'Preço analisado:    {moeda(num)}')
    print(f'Dobro do preço:     {dobro(num)}')
    print(f'Metade do preço:    {metade(num)}')
    print(f'{aumento}% de aumento:     {aumentar(num, aumento)}')
    print(f'{redução}% de redução:     {diminuir(num, redução)}')
    print('-' * 30)
