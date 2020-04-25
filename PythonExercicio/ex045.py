import random
print("Vamos jogar Jokempô!!!")
print("Escolha 1 para Pedra, 2 para Tesoura ou 3 para Papel:")
escolha = int(input("Qual a sua escolha? "))
opcoes = ['Pedra', 'Tesoura', 'Papel']
maquina = random.choice(opcoes)
if escolha >= 1 and escolha <=3:
    jogador = opcoes[escolha-1]
    print("Você escolheu {}.".format(jogador))
    print("O computador escolheu {}.".format(maquina))
    if jogador == maquina:
        print("Houve empate!")
    elif (jogador == 'Pedra' and maquina == 'Tesoura') or (jogador == 'Tesoura' and maquina == 'Papel') or (jogador == 'Papel' and maquina == 'Pedra'):
        print("Você VENCEU!!!")
    else:
        print("Você PERDEU!!!")
else:
    print("Você digitou uma opção incorreta. Tente novamente.")

