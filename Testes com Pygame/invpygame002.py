import pygame, sys
from pygame.locals import *

pygame.init()

# set up the window
displaysurf = pygame.display.set_mode((500,400), 0, 32)
pygame.display.set_caption('Drawing')

# set up the colors
BLACK = (  0,  0,  0)
WHITE = (255,255,255)
RED   = (255,  0,  0)
GREEN = (  0,255,  0)
BLUE  = (  0,  0,255)

# draw on the surface object
displaysurf.fill(WHITE)
pygame.draw.polygon(displaysurf, GREEN, ((146, 0), (291, 106), (235, 277), (56, 277), (0, 106)))
pygame.draw.line(displaysurf, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(displaysurf, BLUE, (120, 60), (60, 120))
pygame.draw.line(displaysurf, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(displaysurf, BLUE, (300, 50), 20, 0)
pygame.draw.ellipse(displaysurf, RED, (300, 250, 40, 80), 1)
pygame.draw.rect(displaysurf, RED, (200, 150, 100, 50), 1)

pixObj = pygame.PixelArray(displaysurf)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj

# run the game loop
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()