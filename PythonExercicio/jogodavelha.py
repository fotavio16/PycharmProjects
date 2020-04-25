import random

# Pedir ao Jogador para escolher uma letra O ou X
def escolhaLetraJogador():
    l = ""
    while l != "O" and l != "X":
        l = str(input('Escolha a letra que prefere jogar (O ou X): ')).upper()
    if l == "O":
        letras = ['O', "X"]
    else:
        letras = ['X', "O"]
    return letras

# Sortear quem começa primeiro
def iniciaJogador():
    if random.randint(1,2) == 1:
        return True
    else:
        return False

def criaTabuleiro():
    t = []
    t.append('')
    for i in range(9):
        t.append(' ')
    return t

# Mostrar o tabuleiro
def mostraTabuleiro(posi):
    print("   |   |   ")
    print(' {} | {} | {} '.format(posi[7],posi[8],posi[9]))
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(' {} | {} | {} '.format(posi[4], posi[5], posi[6]))
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(' {} | {} | {} '.format(posi[1], posi[2], posi[3]))
    print("   |   |   ")

letras = escolhaLetraJogador()
vezJogador = iniciaJogador()
#tabuleiro = [' ','X',' ','O',' ','X','O',' ','O','X']
tabuleiro = criaTabuleiro()
mostraTabuleiro(tabuleiro)



# Vez do Jogador
# Mostrar o tabuleiro
# Receber o movimento do jogador

# Vez do Computador
# Definir movimento do computador
# 1) Executar movimento para vencer
# 2) Executar movimento para bloquaer o jogador de vencer na próxima jogada
# 3) Jogar nos cantos
# 4) Jogar no centro
# 5) Jogar nos lados

# Verifica se houve vencedor
# Verifica se houve empate

# Pergunta se o Jogador deseja jogar novamente
