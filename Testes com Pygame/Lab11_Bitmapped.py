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

    pygame.display.set_caption("LAB 11 - Bitmapped e Gráficos")

    # Loop until the user clicks the close button.
    done = False

    # Hide the mouse cursor
    pygame.mouse.set_visible(False)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Before the loop, load the sounds:
    click_sound = pygame.mixer.Sound("laser5.ogg")

    # Set positions of graphics
    background_position = [0, 0]

    # Load and set up graphics.
    background_image = pygame.image.load("Saturn_family.jpg").convert()
    player_image = pygame.image.load("playerShip1_orange.png").convert()
    player_image.set_colorkey(BLACK)

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_sound.play()




        # --- Screen-clearing code goes here

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.

        # If you want a background image, replace this clear with blit'ing the
        # background image.
        #screen.fill(WHITE)

        # Copy image to screen:
        screen.blit(background_image, background_position)

        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        player_position = pygame.mouse.get_pos()
        x = player_position[0]
        y = player_position[1]

        # Copy image to screen:
        screen.blit(player_image, [x, y])



        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(FPS)

    # Close the window and quit.
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
