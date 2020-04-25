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


class Block(pygame.sprite.Sprite):
    '''
    Esta classe representa a bola.
    Deriva da classe 'Sprite'
    '''

    def __init__(self, color, width, height):
        # Chama a classe pai do construtor
        super().__init__()

        # Cria a imagem do bloco
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Cria o retângulo com as dimensões da imagem
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 1
        if self.rect.y > WINDOWHEIGHT:
            self.rect.y = random.randrange(-100, -10)
            self.rect.x = random.randrange(0, WINDOWWIDTH-20)

def main():
    global clock, screen

    pygame.init()

    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.display.set_caption("Teste com Sprites em Pygame")

    # Loop until the user clicks the close button.
    done = False

    # Cria a lista de blocos para controle de colisão
    block_list = pygame.sprite.Group()

    # Cria a lista de todos os sprites para desenho
    all_sprites_list = pygame.sprite.Group()

    # Cria todos os blocos
    for i in range(50):
        bloco = Block(BLACK, 20, 15)

        bloco.rect.x = random.randrange(WINDOWWIDTH-20)
        bloco.rect.y = random.randrange(WINDOWHEIGHT-15)

        # Adiciona às listas de objetos
        block_list.add(bloco)
        all_sprites_list.add(bloco)

    # Cria o jogador
    player = Block(RED, 20, 15)
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

        # Limpa a tela
        screen.fill(WHITE)

        # Obtêm a posição do mouse
        pos = pygame.mouse.get_pos()

        # Define a posição do jogador de acordo com a posição do mouse
        player.rect.x = pos[0]
        player.rect.y = pos[1]

        # Verifica se o jogador colidiu com algo
        # O parâmetro True remove os sprite que colidiram
        blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

        # Checa a lista de colisões
        for block in blocks_hit_list:
            score += 1
            print(score)

        # Atualiza os blocos
        block_list.update()

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
