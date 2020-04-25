import random
import time
import os



# Definições
listaLetras = []
hangmanpics = []
partesBoneco = 0
bonecoCompleto = 4
acertos = 0

# words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
words = 'formiga babuíno texugo morcego urso castor camelo gato molusco cobra puma coiote cão burro pato águia furão ' \
        'raposa rã cabra corvo cervo ganso falcão leão lagarto lhama macaco alce rato mula lontra coruja panda ' \
        'papagaio salamandra toupeira pombo piton coelho rinoceronte salmão foca tubarão ovelha doninha carneiro ' \
        'preguiça aranha cegonha cisne tigre sapo truta peru tartaruga baleia lobo zebra'.split()

def getWord(lista): # Escolhe aleatoriamente uma palavra da lista
    indice = random.randint(0, len(lista)-1)
    return lista[indice]

def mostraTela():
    os.system('CLS')
    print("J O G O  D A  F O R C A")
    print("==" * 12)
    print()
    for letra in palavraSecreta:
        print(" {}".format(letra), end='')
    print("\nLetras usadas: ", end='')
    for letra in listaLetras:
        print(" {}".format(letra), end='')
    print("\n")
    return


#print(words)
palavraSorteada = getWord(words)
#print(palavraSorteada)

# Constroi a palavra secreta que será mostrada na tela
palavraSecreta = []
for i in range(len(palavraSorteada)):
    palavraSecreta.append('-')

acabou = False
while not acabou:
    mostraTela()
    letra = str(input('Digite uma letra diferente: '))
    letraOK = False
    if letra in listaLetras:
        print("A letra digitada já foi utilizada antes")
        time.sleep(2)
    else:
        listaLetras.append(letra)
        for i in range(len(palavraSorteada)):
            if letra == palavraSorteada[i]:
                palavraSecreta[i] = letra
                acertos += 1
                letraOK = True
    if not letraOK:
        partesBoneco += 1
    if acertos == len(palavraSorteada):
        print("\nParabéns! Você venceu!")
        acabou = True
    if partesBoneco == bonecoCompleto:
        print("\nO boneco foi enforcado. Acabou o jogo!")
        acabou = True
