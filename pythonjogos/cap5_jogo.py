'''
    Reino do Dragão
'''

import time
from random import randint

def abertura():
    print("Você está em uma terra cheia de dragões. ")
    print("Na sua frente, você vê duas cavernas.")
    print("Em uma caverna, o dragão é amigável e compartilhará")
    print("seu tesouro com você.")
    print("O outro dragão é ganancioso e faminto,")
    print("e o comerá à primeira vista.")
    print()

def escolheCaverna():

    print("Em qual caverna você entrará? (1 ou 2)")
    while True:
        escolha = int(input())
        if escolha == 1 or escolha == 2:
            return escolha
        else:
            print("Opção Inválida. Digite novamente.")

def verificaCaverna(e, cavDrag):

    print("Você se aproxima da caverna ...")
    time.sleep(1)
    print("É escuro e assustador ...")
    time.sleep(1)
    print("Um dragão grande pula na sua frente! "
          "Ele abre as mandíbulas e...")
    time.sleep(1)
    if e == cavDrag:
        print("Devora você em uma mordida!")
    else:
        print("Dá-lhe o seu tesouro!")


continua = 'S'
while continua == 'S':

    cavernaDragão = randint(1,2)

    abertura()

    escolha = escolheCaverna()

    verificaCaverna(escolha, cavernaDragão)

    print("Você quer jogar novamente? (Sim ou Não)")
    continua = str(input()).upper()[0]

print("Game Over")
