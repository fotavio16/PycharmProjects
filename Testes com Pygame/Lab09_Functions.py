# Functions
from random import randint

def min3(a, b, c):
    '''
    Avalia os valores e retorna o melhor
    :param a: 1º parâmetro
    :param b: 2º parâmetro
    :param c: 3º parâmetro
    :return: O menor dos 3 parâmetros
    '''
    min = a
    if b < min:
        min = b
    if c < min:
        min = c
    return min

def box(l,c):
    '''
    Imprime retângulos com asteriscos
    :param l: Número de linhas
    :param c: Número de colinas
    :return: Sem retorno
    '''
    for i in range(l):
        for j in range(c):
            print('*',end='')
        print()


def find(lista, key):
    for i in range(len(lista)):
        if lista[i] == key:
            print(f'Found {key} at position {i+1}.')


def create_list(num):
    lista = []
    for i in range(num):
        lista.append(randint(1,6))
    return lista


def count_list(lista, num):
    cont = 0
    for i in lista:
        if i == num:
            cont += 1
    return cont


def average_list(lista):
    media = 0
    for i in range(len(lista)):
        media += lista[i]
    return media / len(lista)



print(min3(4, 7, 5))
print(min3(4, 5, 5))
print(min3(4, 4, 4))
print(min3(-2, -6, -100))
print(min3("Z", "B", "A"))

print()

box(7,5)  # Print a box 7 high, 5 across
print()   # Blank line
box(3,2)  # Print a box 3 high, 2 across
print()   # Blank line
box(3,10) # Print a box 3 high, 10 across

print()

my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]

find(my_list, 12)
find(my_list, 91)
find(my_list, 80)

print()

my_list = create_list(5)
print(my_list)

print()

count = count_list([1,2,3,3,3,4,2,1],3)
print(count)

print()

avg = average_list([1,2,3])
print(avg)

print()

listaMil = create_list(10000)
for n in range(1,7):
    contador = count_list(listaMil, n)
    print(f'O número {n} aparece {contador} vezes na lista de 10.000 númeors aleatórios.')
avg = average_list(listaMil)
print(f'E a média dos números da lista é {avg}.')

