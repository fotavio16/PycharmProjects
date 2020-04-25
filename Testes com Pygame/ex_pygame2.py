import pygame, sys
from pygame.locals import *
import pygame.mixer

pygame.init()
tela = pygame.display.set_mode((610, 550))

bola = pygame.Surface((0,0))
xis = pygame.Surface((0,0))

text = pygame.font.SysFont("Arial.ttf", 32)
pontosJogadorBola = pygame.Surface((0,0))
pontosJogadorXis = pygame.Surface((0,0))

efeitoXis = pygame.mixer.Sound("som.wav")
efeitoBola = pygame.mixer.Sound("som1.wav")

BolaPosX = 80
BolaPosY = 45

XisPosX = 250
XisPosY = 45

comecou = False

clock = pygame.time.Clock()
continuar = True
while (continuar):
    clock.tick(60)

    if comecou == False:
        novoJogo = text.render("Novo Jogo", True, (0, 0, 0))
        novoJogoRect = novoJogo.get_rect().move(450, 500)

    for event in pygame.event.get():
        if event.type == QUIT:
            continuar = False

        if comecou == True:
            if pygame.mouse.get_pressed()[0]:
                efeitoBola.play()
                bola = pygame.image.load('bola.png').convert_alpha()
                BolaPosX = pygame.mouse.get_pos()[0]
                BolaPosY = pygame.mouse.get_pos()[1]

            elif pygame.mouse.get_pressed()[2]:
                efeitoXis.play()
                xis = pygame.image.load('xis.png').convert_alpha()
                XisPosX = pygame.mouse.get_pos()[0]
                XisPosY = pygame.mouse.get_pos()[1]

    if novoJogoRect.collidepoint(pygame.mouse.get_pos()) and comecou == False:
        novoJogo = text.render("Novo Jogo", True, (255,0,0))
        if pygame.mouse.get_pressed()[0]:
            comecou = True
            novoJogo = pygame.Surface((0,0))
            pontosJogadorBola = text.render("Jogador 1 = ", True, (0,0,255))
            pontosJogadorXis = text.render("Jogador 2 = ", True, (0, 0, 255))

    tela.fill((255, 255, 255))

    tela.blit(novoJogo, (450,500))
    tela.blit(pontosJogadorBola, (10, 10))
    tela.blit(pontosJogadorXis, (440, 10))

    # primeira linha
    #pygame.draw.line(tela, (0, 0, 0), (100, 70), (170, 130), 5)
    #pygame.draw.line(tela, (0, 0, 0), (100, 130), (170, 70), 5)
    #tela.blit(xis, (85, 50))
    #pygame.draw.circle(tela, (255, 0, 0), (300, 100), 45)
    #tela.blit(bola, (250, 45))
    #pygame.draw.line(tela, (0, 0, 0), (430, 70), (500, 130), 5)
    #pygame.draw.line(tela, (0, 0, 0), (430, 130), (500, 70), 5)
    #tela.blit(xis, (415, 50))

    # segunda linha
    #pygame.draw.circle(tela, (255, 0, 0), (130, 220), 45)
    #tela.blit(bola, (85, 175))
    #pygame.draw.line(tela, (0, 0, 0), (270, 200), (340, 260), 5)
    #pygame.draw.line(tela, (0, 0, 0), (270, 260), (340, 200), 5)
    #tela.blit(xis, (250, 180))
    #pygame.draw.circle(tela, (255, 0, 0), (480, 220), 45)
    #tela.blit(bola, (420, 175))

    # terceira Linha
    #ygame.draw.line(tela, (0, 0, 0), (100, 330), (170, 390), 5)
    #pygame.draw.line(tela, (0, 0, 0), (100, 390), (170, 330), 5)
    #tela.blit(xis, (85, 310))
    #pygame.draw.circle(tela, (255, 0, 0), (300, 360), 45)
    #tela.blit(bola, (250, 305))
    #pygame.draw.line(tela, (0, 0, 0), (430, 330), (500, 390), 5)
    #pygame.draw.line(tela, (0, 0, 0), (430, 390), (500, 330), 5)
    #tela.blit(xis, (415, 310))

    # tabuleiro
    pygame.draw.line(tela, (0, 0, 0), (200, 50), (200, 420), 5)
    pygame.draw.line(tela, (0, 0, 0), (400, 50), (400, 420), 5)
    pygame.draw.line(tela, (0, 0, 0), (80, 150), (530, 150), 5)
    pygame.draw.line(tela, (0, 0, 0), (80, 300), (530, 300), 5)

    tela.blit(bola,(BolaPosX,BolaPosY))
    tela.blit(xis, (XisPosX,XisPosY))

    pygame.display.flip()
