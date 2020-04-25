import pygame
from pygame.locals import *
from time import sleep

# Inicia o pygame
pygame.init()

# Inicia a janela
tela = pygame.display.set_mode([500,400], 0, 32)
pygame.display.set_caption("Hello Mundo!")

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

# Inicia as fontes
basicFont = pygame.font.SysFont(None, 48)

# Inicia o texto
text = basicFont.render('Hello Mundo!', True, BLUE)
textRect = text.get_rect()
textRect.centerx = tela.get_rect().centerx
textRect.centery = tela.get_rect().centery

# Inicia a variável de saída
sair = False

while sair == False:
    # Verifica se a janela foi fechada
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True

    # desenha o fundo branco
    tela.fill(WHITE)

    # desenha um poligono verde na superficie
    pygame.draw.polygon(tela, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

    # desenha algumas linhas azuis na superficie
    pygame.draw.line(tela, BLUE, (300, 60), (360, 60), 4)
    pygame.draw.line(tela, ROXO, (360, 60), (300, 120), 4)
    pygame.draw.line(tela, VERDE, (300, 120), (360, 120), 4)

    # desenha um circulo azul na superficie
    pygame.draw.circle(tela, YELLOW, (300, 30), 20, 0)

    # desenha uma elipse vermelha na superficie
    pygame.draw.ellipse(tela, RED, (300, 250, 40, 80), 1)

    # desenha o retangulo do fundo do texto na superficie
    pygame.draw.rect(tela, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

    # obtem um array de pixel da superficie
    pixArray = pygame.PixelArray(tela)
    pixArray[480][380] = BLACK
    pixArray[481][380] = BLACK
    pixArray[482][380] = BLACK
    pixArray[483][380] = BLACK
    pixArray[484][380] = BLACK
    del pixArray

    # desenha o texto na janela
    tela.blit(text, textRect)

    # desenha a janela na tela
    pygame.display.update()

