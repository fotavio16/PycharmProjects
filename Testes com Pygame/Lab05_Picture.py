# Import a library of functions called 'pygame'
import pygame, random

# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
SKY_BLUE = (135, 206, 235)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 100, 0)
DARK_SPRING_GREEN = (23, 114, 69)
RED = (255, 0, 0)
DARK_BROWN = (101, 67, 33)
LIGHT_GRAY = (211, 211, 211)
YELLOW = (255, 255, 0)
ORANGE_SUN = (243, 130, 53)

PI = 3.141592653

# Set the height and width of the screen
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

pygame.display.set_caption("Picture LAB")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Lista de coordenadas das Aves
birds = []
for i in range(10):
    # Any random x from 0 to the width of the screen
    x = random.randrange(0, WINDOWWIDTH - 50)

    # Any random y from in the top 2/3 of the screen.
    # No birds on the ground.
    y = random.randrange(0, WINDOWHEIGHT * 2 / 3)
    birds.append((x,y))


def draw_background():
    """
    This function draws the background. Specifically, the sky and ground.
    """
    # Draw the sky in the top dois-terços
    pygame.draw.rect(screen, SKY_BLUE, [0, 0, WINDOWWIDTH, WINDOWHEIGHT * 2 /3])

    # Draw the ground
    pygame.draw.rect(screen, DARK_SPRING_GREEN, [0, WINDOWHEIGHT * 2 /3, WINDOWWIDTH, WINDOWHEIGHT / 3])

def draw_sun(x, y):

    #pygame.draw.ellipse(screen, YELLOW, [x, y, 45, 45])
    pygame.draw.ellipse(screen, ORANGE_SUN, [x, y, 40, 40])


def draw_bird(x, y):
    """
    Draw a bird using a couple arcs.
    """
    pygame.draw.arc(screen, BLACK, [x, y, 20, 20], 0, PI / 2, 2)
    pygame.draw.arc(screen, BLACK, [x + 20, y, 20, 20], PI / 2, PI, 2)

def draw_pine_tree(center_x, center_y):
    """
    This function draws a pine tree at the specified location.

    Args:
      :center_x: x position of the tree center.
      :center_y: y position of the tree trunk center.
    """
    # Draw the trunk
    pygame.draw.rect(screen, DARK_BROWN, [center_x - 10, center_y - 20, 20, 40])

    # Draw the triângulo no topo do retângulo
    lista_pontos = [[center_x - 40, center_y - 20], [center_x, center_y - 120], [center_x + 40, center_y - 20]]
    pygame.draw.polygon(screen, DARK_GREEN, lista_pontos)

def draw_casa(center_x, center_y):
    '''

    :param center_x:
    :param center_y:
    :return:
    '''
    # Desenha o retângulo
    pygame.draw.rect(screen, LIGHT_GRAY, [center_x - 60, center_y - 50, 120, 100])
    # Desenha o telhado
    lista_pontos = [[center_x - 65, center_y - 50], [center_x, center_y - 90], [center_x + 65, center_y - 50]]
    pygame.draw.polygon(screen, BLACK, lista_pontos)
    # Desenha a porta
    pygame.draw.ellipse(screen, YELLOW, [center_x - 50, center_y - 18, 35, 30])
    pygame.draw.rect(screen, BLUE, [center_x - 50, center_y - 3, 35, 50])
    # Desenha as janelas
    pygame.draw.rect(screen, YELLOW, [center_x + 5, center_y - 3, 45, 30])
    pygame.draw.rect(screen, RED, [center_x + 5, center_y - 45, 45, 30])

# Loop as long as done == False
while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # All drawing code happens after the for loop and but
    # inside the main while not done loop.

    # Clear the screen and set the screen background
    #screen.fill(WHITE)
    draw_background()

    draw_sun(WINDOWWIDTH - 70, 50)


    # Desenha as Aves
    for coord in birds:
        draw_bird(coord[0],coord[1])

    # Draw the top row of trees
    for x in range(45, WINDOWWIDTH, 90):
        draw_pine_tree(x, WINDOWHEIGHT * 2 / 3)

    # Desenha a Casa
    for x in range(75, WINDOWWIDTH - 160, 140):
        draw_casa(x, WINDOWHEIGHT - 60)

    # Draw on the screen a line from (0,0) to (100,100)
    # 5 pixels wide.
    # pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)

    # Draw on the screen several lines from (0,10) to (100,110)
    # 5 pixels wide using a loop
    #for y_offset in range(0, 100, 10):
    #    pygame.draw.line(screen, RED, [0, 10 + y_offset], [100, 110 + y_offset], 5)

    # Draw a rectangle
    #pygame.draw.rect(screen, BLACK, [20, 20, 250, 100], 2)

    # Draw an ellipse, using a rectangle as the outside boundaries
    #pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)

    # Draw an arc as part of an ellipse.
    # Use radians to determine what angle to draw.
    #pygame.draw.arc(screen, BLACK, [20, 220, 250, 200], 0, PI / 2, 2)
    #pygame.draw.arc(screen, GREEN, [20, 220, 250, 200], PI / 2, PI, 2)
    #pygame.draw.arc(screen, BLUE, [20, 220, 250, 200], PI, 3 * PI / 2, 2)
    #pygame.draw.arc(screen, RED, [20, 220, 250, 200], 3 * PI / 2, 2 * PI, 2)

    # This draws a triangle using the polygon command
    # pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)

    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)

    # Render the text. "True" means anti-aliased text.
    # Black is the color. This creates an image of the
    # letters, but does not put it on the screen
    text = font.render("Meu desenho", True, BLACK)

    # Put the image of the text on the screen at 250x250
    screen.blit(text, [WINDOWWIDTH - 160, WINDOWHEIGHT - 50])

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

# Be IDLE friendly
pygame.quit()

