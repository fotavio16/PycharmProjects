import pygame, sys
from pygame.locals import *
from random import randint
from time import sleep

class Casas(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Casa(Casas):
    def __init__(self, l, a, x, y, num, texto):
        Casas.__init__(self)
        self.cor = CORES[randint(0,3)]
        self.image = pygame.Surface((l, a))
        self.image.convert()
        self.imgBKP = self.image
        self.rect = Rect(x, y, l, a)
        self.id = num
        if texto == '':
            self.textoNum = textNum.render(str(num), True, BLUE)
        else:
            self.textoNum = textNum.render(texto, True, BLUE)
            self.cor = CORES[4]
        self.image.fill(self.cor)

def buscaCasa(num):
    for c in casas:
        if c.id == num:
            return c
    return ''

def montaTabuleiro():
    mapa = [['L', 1], ['D', 14], ['B', 3], ['E', 15], ['B', 3], ['D', 15], ['B', 3], ['E', 15], ['S', 1]]
    posX = 20
    posY = 85
    num = 0
    for dir in mapa:
        if dir[0] == 'L':
            param = [80, 80, 80, 15, 'Largada']  # [largura, altura, dx, dy, texto especial]
        elif dir[0] == 'S':
            param = [80, 80, 0, 0, 'Chegada']  # [largura, altura, dx, dy, texto especial]
            posX -= 30
            posY -= 15
        elif dir[0] == 'D':
            param = [50, 50, 50, 0, '']  # [largura, altura, dx, dy, texto especial]
        elif dir[0] == 'E':
            param = [50, 50, -50, 0, '']  # [largura, altura, dx, dy, texto especial]
        elif dir[0] == 'B':
            param = [50, 50, 0, 50, '']  # [largura, altura, dx, dy, texto especial]
        for i in range(dir[1]):
            casa = Casa(param[0], param[1], posX, posY, num, param[4])
            casas.add(casa)
            posX += param[2]
            posY += param[3]
            num += 1
    return num - 1

def jogaJogador(posAtual):
    lance = randint(1, 6)
    if posAtual + lance > casaFinal:
        return False
    jogador.image.fill(jogador.cor)
    textoDado = textDado.render(str(lance), True, BLACK)
    dado.fill(PRATA)
    posAtual += lance
    if posAtual == casaFinal:
        return True
    else:
        return False

def jogaComputador(posAtual):
    lance = randint(1, 6)
    if posAtual + lance > casaFinal:
        return False
    computador.image.fill(computador.cor)
    dado.fill(PRATA)
    posAtual += lance
    if posAtual == casaFinal:
        return True
    else:
        return False

def mostraDado(n):
    ct = 0.01
    for i in range(5):
        st = 0.005 * (i +1)
        for j in range(6):
            ct += st
            print(ct)
            sleep(ct)
            textoDado = textDado.render(str(j+1), True, BLACK)
            dado.blit(textoDado, (9, 9))
    #textoDado = textNum.render(str(n), True, BLACK)
    #dado.blit(textoDado, (9, 9))
    return

pygame.init()
tela = pygame.display.set_mode((1200, 800))
casas = pygame.sprite.Group()

textNum = pygame.font.SysFont("Arial.ttf", 24)
textDado = pygame.font.SysFont("Arial.ttf", 32)

imgJogador = pygame.image.load('carinha.png').convert_alpha()
imgComputador = pygame.image.load('Computer.png').convert_alpha()

casaJogador = 0
casaComputador = 0

# Define as cores utilizadas
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PRATA = (192, 192, 192)
VERDE = (128, 128, 0)
ROXO = (128, 0, 128)
FUCSIA = (255, 0, 255)
CINZA = (128, 128, 128)
CIANO = (0, 255, 255)
AZUL = (100, 149, 237)
CORES = [(255, 255, 0), (186,85,211), (255,20,147), (255,165,0), (0,255,127)] # Yellow, MediumOrchid, DeepPink, Laranja, SpringGreen

casaFinal = montaTabuleiro()
print(casaFinal)
dado = pygame.Surface((50,50))
dado.fill(PRATA)
textoDado = textNum.render("", True, BLACK)

clock = pygame.time.Clock()
continuar = True


while (continuar):
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            continuar = False

    tela.fill(CIANO)

    for e in casas:
        tela.blit(e.image, e.rect)
        pygame.draw.rect(tela, BLACK, e.rect, 1)
        e.image.blit(e.textoNum, (2,2))

    jogador = buscaCasa(casaJogador)
    computador = buscaCasa(casaComputador)

    jogador.image.blit(imgJogador, (10, 15))
    computador.image.blit(imgComputador, (5, 17))

    tela.blit(dado, (1000, 150))
    pygame.draw.rect(tela, BLACK, (1000,150,50,50), 1)
    sorteio = textNum.render("Clique Aqui para Jogar Dado", True, BLUE)
    sorteioRect = sorteio.get_rect().move(900, 100)


    if sorteioRect.collidepoint(pygame.mouse.get_pos()):
        sorteio = textNum.render("Clique Aqui para Jogar Dado", True, RED)
        if pygame.mouse.get_pressed()[0]:
            sorteio = pygame.Surface((0,0))
            # Sorteia Dado do Jogador
            lance = randint(1,6)
            sleep(1)
            #mostraDado(lance)
            if lance + casaJogador > casaFinal:
                lance = 0
            else:
                jogador.image.fill(jogador.cor)
                textoDado = textDado.render(str(lance), True, BLACK)
                dado.fill(PRATA)
                casaJogador += lance
                if casaJogador == casaFinal:
                    #continuar = False
                    sorteio = textNum.render("Você Venceu! Parabéns!", True, BLUE)
                    #break
            # Sorteia Dado do Computador
            lance = randint(1, 6)
            if lance + casaComputador > casaFinal:
                lance = 0
            else:
                computador.image.fill(computador.cor)
                casaComputador += lance
                if casaComputador == casaFinal:
                    #continuar = False
                    sorteio = textNum.render("O Computador Venceu! Melhor sorte da próxima vez.", True, BLUE)
                    #break

    tela.blit(sorteio, (900, 100))
    dado.blit(textoDado, (9,9))

    pygame.display.update()





