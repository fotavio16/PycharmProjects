import random

tentativas = 0
sorteio = random.randint(0, 10)
guess = 11
while guess != sorteio:
    tentativas += 1
    guess = int(input("Tente advinhar o número que eu sorteei..."))

print("O numero sorteado foi {}. Você acerou em {} tentativas.".format(sorteio, tentativas))
