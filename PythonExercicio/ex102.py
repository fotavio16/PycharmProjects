def fatorial(n, show=False):
    '''
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    '''
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        resposta = str(n)
        fat = n
        while n > 2:
            n = n - 1
            fat = fat * n
            resposta = resposta + ' x ' + str(n)
        if show:
            return resposta + ' x 1 = ' + str(fat)
        else:
            return fat


# Programa Principal
help(fatorial)
print(fatorial(5))
print(fatorial(8, True))
print(fatorial(0))
print(fatorial(1))
print(fatorial(2, True))
print(fatorial(3, True))