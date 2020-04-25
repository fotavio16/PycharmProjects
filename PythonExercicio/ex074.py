from random import randint
minimo = 20
maximo = 1
print("Os números sorteados são : ", end='')
for i in range (10):
    num = randint(1,20)
    print(f'{num} ', end='')
    if minimo >= num:
        minimo = num
    if maximo <= num:
        maximo = num
print()
print(f'O menor valor é {minimo}.')
print(f'O maior valor é {maximo}.')
print()
tuplinha = tuple(randint(1,20) for _ in range(5))
minimo = min(tuplinha)
maximo = max(tuplinha)
print(f'Agora os números sorteados são : {tuplinha}')
print(f'O menor valor é {minimo}.')
print(f'O maior valor é {maximo}.')

