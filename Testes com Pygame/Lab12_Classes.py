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

lista_de_cores = [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN, SKY_BLUE, ORANGE_SUN, LIGHT_GRAY]

# Set the width and height of the screen [width, height]
FPS = 60 # frames per second, the general speed of the program
WINDOWWIDTH = 700 # size of window's width in pixels
WINDOWHEIGHT = 500 # size of windows' height in pixels


def give_money1(money):
    money += 100

def give_money2(person):
    person.money += 100

class Person():
    def __init__(self):
        self.name = ""
        self.money = 0

class Cat():
    def __init__(self):
        self.name = ""
        self.color = ""
        self.weight = ""

    def meow(self):
        print("Meow")


class Rectangle():
    def __init__(self, x=0, y=0, w=10, h=10):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.change_x = 5
        self.change_y = 5
        self.cor = WHITE

    def draw(self, screen):
        pygame.draw.rect(screen, self.cor, [self.x, self.y, self.width, self.height])

    def move(self):
        if (self.x + self.change_x + self.width) >= WINDOWWIDTH or (self.x + self.change_x) < 0:
            self.change_x *= -1
        if (self.y + self.change_y + self.height) >= WINDOWHEIGHT or (self.y + self.change_y) < 0:
            self.change_y *= -1
        self.x += self.change_x
        self.y += self.change_y


class Ellipse(Rectangle):

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.cor, [self.x, self.y, self.width, self.height])


def main():
    global clock, screen

    pygame.init()

    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.display.set_caption("Teste com Classes e Pygame")

    # Loop until the user clicks the close button.
    done = False

    bob = Person()
    bob.name = "Bob"
    bob.money = 100

    give_money2(bob)
    print(bob.money)

    fumacinha = Cat()
    fumacinha.name = "Fumacinha"
    fumacinha.color = GRAY
    fumacinha.weight = 3.8
    fumacinha.meow()

    my_list = list()

    for i in range(100):
        my_object = Rectangle(0, 0)

        my_object.x = random.randint(0, WINDOWWIDTH-70)
        my_object.y = random.randint(0, WINDOWHEIGHT-70)
        my_object.width = random.randint(10, 40)
        my_object.height = random.randint(10, 40)
        my_object.change_x = random.randint(-3, 3)
        my_object.change_y = random.randint(-3, 3)
        my_object.cor = lista_de_cores[i % 10]

        my_list.append(my_object)

    for i in range(100):
        my_object = Ellipse()

        my_object.x = random.randint(0, WINDOWWIDTH - 70)
        my_object.y = random.randint(0, WINDOWHEIGHT - 70)
        my_object.width = random.randint(10, 40)
        my_object.height = random.randint(10, 40)
        my_object.change_x = random.randint(-3, 3)
        my_object.change_y = random.randint(-3, 3)
        my_object.cor = lista_de_cores[i % 10]

        my_list.append(my_object)

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

        for obj in my_list:
            obj.draw(screen)
            obj.move()

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
    main()
