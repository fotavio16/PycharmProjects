import pygame, sys
from pygame.locals import *
import time

pygame.init()

# set up the window
displaysurf = pygame.display.set_mode((500,400), 0, 32)
pygame.display.set_caption('Drawing')
soundObj = pygame.mixer.Sound('som.wav')

# set up the colors
BLACK = (  0,  0,  0)
WHITE = (255,255,255)
RED   = (255,  0,  0)
GREEN = (  0,255,  0)
BLUE  = (  0,  0,255)

# draw on the surface object
displaysurf.fill(WHITE)
pygame.draw.line(displaysurf, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(displaysurf, BLUE, (120, 60), (60, 120))
pygame.draw.line(displaysurf, BLUE, (60, 120), (120, 120), 4)
pygame.draw.aaline(displaysurf, BLUE, (160, 60), (320, 60), 8)
pygame.draw.aaline(displaysurf, BLUE, (320, 60), (160, 200), 2)
pygame.draw.aaline(displaysurf, BLUE, (160, 200), (320, 200), 6)

soundObj.play()
time.sleep(1)
soundObj.stop()

# run the game loop
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
