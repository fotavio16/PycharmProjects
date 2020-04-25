'''
    Advinhe o Número
'''

from random import randint

name = str(input("Olá! Qual o seu nome? "))

print(f'Então, {name}. Eu estou pensando em um número entre 1 e 20.')

numero = randint(1,20)
tentativas = 0
acertou = False

while not acertou:
    palpite = int(input("Tente um palpite: "))
    tentativas += 1
    if palpite == numero:
        acertou = True
    elif palpite > numero:
        print("Seu palpite está alto.")
    else:
        print("Seu palpite está baixo.")

print(f'Bom trabalho, {name}! Você acertou meu número em {tentativas} tentativas.')
