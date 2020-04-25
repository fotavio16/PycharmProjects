from random import randint
from time import sleep

def sorteia():
    print("Sorteando 5 valores da lista: ", end='', flush=True)
    for i in range(5):
        sleep(1)
        temp = randint(1,9)
        lista.append(temp)
        print(f'{temp} ',end='', flush=True)
    print("PRONTO!")


def somaPar():
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    sleep(2)
    print(f'A soma de todos os valores pares de {lista} é {soma}.')



# Programa principal
lista = list()
sorteia()
somaPar()