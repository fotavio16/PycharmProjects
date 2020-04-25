# The Nature of Code
# Daniel Shiffman
# Fernando Otávio
# http://natureofcode.com
# Example 1-1: Bouncing Ball, no vectors

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
WINDOWWIDTH = 640 # size of window's width in pixels
WINDOWHEIGHT = 360 # size of windows' height in pixels

class Walker():
    def __init__(self, x=100, y=100, cor=WHITE):
        self.x = x
        self.y = y
        self.cor = cor

    def draw(self, screen):
        pygame.draw.circle(screen, self.cor, (self.x, self.y), 2, 0)

    def move(self):
        choice = random.randint(0,4)
        if choice == 0 and self.x < WINDOWWIDTH:
            self.x = self.x + 1
        elif choice == 1 and self.x > 0:
            self.x = self.x - 1
        elif choice == 2 and self.y < WINDOWHEIGHT:
            self.y = self.y + 1
        elif choice == 3 and self.y > 0:
            self.y = self.y - 1



def main():
    global clock, screen

    pygame.init()

    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.display.set_caption("Nature of Code - Python")

    # Loop until the user clicks the close button.
    done = False

    screen.fill(BLACK)

    willy = Walker()
    watson = Walker(500, 200, YELLOW)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        #screen.fill(BLACK)

        willy.move()

        watson.move()

        willy.draw(screen)

        watson.draw(screen)

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(FPS)

    # Close the window and quit.
    pygame.quit()
    sys.exit()


"""
x = 100
y = 100
xspeed = 2.5
yspeed = 2


def setup():
    size(800, 200)
    smooth()


def draw():
    background(255)
    # Add the current speed to the location.
    global x, y, xspeed, yspeed
    x = x + xspeed
    y = y + yspeed
    if (x > width) or (x < 0):
        xspeed = xspeed * -1
    if (y > height) or (y < 0):
        yspeed = yspeed * -1
    # Display circle at x location
    stroke(0)
    strokeWeight(2)
    fill(127)
    ellipse(x, y, 48, 48)
"""


if __name__ == '__main__':
    main()