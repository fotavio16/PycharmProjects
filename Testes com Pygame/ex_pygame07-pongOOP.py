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
FPS = 80 # frames per second, the general speed of the program
WINDOWWIDTH = 700 # size of window's width in pixels
WINDOWHEIGHT = 500 # size of windows' height in pixels


class Ball(object):
    def __init__(self, x, y, vx, vy, raio, cor):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.raio = raio
        self.cor = cor

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def draw(self, surface):
        pygame.draw.circle(surface, self.cor, (self.x, self.y), self.raio)

    def rect(self):
        return pygame.Rect(self.x - self.raio, self.y - self.raio, 2 * self.raio, 2 * self.raio)



class Game(object):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        self.ball = Ball(int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2), 3, 3, 10, GREEN)


    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            self.draw()

    def draw(self):
        self.screen.fill(Game.WHITE)
        self.ball.draw(self.screen)
        pygame.display.update()


def main():
    global clock, screen

    pygame.init()

    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.display.set_caption("Animação, Colisão e Texto")

    # Define a font
    fonte = pygame.font.Font('freesansbold.ttf', 18)

    # Loop until the user clicks the close button.
    done = False


    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Set positions of graphics
    background_position = [0, 0]

    # Load and set up graphics.
    xPos = 250
    yPos = 150
    xVel = 3
    yVel = 3

    bPos = 210
    bVel = 0

    gameScore = 0

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    bVel = -5
                elif event.key == K_RIGHT:
                    bVel = 5
            if event.type == KEYUP:
                if event.key == K_RIGHT or event.key == K_LEFT:
                    bVel = 0


        # --- Screen-clearing code goes here

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.

        # If you want a background image, replace this clear with blit'ing the
        # background image.
        screen.fill(WHITE)

        # Animação com círculo
        pygame.draw.circle(screen, RED, (xPos, yPos), 10)

        # Move a bola
        xPos += xVel
        yPos += yVel

        # Check de borda da tela
        if xPos > WINDOWWIDTH - 10 or xPos < 10:
            xVel = -xVel
        if yPos > WINDOWHEIGHT - 10 or yPos < 10:
            yVel = -yVel

        # Barra de Colisão
        pygame.draw.rect(screen, BLUE, (bPos, WINDOWHEIGHT - 20, 80, 20))

        # Check os limites da tela
        if bPos >= 0 and bVel < 0:
            bPos += bVel
        elif bPos <= WINDOWWIDTH - 80 and bVel > 0:
            bPos += bVel

        # Check a colisão
        if yPos > WINDOWHEIGHT - 30:
            if pygame.Rect(bPos, WINDOWHEIGHT - 20, 80, 20).colliderect((xPos-10, yPos+10, 20, 20)):
                yVel = -yVel
            elif yVel > 0:
                gameScore += 1
                yPos = int(WINDOWHEIGHT / 2)
                yVel = 3


        # Renderiza a mensagem no centro do retângulo
        score = fonte.render(str(gameScore), True, RED)
        scoreRect = score.get_rect()
        scoreRect.center = (480, 20)

        # Blit msg
        screen.blit(score, scoreRect)


        #for i in range(len(wave)):
        #    pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)



        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(FPS)

    # Close the window and quit.
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    Game().play()
