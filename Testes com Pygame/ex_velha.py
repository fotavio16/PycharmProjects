import pygame
from pygame.locals import *

# Inicia o pygame
pygame.init()

# Inicia a janela
tela = pygame.display.set_mode([640,480])
pygame.display.set_caption("Teste Jogo da Velha")

# Define as cores utilizadas
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
AZULSTEEL = (70, 130, 180)
VERDEHUNTER = (53, 94, 59)
VERMELHOINDIANO = (205,92,92)

# Inicia as fontes
basicFont = pygame.font.SysFont(None, 32)

# Inicia o texto
text = basicFont.render('Jogo da Velha', True, BLACK)
textRect = text.get_rect()
textRect.centerx = tela.get_rect().centerx
textRect.top = 70

# Define a superfície do tabuleiro do jogo
tabuleiro = pygame.Surface([200,200])
tabuleiro.fill(AZULSTEEL)


# Inicia a variável de saída
sair = False

while sair == False:
    # Verifica se a janela foi fechada
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True

    # desenha o fundo branco
    tela.fill(WHITE)

    # desenha o texto na janela
    tela.blit(text, textRect)

    # Desenha o tabuleiro
    tela.blit(tabuleiro, [220,100])

    # Desenha as linhas do tabuleiro
    pygame.draw.line(tabuleiro, BLACK, (66, 5), (66, 195), 3)
    pygame.draw.line(tabuleiro, BLACK, (134, 5), (134, 195), 3)
    pygame.draw.line(tabuleiro, BLACK, (5, 66), (195, 66), 3)
    pygame.draw.line(tabuleiro, BLACK, (5, 134), (195, 134), 3)

    # Desenha os círculos
    pygame.draw.circle(tabuleiro, VERMELHOINDIANO, (33, 33), 20, 0)
    pygame.draw.circle(tabuleiro, VERMELHOINDIANO, (33, 100), 20, 0)
    pygame.draw.circle(tabuleiro, VERMELHOINDIANO, (33, 167), 20, 0)
    pygame.draw.circle(tabuleiro, VERMELHOINDIANO, (167, 167), 20, 0)


    # Desenha os xis
    pygame.draw.line(tabuleiro, VERDEHUNTER, (144, 10), (190, 56), 5)
    pygame.draw.line(tabuleiro, VERDEHUNTER, (144, 56), (190, 10), 5)
    pygame.draw.line(tabuleiro, VERDEHUNTER, (76, 76), (124, 124), 5)
    pygame.draw.line(tabuleiro, VERDEHUNTER, (76, 124), (124, 76), 5)
    pygame.draw.line(tabuleiro, VERDEHUNTER, (76, 144), (124, 190), 5)
    pygame.draw.line(tabuleiro, VERDEHUNTER, (76, 190), (124, 144), 5)


    # desenha a janela na tela
    pygame.display.update()

