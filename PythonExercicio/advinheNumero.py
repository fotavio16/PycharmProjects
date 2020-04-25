from random import randint
print("Hello! Meu nome é Robin.")
nome = str(input('Qual o seu nome? '))
print("Ok, {}, vamos jogar!!!".format(nome))
c = randint(1,2)
if c == 1:
    print("Eu estou pensando em um número entre 1 e 20. Você consegue advinhar?")
    robin = randint(1,20)
    humano = 0
    while humano != robin:
        humano = int(input('Qual o seu palpite? '))
        if humano < robin:
            print("É mais...")
        elif humano > robin:
            print("É menos...")
    print("Parabéns! Você acertou.")
else:
    print("Pense em um número entre 1 e 20, que eu vou tentar advinhar.")
    input('Tecle OK ou ENTER quando estiver pronto: ')
    min = 1
    max = 20
    acertei = False
    while not acertei:
        palpite = randint(min,max)
        resposta = str(input("Eu acho que é {}. Acertei? Mais ou Menos? ".format(palpite)))
        if resposta == 'Mais':
            min = palpite + 1
        elif resposta == 'Menos':
            max = palpite - 1
        elif resposta == 'Sim':
            acertei = True
        else:
            print("Opção inválida. Vamos de novo.")
    print("Yeah. Nada mal para Robin.")

