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
WINDOWWIDTH = 255 # size of window's width in pixels
WINDOWHEIGHT = 255 # size of windows' height in pixels


def main():
    global clock, screen

    pygame.init()

    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.display.set_caption("Teste com Arrays e Grids Pygame")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Variáveis usadas nos grids
    width = 20
    height = 20
    margin = 5

    # Cria um array 10 x 10
    grid = []
    for row in range(10):
        grid.append([])
        for col in range(10):
            grid[row].append(0)

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Pega a posição do mouse
                pos = pygame.mouse.get_pos()
                x = (pos[0] - margin) // (width + margin)
                y = (pos[1] - margin) // (height + margin)
                grid[y][x] = 1
                print(f'Click: {pos} - Coordenadas: {y} e {x}')


        # Limpa a tela
        screen.fill(BLACK)



        # Desenha um box com a altura e largura
        # nas variáveis criadas
        for col in range(margin,WINDOWWIDTH-margin,width+margin):
            for lin in range(margin, WINDOWHEIGHT-margin,height+margin):
                color = WHITE
                # print(f'{(lin-margin)//(height+margin)} - {(col-margin)//(width+margin)} = {grid[(lin-margin)//(height+margin)][(col-margin)//(width+margin)]}')
                if grid[(lin-margin)//(height+margin)][(col-margin)//(width+margin)] == 1:
                    color = GREEN
                pygame.draw.rect(screen, color, [col, lin, width, height])








        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(FPS)

    # Close the window and quit.
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
