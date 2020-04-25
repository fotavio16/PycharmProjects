from random import randint
import time

print('-'*40)
print('JOGAR NA MEGA SENA'.center(40))
print('-'*40)
num = int(input('Quantos jogos você quer que eu sorteie? '))
mega = []
print(' SORTEANDO OS NÚMEROS '.center(40, '#'))
for i in range(num):
    jogo = []
    while len(jogo)<6:
        sorteio = randint(1,60)
        if sorteio not in jogo:
            jogo.append(sorteio)
    print(f'Jogo {i+1}: {sorted(jogo)}')
    time.sleep(1)
    mega.append(jogo[:])
print(' < BOA SORTE! > '.center(40, '#'))