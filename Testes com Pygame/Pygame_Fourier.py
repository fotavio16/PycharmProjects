"""
 Pygame base template for opening a window


"""

import pygame, random, sys, math

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
FPS = 60 # frames per second, the general speed of the program
WINDOWWIDTH = 700 # size of window's width in pixels
WINDOWHEIGHT = 500 # size of windows' height in pixels

def circuloNoCentro(tela, cor, x, y, raio, linha=None):
    if linha != None:
        pygame.draw.ellipse(tela, cor, [x - raio, y - raio, raio * 2, raio * 2], linha)
    else:
        pygame.draw.ellipse(tela, cor, [x - raio, y - raio, raio * 2, raio * 2])

def main():
    global clock, screen

    pygame.init()

    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.display.set_caption("Teste com Série de Fourier")

    # Loop until the user clicks the close button.
    done = False

    radius = 100
    time = 0
    wave = []
    CENTER_X = 200
    CENTER_Y = 200
    pos_x = CENTER_X * 2

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Set positions of graphics
    background_position = [0, 0]

    # Load and set up graphics.

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # --- Screen-clearing code goes here

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.

        # If you want a background image, replace this clear with blit'ing the
        # background image.
        screen.fill(BLACK)

        circuloNoCentro(screen, YELLOW, CENTER_X, CENTER_Y, radius, 2)

        x = radius * math.cos(time) + CENTER_X
        y = CENTER_Y + radius * math.sin(time)
        wave.insert(0, y)
        wave2 = []
        for i in range(len(wave)):
            wave2.append([i + CENTER_X*2, wave[i]])


        circuloNoCentro(screen, WHITE, x, y, 8)
        pygame.draw.line(screen, WHITE, [CENTER_X, CENTER_Y], [x, y], 2)

        pygame.draw.line(screen, WHITE, [x, y], wave2[0], 2)

        if len(wave) > 2:
            pygame.draw.lines(screen, GREEN, False, wave2, 1)


        #for i in range(len(wave)):
        #    pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)

        time += 0.05

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(FPS)

    # Close the window and quit.
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
