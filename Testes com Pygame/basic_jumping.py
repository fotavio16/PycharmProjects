import math, random, sys
import pygame
from pygame.locals import *

# Saída do programa via fechamento da janela
def eventos():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

# Classe do Jogador
class player:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.jumping = False
        self.jump_offset = 0

def keys(player):
    keys = pygame.key.get_pressed()
    if keys[K_SPACE] and player.jumping == False and player.jump_offset == 0:
        player.jumping = True

def do_jumping(player):
    global jump_height

    if player.jumping:
        player.jump_offset+= 1
        if player.jump_offset >= jump_height:
            player.jumping = False
    elif player.jump_offset > 0 and player.jumping == False:
        player.jump_offset -= 1

# Define o tamanho da superfície da tela
W, H = 1600, 900
HW, HH = int(W / 2), int(H / 2)
AREA = W * H

# Inicializa a Tela
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode([W, H])
pygame.display.set_caption("Teste do Jumping")
FPS = 120

# Define as cores
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
RED = (255, 0, 0)
verde = (0,128,0)
laranja = (255,140,0)
amarela = (255,255,0)
azul = (30,144,255)
violeta = (138,43,226)
rosa = (255,20,147)
cinza = (128,128,128)
SOLID_FILL = 0

# Iniciliza o Jogador
p = player(HW, HH, 30)
jump_height = 150

# Loop Principal
while True:
    eventos()
    keys(p)

    do_jumping(p)
    pygame.draw.circle(DS, WHITE, (p.x, p.y - p.jump_offset), p.size, SOLID_FILL)

    if p.jump_offset == 0:
        pygame.draw.rect(DS, WHITE, (HW - 100, HH + p.size, 200, 10), SOLID_FILL)
    else:
        pygame.draw.rect(DS, RED, (HW - 100, HH + p.size, 200, 10), SOLID_FILL)

    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)
