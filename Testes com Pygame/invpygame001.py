import pygame, sys
from pygame.locals import *

pygame.init()
displaysurf = pygame.display.set_mode((800,600))
pygame.display.set_caption('Hello World!')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()