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
walkRightEnemy = [pygame.image.load('imagens/R1E.png'), pygame.image.load('imagens/R2E.png'), pygame.image.load('imagens/R3E.png'),
             pygame.image.load('imagens/R4E.png'), pygame.image.load('imagens/R5E.png'), pygame.image.load('imagens/R6E.png'),
             pygame.image.load('imagens/R7E.png'), pygame.image.load('imagens/R8E.png'), pygame.image.load('imagens/R9E.png'),
             pygame.image.load('imagens/R10E.png'), pygame.image.load('imagens/R11E.png')]
walkLeftEnemy = [pygame.image.load('imagens/L1E.png'), pygame.image.load('imagens/L2E.png'), pygame.image.load('imagens/L3E.png'),
            pygame.image.load('imagens/L4E.png'), pygame.image.load('imagens/L5E.png'), pygame.image.load('imagens/L6E.png'),
            pygame.image.load('imagens/L7E.png'), pygame.image.load('imagens/L8E.png'), pygame.image.load('imagens/L9E.png'),
            pygame.image.load('imagens/L10E.png'), pygame.image.load('imagens/L11E.png')]


class Player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                screen.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                screen.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                screen.blit(walkRight[0], (self.x,self.y))
            else:
                screen.blit(walkLeft[0], (self.x, self.y))


class Projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)


class Enemy(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0

        if self.vel > 0:
            screen.blit(walkRightEnemy[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            screen.blit(walkLeftEnemy[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0

def redrawGameWindow():
    # We have 9 images for our walking animation, I want to show the same image for 3 frames
    # so I use the number 27 as an upper bound for walkCount because 27 / 3 = 9. 9 images shown
    # 3 times each animation.
    global walkCount, left, right

    screen.blit(bg, (0, 0))  # This will draw our background image at (0,0)

    man.draw(screen)
    goblin.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)

    pygame.display.flip()

def main():
    global clock, screen, man, bullets, goblin

    pygame.init()

    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.display.set_caption("First Move and Keys")

    # Loop until the user clicks the close button.
    run = True

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Set positions of graphics
    background_position = [0, 0]

    # Cria o personagem
    man = Player(200, 410, 64, 64)
    goblin = Enemy(100, 410, 64, 64, 300)

    # Cria os projéteis
    bullets = []

    # -------- Main Program Loop -----------
    while run:
        # --- Main event loop
        #pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

        # Controle da lista de bullets
        for bullet in bullets:
            if bullet.x < 500 and bullet.x > 0:
                bullet.x += bullet.vel  # Moves the bullet
            else:
                bullets.pop(bullets.index(bullet))  # Remove os bullets off the screen

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            if man.left:
                facing = -1
            else:
                facing = 1

            if len(bullets) < 5:  # This will make sure we cannot exceed 5 bullets on the screen at once
                bullets.append(
                    Projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0, 0), facing))

        if keys[K_LEFT] and man.x > man.vel:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.standing = False
        elif keys[K_RIGHT] and man.x < WINDOWWIDTH - man.width - man.vel:
            man.x += man.vel
            man.left = False
            man.right = True
            man.standing = False
        else: # Reset the animation if it is not moving
            main.standing = True
            man.walkCount = 0

        if not(man.isJump):
            if keys[K_UP]:
                man.isJump = True
                man.right = False
                man.left = False
                man.walkCount = 0
        else:
            if man.jumpCount >= -10:
                neg = 1
                if man.jumpCount < 0:
                    neg = -1
                man.y -= (man.jumpCount ** 2) * 0.5 * neg
                man.jumpCount -= 1
            else:
                man.isJump = False
                man.jumpCount = 10


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
