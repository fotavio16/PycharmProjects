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
    def __init__(self, x, y, plty, size):
        self.x = x
        self.y = y
        self.size = size
        self.jumping = False
        self.velocity_index = 0
        self.platform_y = plty

    def do_jumping(self):
        global velocity
        # velocity = list([ -7.5, -7, -6.5, -6, -5.5, -5, -4.5, -4, -3.5, -3, -2.5, -2, -1.5, -1, -0.5, 0,
        #					0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5])

        if self.jumping:
            self.y += velocity[self.velocity_index]
            self.velocity_index += 1
            if self.velocity_index >= len(velocity) - 1:
                self.velocity_index = len(velocity) -1
            if self.y > self.platform_y:
                self.y = self.platform_y
                self.jumping = False
                self.velocity_index = 0

    def draw(self):
        global DS, amarela, SOLID_FILL
        pygame.draw.circle(DS, amarela, (int(self.x), int(self.y)), self.size, SOLID_FILL)

    def do(self):
        self.do_jumping()
        self.draw()

def keys(player):
    keys = pygame.key.get_pressed()
    if keys[K_SPACE] and player.jumping == False:
        player.jumping = True


# Define o tamanho da superfície da tela
W, H = 1600, 900
HW, HH = int(W / 2), int(H / 2)
AREA = W * H

# Inicializa a Tela
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode([W, H])
pygame.display.set_caption("Teste do Jumping")
FPS = 60

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
p = player(HW, HH, HH, 30)
velocity = list([-7.5, -7, -6.5, -6, -5.5, -5, -4.5, -4, -3.5, -3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5])

# Loop Principal
while True:
    eventos()
    keys(p)

    p.do()

    if p.jumping:
        pygame.draw.rect(DS, rosa, (HW - 100, HH + p.size, 200, 10), SOLID_FILL)
    else:
        pygame.draw.rect(DS, amarela, (HW - 100, HH + p.size, 200, 10), SOLID_FILL)

    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(azul)
