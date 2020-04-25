import random
print("BEM VINDO AO JOGO DO PARA OU IMPAR")
print("--"*15)
vit = 0
while True:
    palpite = int(input('Diga um valor entre zero e 9: '))
    jogador = ''
    while jogador not in ['P', 'I']:
        jogador = str(input('Quer Par ou Impar? ')).strip().upper()[0]
    jogada = random.choice(['PAR','IMPAR'])
    if (jogador == 'P' and jogada == 'PAR') or (jogador == 'I' and jogada == 'IMPAR'):
        print("Saiu {}. Você Venceu!! Vamos novamente.".format(jogada))
        vit += 1
    else:
        print("Saiu {}. Você Perdeu!!".format(jogada))
        break
print("Você teve {} vitórias consecutivas.".format(vit) if vit > 0 else "Infelizmente você não teve vitórias desta vez.")
