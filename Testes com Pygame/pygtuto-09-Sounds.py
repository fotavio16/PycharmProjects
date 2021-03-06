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

pygame.init()

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

bulletSound = pygame.mixer.Sound('bullet.ogg')
hitSound = pygame.mixer.Sound('hit.ogg')

music = pygame.mixer.music.load('imagens/music.mp3')
pygame.mixer.music.play(-1)

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
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, screen):
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
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        #pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = 60
        self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255, 0, 0))
        screen.blit(text, (250 - (text.get_width() / 2), 200))
        pygame.display.update()
        i = 0
        while i < 200:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 201
                    pygame.quit()

class Projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x,self.y), self.radius)


class Enemy(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self, screen):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                screen.blit(walkRightEnemy[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                screen.blit(walkLeftEnemy[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(screen, RED, (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(screen, DARK_GREEN, (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))

            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            #pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                #self.x += self.vel
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                #self.x += self.vel
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('hit')


def redrawGameWindow():
    # We have 9 images for our walking animation, I want to show the same image for 3 frames
    # so I use the number 27 as an upper bound for walkCount because 27 / 3 = 9. 9 images shown
    # 3 times each animation.
    global walkCount, left, right

    screen.blit(bg, (0, 0))  # This will draw our background image at (0,0)
    text = font.render('Score: ' + str(score), 1, (0, 0, 0))
    screen.blit(text, (350, 10))
    man.draw(screen)
    goblin.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)

    pygame.display.flip()

def main():
    global clock, screen, man, bullets, goblin, font, score

    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.display.set_caption("First Move and Keys")

    font = pygame.font.SysFont('comicsans', 30, True)

    # Loop until the user clicks the close button.
    run = True

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Set positions of graphics
    background_position = [0, 0]

    # Cria os personagens
    man = Player(200, 410, 64, 64)
    goblin = Enemy(100, 410, 64, 64, 450)

    # Cria os projéteis
    bullets = []
    shootLoop = 0
    score = 0

    # -------- Main Program Loop -----------
    while run:
        # --- Main event loop
        #pygame.time.delay(100)

        if goblin.visible == True:
            if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                    man.hit()
                    score -= 5

        if shootLoop > 0:
            shootLoop += 1
        if shootLoop > 3:
            shootLoop = 0

        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

        # Controle da lista de bullets
        for bullet in bullets:
            if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > \
                    goblin.hitbox[1]:
                if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + \
                        goblin.hitbox[2]:
                    hitSound.play()
                    goblin.hit()
                    score += 1
                    bullets.pop(bullets.index(bullet))

            if bullet.x < WINDOWWIDTH and bullet.x > 0:
                bullet.x += bullet.vel  # Moves the bullet
            else:
                bullets.pop(bullets.index(bullet))  # Remove os bullets off the screen

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and shootLoop == 0:
            bulletSound.play()
            if man.left:
                facing = -1
            else:
                facing = 1

            if len(bullets) < 5:  # This will make sure we cannot exceed 5 bullets on the screen at once
                bullets.append(Projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0, 0), facing))

            shootLoop = 1

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
