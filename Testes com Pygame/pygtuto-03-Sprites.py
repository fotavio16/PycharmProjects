"""
 Pygame base template for opening a window


"""

import pygame, random, sys, math
from pygame.locals import *


# Define some colors
#            R    G    B
BLACK    = (  0,   0,   0)
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
SKY_BLUE = (135, 206, 235)
DARK_GREEN = (  0, 100,   0)
DARK_SPRING_GREEN = ( 23, 114,  69)
DARK_BROWN = (101,  67,  33)
LIGHT_GRAY = (211, 211, 211)
ORANGE_SUN = (243, 130,  53)

# Set the width and height of the screen [width, height]
FPS = 27 # frames per second, the general speed of the program
WINDOWWIDTH = 850 # size of window's width in pixels
WINDOWHEIGHT = 500 # size of windows' height in pixels

# Carrega as imagens
walkRight = [pygame.image.load('imagens/R1.png'), pygame.image.load('imagens/R2.png'), pygame.image.load('imagens/R3.png'), pygame.image.load('imagens/R4.png'), pygame.image.load('imagens/R5.png'), pygame.image.load('imagens/R6.png'), pygame.image.load('imagens/R7.png'), pygame.image.load('imagens/R8.png'), pygame.image.load('imagens/R9.png')]
walkLeft = [pygame.image.load('imagens/L1.png'), pygame.image.load('imagens/L2.png'), pygame.image.load('imagens/L3.png'), pygame.image.load('imagens/L4.png'), pygame.image.load('imagens/L5.png'), pygame.image.load('imagens/L6.png'), pygame.image.load('imagens/L7.png'), pygame.image.load('imagens/L8.png'), pygame.image.load('imagens/L9.png')]
bg = pygame.image.load('imagens/bg.jpg')
char = pygame.image.load('imagens/standing.png')


def redrawGameWindow():
    # We have 9 images for our walking animation, I want to show the same image for 3 frames
    # so I use the number 27 as an upper bound for walkCount because 27 / 3 = 9. 9 images shown
    # 3 times each animation.
    global walkCount, left, right

    screen.blit(bg, (0, 0))  # This will draw our background image at (0,0)

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        screen.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        screen.blit(walkRight[walkCount // 3], (x, y))
        walkCount += 1
    else:
        screen.blit(char, (x,y))



    #pygame.display.update()
    pygame.display.flip()

def main():
    global clock, screen, walkCount, left, right, x, y

    pygame.init()

    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.display.set_caption("First Move and Keys")

    # Loop until the user clicks the close button.
    run = True

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Set positions of graphics
    background_position = [0, 0]

    # Load and set up graphics.
    x = 50
    y = 400
    width = 40
    height = 60
    velx = vely = 5

    # Controle do salto
    isJump = False
    jumpCount = 10

    # Controle das Imagens
    left = False
    right = False
    walkCount = 0

    # -------- Main Program Loop -----------
    while run:
        # --- Main event loop
        #pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[K_LEFT] and x > velx:
            x -= velx
            left = True
            right = False

        elif keys[K_RIGHT] and x < WINDOWWIDTH - width - velx:
            x += velx
            left = False
            right = True

        else: # Reset the animation if it is not moving
            left = False
            right = False
            walkCount = 0

        if not(isJump):
            if keys[K_SPACE]:
                isJump = True
                right = False
                left = False
                walkCount = 0
        else:
            if jumpCount >= -10:
                y -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1
            else:
                jumpCount = 10
                isJump = False

        # --- Screen-clearing code goes here

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.

        # If you want a background image, replace this clear with blit'ing the
        # background image.
        #screen.fill(BLACK)
        redrawGameWindow()

        # Animação com retângulo
        #pygame.draw.rect(screen, RED, (x, y, width, height))


        # Barra de Colisão


        #for i in range(len(wave)):
        #    pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)



        # --- Go ahead and update the screen with what we've drawn.
        #pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(FPS)

    # Close the window and quit.
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
