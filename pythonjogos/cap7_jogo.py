from random import randint, choice

def mostraTela(tela):
    print('   |   |')
    print(f' {tela[7]} | {tela[8]} | {tela[9]}')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(f' {tela[4]} | {tela[5]} | {tela[6]}')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(f' {tela[1]} | {tela[2]} | {tela[3]}')
    print('   |   |')

def escolheLetra():
    letra = ""
    while not (letra == 'X' or letra == 'O'):
        letra = str(input("Qual a letra vai usar ('X' ou 'O')? ")).upper()[0]

    if letra == 'X':
        return ['X','O']
    else:
        return ['O','X',]

def definePrimeiro():
    if randint(0,1) == 1:
        return False
    else:
        return True

def recebeMovmto(tela):
    while True:
        #posicao = str(input("Qual sua próxima posição (1-9)? "))
        posicao = int(input("Qual sua próxima posição (1-9)? "))
        if str(posicao) in '123456789':
            if tela[posicao] == ' ':
                return posicao


def venceu(tela, l):
    return ((tela[7] == l and tela[8] == l and tela[9] == l) or
            (tela[4] == l and tela[5] == l and tela[6] == l) or
            (tela[1] == l and tela[2] == l and tela[3] == l) or
            (tela[7] == l and tela[4] == l and tela[1] == l) or
            (tela[8] == l and tela[5] == l and tela[2] == l) or
            (tela[9] == l and tela[6] == l and tela[3] == l) or
            (tela[7] == l and tela[5] == l and tela[3] == l) or
            (tela[9] == l and tela[5] == l and tela[1] == l))

def deuVelha(tela):
    for i in range(1, 10):
        if tela[i] == ' ':
            return False
    return True

def copiaTela(tela):
    copia = []
    for t in tela:
        copia.append(t)
    return copia

def escolhePosicaoAleatoria(tela, lista):
    posicoes = []
    for p in lista:
        if tela[p] == ' ':
            posicoes.append(p)

    if len(posicoes) == 0:
        return None
    else:
        return choice(posicoes)

def escolheMovimento(tela, computador, jogador):
    # Possível vencer neste lance?
    for i in range(1, 10):
        copia = copiaTela(tela)
        if copia[i] == ' ':
            copia[i] = computador
            if venceu(copia, computador):
                return i

    # Bloqueia posição de vitória do jogador
    for i in range(1, 10):
        copia = copiaTela(tela)
        if copia[i] == ' ':
            copia[i] = jogador
            if venceu(copia, jogador):
                return i

    # Tenta ocupar um dos cantos
    posicao = escolhePosicaoAleatoria(tela, [1, 3, 7, 9])
    if posicao != None:
        return posicao

    # Tenta ocupar o centro
    if tela[5] == ' ':
        return 5

    # Ocupa os lados
    return escolhePosicaoAleatoria(tela, [2, 4, 6, 8])


print("J O G O  D A  V E L H A")

while True:
    # Inicia a variáveis do jogo
    tela = [' ']*10
    jogador, computador = escolheLetra()
    vezJogador = definePrimeiro()
    if vezJogador:
        print("O humano joga primeiro.")
    else:
        print("O computador joga primeiro.")
    jogando = True

    while jogando:
        if vezJogador:
            mostraTela(tela)
            posicao = recebeMovmto(tela)
            tela[posicao] = jogador

            if venceu(tela, jogador):
                mostraTela(tela)
                print("Parabéns!!! Você venceu!")
                jogando = False
            else:
                if deuVelha(tela):
                    mostraTela(tela)
                    print("Deu Velha...")
                    break
                else:
                    vezJogador = False
        else:
            posicao = escolheMovimento(tela, computador, jogador)
            tela[posicao] = computador

            if venceu(tela, computador):
                mostraTela(tela)
                print("Você perdeu. O computador bateu você.")
                jogando = False
            else:
                if deuVelha(tela):
                    mostraTela(tela)
                    print("Deu Velha...")
                    break
                else:
                    vezJogador = True


    if not (input("Quer continuar a jogar (Sim ou Não)? ").lower().startswith('s')):
        break

