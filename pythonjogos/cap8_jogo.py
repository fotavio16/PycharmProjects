'''
    Bagels
'''

from random import randint, shuffle

def abertura():
    print("Estou pensando em um número de 3 dígitos. Tente adivinhar o que é.")
    print("Aqui estão algumas dicas:")
    print("Quando digo: Isso significa:")
    print("Pico:    Um dígito está correto, mas na posição errada.")
    print("Fermi:   Um dígito está correto e na posição correta.")
    print("Bagels:  Nenhum dígito está correto.")
    print("Eu pensei em um número. Você tem 10 palpites para obtê-lo.")

def sorteia():
    numeros = '0123456789'
    numeros = list(numeros)
    for i in range(10):
        shuffle(numeros)
    return ''.join(numeros)[:3]


def jogarDeNovo():
    if str(input("Quer jogar novamente? (S/N)")).upper()[0] == 'S':
        return True
    else:
        return False

def mostrarDicas(chave, palpite):
    dica = ''
    for i in range(len(palpite)):
        if palpite[i] in chave:
            if palpite[i] == chave[i]:
                dica = dica + 'Fermi '
            else:
                dica = dica + 'Pico '
    if len(dica) == 0:
        dica = 'Bagels'
    print(dica)


maxTentativas = 10
tentativas = 1

while True:
    if tentativas == 1:
        abertura()
        chave = sorteia()

    #print(chave)

    palpite = str(input(f'Tentativa {tentativas}: '))
    if palpite == chave:
        print("Você Venceu!! Parabéns!!!")
        if jogarDeNovo():
            tentativas = 1
        else:
            print("GAME OVER")
            break
    else:
        mostrarDicas(chave, palpite)

    tentativas += 1
    if tentativas > 10:
        print("Você gastou todas as tentativas. Você perdeu.")
        print(f'A palavra secreta é {chave}.')
        if jogarDeNovo():
            tentativas = 1
        else:
            print("GAME OVER")
            break



