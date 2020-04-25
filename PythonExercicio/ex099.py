# Calcula o maior valor de uma lista
def maior(*lista):
    m = 0
    print("-=" *30)
    print("Analisando os valores passados...")
    for i in lista:
        print(f'{i} ',end='')
        if i > m:
            m = i
    print(f'Foram infornados {len(lista)} valores ao todo.')
    print(f'O maior valor informado foi {m}.')
    print("-=" * 30)


# Programa Principal
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()


