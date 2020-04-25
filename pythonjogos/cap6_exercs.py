from random import randint, shuffle

def programa1():
    '''Faça um programa que leia uma lista de 10 números reais
    e mostre-os na ordem inversa.'''


def programa2():
    '''Faça um programa que simule um lançamento de dados.
    Lance o dado 100 vezes e armazene os resultados em uma lista.
    Depois, mostre quantas vezes cada valor foi conseguido.
    Dica: use uma lista de contadores (1-6) e uma função para
    gerar numeros aleatórios, simulando os lançamentos dos dados.'''

def programa3():
    '''Faça um programa que leia duas listas com 10 elementos
    cada. Gere uma terceira lista de 20 elementos, cujos
    valores deverão ser compostos pelos elementos intercalados
    das duas outras listas.'''

def programa4():
    '''Nome na vertical. Faça um programa que solicite o nome do
    usuário e imprima-o na vertical.'''

def programa5():
    '''Faça um programa que leia uma sequência de caracteres,
    mostre-a e diga se é um palíndromo19 ou não.'''


def programa6():
    '''Jogo da palavra embaralhada.
    Desenvolva um jogo em que o usuário tenha que adivinhar
    uma palavra que será mostrada com as letras embaralhadas.
    O programa terá uma lista de palavras e escolherá uma
    aleatoriamente. O jogador terá seis tentativas para adivinhar
    a palavra. Ao final a palavra deve ser mostrada na tela,
    informando se o usuário ganhou ou perdeu o jogo.'''

    print("P A L A V R A  E M B A R A L H A D A")

    palavra = sorteiaPalavra()
    mistura = embaralha(palavra)

    print(mistura)
    tentativas = 0
    maxTentativas = 6

    while tentativas < maxTentativas:
        print(f'Você tem {maxTentativas-tentativas}:')
        palpite = str(input("Qual o seu palpite? "))
        if palpite == palavra:
            print("Parabéns!!! Você acertou.")
            break
        else:
            tentativas += 1

    if tentativas >= maxTentativas:
        print("Você perdeu...")

    print(f'A palavra secreta é {palavra}.')



def sorteiaPalavra():
    PALAVRAS = '''formiga babuíno morcego molusco bandolim banqueta 
    barbante berimbau lagarto toupeira salamandra papagaio 
    rinoceronte tubarão preguiça cegonha faqueiro farolete ferrolho 
    turquia tartaruga doninha espadrilha espartilho espingarda 
    estandarte estilingue paraquedas pergaminho mamadeira mangueira 
    marionete microfone minissaia'''.split()

    indice = randint(0,len(PALAVRAS)-1)
    return PALAVRAS[indice]

def embaralha(palavra):
    p = list(palavra)
    shuffle(p)
    return "".join(p)



programa6()
