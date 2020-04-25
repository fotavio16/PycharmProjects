"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/


"""

import pygame, random, sys

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



def main():
    global clock, screen

    pygame.init()

    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.display.set_caption("LAB 08 - Animation")

    # Loop until the user clicks the close button.
    done = False
    rect_x = 50
    rect_y = 50
    rect_h = 50
    rect_w = 50
    rect_chg_x = 3
    rect_chg_y = 3

    # Cria lista dew coordenadas para flocos de neve
    snow_list = []
    for i in range(50):
        x = random.randrange(0, WINDOWWIDTH)
        y = random.randrange(0, WINDOWHEIGHT)
        snow_list.append([x,y])

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # --- Game logic should go here

        # --- Screen-clearing code goes here

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.

        # If you want a background image, replace this clear with blit'ing the
        # background image.
        screen.fill(BLACK)

        # --- Drawing code should go here
        pygame.draw.rect(screen, SKY_BLUE, [rect_x, rect_y, rect_w, rect_h])

        # Movimenta o retângulo
        rect_x += rect_chg_x
        rect_y += rect_chg_y

        # Desvia o retângulo se necessário
        if rect_x > WINDOWWIDTH - rect_w or rect_x < 0:
            rect_chg_x = -rect_chg_x
        if rect_y < 0 or rect_y > WINDOWHEIGHT - rect_h:
            rect_chg_y = -rect_chg_y

        # Desenha os flocos de neve
        for i in range(len(snow_list)):
            # Desenha
            pygame.draw.circle(screen, WHITE, snow_list[i], 2)
            # Atualiza as coordenadas
            snow_list[i][1] += 1
            if snow_list[i][1] > WINDOWHEIGHT:
                # Reset para o topo da tela
                snow_list[i][1] = random.randrange(-50,-10)
                snow_list[i][0] = random.randrange(0, WINDOWWIDTH-5)

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(FPS)

    # Close the window and quit.
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
