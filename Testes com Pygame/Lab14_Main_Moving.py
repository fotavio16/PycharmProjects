"""
 Pygame base template for opening a window


"""

import pygame, random, sys, math
from Lab14_block_library import *
from Lab14_goodblock_library import *
from Lab14_badblock_library import *

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

class Player(pygame.sprite.Sprite):
    ''' Classe do Jogador controlado por teclado. '''

    def __init__(self, filename, x, y):
        super().__init__()
        # Define a imagem com altura e largura
        #self.image = pygame.Surface([20, 20])
        self.image = pygame.image.load(filename).convert()
        #self.image.fill(cor)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Cria os atributos de velocidade
        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x1, y1):
        """ Altera a velocidade do jogador"""
        self.change_x += x1
        self.change_y += y1

    def update(self):
        """ Muda a posição do jogador. """
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.x < 0:
            bump_sound.play()
            self.rect.x = 0
        elif self.rect.x > WINDOWWIDTH - 20:
            self.rect.x = WINDOWWIDTH - 20
            bump_sound.play()
        if self.rect.y < 0:
            bump_sound.play()
            self.rect.y = 0
        elif self.rect.y > WINDOWHEIGHT - 20:
            bump_sound.play()
            self.rect.y = WINDOWHEIGHT - 20


def main():
    global clock, screen, bump_sound

    pygame.init()

    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.display.set_caption("Teste com Pygame - Classes em arquivos separados.")

    # Define a Fonte do Texto - Score
    font = pygame.font.SysFont('Calibri', 25, True, False)

    # Carrega os sons utilizados
    good_block_sound = pygame.mixer.Sound("good_block.wav")
    bad_block_sound = pygame.mixer.Sound("bad_block.wav")
    bump_sound = pygame.mixer.Sound("bump.wav")

    # Loop until the user clicks the close button.
    done = False

    # Cria a lista de blocos para controle de colisão
    block_list = pygame.sprite.Group()
    good_block_list = pygame.sprite.Group()
    bad_block_list = pygame.sprite.Group()

    # Cria a lista de todos os sprites para desenho
    all_sprites_list = pygame.sprite.Group()

    # Cria os Good Sprites
    for i in range(50):
        bloco = GoodBlock('gold_bar.png', 20, 15)

        bloco.rect.x = random.randrange(WINDOWWIDTH - 20)
        bloco.rect.y = random.randrange(WINDOWHEIGHT - 15)

        # Adiciona às listas de objetos
        good_block_list.add(bloco)
        all_sprites_list.add(bloco)

    # Cria os Bad Sprites
    for i in range(50):
        bloco = BadBlock('poison-30x30.png', 20, 15)

        bloco.rect.x = random.randrange(WINDOWWIDTH-20)
        bloco.rect.y = random.randrange(WINDOWHEIGHT-15)

        # Adiciona às listas de objetos
        bad_block_list.add(bloco)
        all_sprites_list.add(bloco)

    # Cria o jogador
    #player = Player(BLUE, int(WINDOWWIDTH/2), int(WINDOWHEIGHT/2))
    player = Player('emoji.jpg', int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))
    all_sprites_list.add(player)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    score = 0

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # Define a velocidade do jogador de acordo com tecla pressionada
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-3, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(3, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, -3)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, 3)

            # Quando a tecla é liberada a velocidade é retornada
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(3, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(-3, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, 3)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, -3)

        # Limpa a tela
        screen.fill(WHITE)

        all_sprites_list.update()

        # Verifica se o jogador colidiu com algo
        # O parâmetro True remove os sprite que colidiram
        good_blocks_hit_list = pygame.sprite.spritecollide(player, good_block_list, True)
        bad_blocks_hit_list = pygame.sprite.spritecollide(player, bad_block_list, True)

        # Checa a lista de colisões
        for block in good_blocks_hit_list:
            score += 1
            good_block_sound.play()

        for block in bad_blocks_hit_list:
            score -= 1
            bad_block_sound.play()


        # print(score)
        texto = font.render("Score: " + str(score), True, BLACK)
        screen.blit(texto, [WINDOWWIDTH-100, WINDOWHEIGHT-50])

        # Desenha todos os Sprites
        all_sprites_list.draw(screen)

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(FPS)

    # Close the window and quit.
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
