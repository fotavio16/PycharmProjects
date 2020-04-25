import pygame, sys
from pygame.locals import *
from random import randint

# inicia o pygame
pygame.init()

# inicia a janela
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Jogo da Velha')

# inicia as cores utilizadas
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
STEELBLUE = (70, 130, 180)
GREENHUNTER = (43, 70, 62)
INDIANRED = (205, 92, 92)

# inicia as fontes
basicFont = pygame.font.SysFont(None, 48)

# inicia o texto
text = basicFont.render('Jogo da Velha', True, BLACK, WHITE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = 30


# desenha o fundo branco
windowSurface.fill(WHITE)

# desenha as linhas do tabuleiro
pygame.draw.line(windowSurface, STEELBLUE, (100, 150), (400, 150), 4)
pygame.draw.line(windowSurface, STEELBLUE, (100, 250), (400, 250), 4)
pygame.draw.line(windowSurface, STEELBLUE, (200, 70), (200, 340), 4)
pygame.draw.line(windowSurface, STEELBLUE, (300, 70), (300, 340), 4)


# desenha os circulos dos "O"
pygame.draw.circle(windowSurface, INDIANRED, (150, 110), 30, 3)
pygame.draw.circle(windowSurface, INDIANRED, (150, 200), 30, 3)
pygame.draw.circle(windowSurface, INDIANRED, (150, 300), 30, 3)
pygame.draw.circle(windowSurface, INDIANRED, (350, 300), 30, 3)

# desenha as linhas dos "X"
pygame.draw.line(windowSurface, GREENHUNTER, (325, 85), (375, 135), 4)
pygame.draw.line(windowSurface, GREENHUNTER, (325, 135), (375, 85), 4)
pygame.draw.line(windowSurface, GREENHUNTER, (225, 175), (275, 225), 4)
pygame.draw.line(windowSurface, GREENHUNTER, (225, 225), (275, 175), 4)
pygame.draw.line(windowSurface, GREENHUNTER, (225, 275), (275, 325), 4)
pygame.draw.line(windowSurface, GREENHUNTER, (225, 325), (275, 275), 4)

# desenha linha do vencedor
pygame.draw.line(windowSurface, (randint(0,255), randint(0,255), randint(0,255)), (150, 70), (150, 340), randint(1,10))


# desenha o texto na janela
windowSurface.blit(text, textRect)

# desenha a janela na tela
pygame.display.update()

# roda o loop do jogo
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()