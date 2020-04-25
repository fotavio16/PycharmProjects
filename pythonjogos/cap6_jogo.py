'''
    JOGO DA FORCA
'''

from random import randint

def sorteiaPalavra():
    PALAVRAS = '''formiga babuíno texugo morcego urso camelo gato molusco 
    cobra puma coiote corvo veado cão burro pato águia furão raposa sapo 
    cabra ganso falcão leão lagarto lhama toupeira macaco alce rato mula 
    salamandra lontra coruja panda papagaio pombo pitão coelho ram rato corvo 
    rinoceronte salmão tubarão ovelha gambá preguiça cobra aranha cegonha 
    cisne tigre sapo truta turquia tartaruga doninha baleia lobo wombat zebra'''.split()

    indice = randint(0,len(PALAVRAS)-1)
    return PALAVRAS[indice]

def mostraTela(FORCAPRINT):
    print(FORCAPRINT[erros])
    print(f'Letras Erradas: {letrasErradas}')
    for l in espaços:
        print(f'{l} ',end='')
    print()

def recebePalpite():
    while True:
        letra = str(input("Advinhe uma letra da palavra: ")).lower()[0]
        if letra in letras:
            print("A letra já foi escolhida. Escolha novamente!")
        else:
            return letra


def acertouLetra(letra, espaços):
    novaEspaços = ''
    for i in range(len(palavraSecreta)):
        if letra == palavraSecreta[i]:
            novaEspaços += letra
        else:
            novaEspaços += espaços[i]
    return novaEspaços


FORCAPRINT = ['''

  +---+
  |   |
      |
      |
      |
      |
========''','''

  +---+
  |   |
  O   |
      |
      |
      |
========''','''

  +---+
  |   |
  O   |
  |   |
      |
      |
========''','''

  +---+
  |   |
  O   |
 /|   |
      |
      |
========''','''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
========''','''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========''','''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========''']
palavraSecreta = sorteiaPalavra()
espaços = '_'*len(palavraSecreta)
letras = ''
letrasErradas = ''
erros = 0

print("J O G O  D A  F O R C A")
print("=======================")

# Loop Principal
while True:
    mostraTela(FORCAPRINT)
    if erros >= 6:
        print("Infelizmente você perdeu a cabeça...")
        break
    else:
        letra = recebePalpite()

    if letra in letras: # É letra repetida
        print("Você já usou essa letra...")
    elif letra in palavraSecreta: # Acertou uma letra
        letras = letras + letra
        espaços = acertouLetra(letra, espaços)
    else: # Letra errada
        letrasErradas = letrasErradas + letra
        letras = letras + letra
        erros += 1

    if '_' not in espaços:
        print(f'Perfeito. A palavra secreta é {palavraSecreta}')
        print("Você se salvou!!")
        break

print("Quer jogar novamente?")

