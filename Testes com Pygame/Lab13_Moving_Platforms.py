"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/

http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
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
WINDOWWIDTH = 800 # size of window's width in pixels
WINDOWHEIGHT = 600 # size of windows' height in pixels


class Player(pygame.sprite.Sprite):
    '''Esta classe representa a barra na parte inferior que o jogador controla'''

    def __init__(self):
        # Chama o construtor pai
        super().__init__()

        # Cria a imagem como superfície.
        # Poderia ser uma imagem carregada.
        width = 40
        height = 60
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)

        # Posiciona o retângulo nas coordenadas passadas
        self.rect = self.image.get_rect()

        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        # List of sprites we can bump against
        self.level = None

    def update(self):
        """ Movimenta o jogador. """
        # Gravidade
        self.calc_grav()

        # Movimenta esquerda/direita
        self.rect.x += self.change_x

        # Verifica se colidiu com algo
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # Se está movendo a direita,
            # Configura o lado direito para o lado esquerdo do item que colidiu
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Caso contrário se está movendo a esquerda faz o oposto.
                self.rect.left = block.rect.right

        # Movimenta pra cima/para baixo
        self.rect.y += self.change_y

        # Verifica se colidiu com algo
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Configura a posição baseada no topo/base do objeto.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Zera a velocidade vertical
            self.change_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

    def calc_grav(self):
        """ Calcula o efeito da gravidade. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # Verifica se chegou ao solo.
        if self.rect.y >= WINDOWHEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = WINDOWHEIGHT - self.rect.height

    def jump(self):
        """ Acionada quando o usuário tecla o botão de 'jump'. """

        # Desce um pouco e verifica se há uma plataforma abaixo.
        # Move para baixo 2 pixels porque não funciona bem se apenas descer 1
        # ao trabalhar com uma plataforma em movimento.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # Se ok para o salto, define velocidade para cima
        if len(platform_hit_list) > 0 or self.rect.bottom >= WINDOWHEIGHT:
            self.change_y = -10

    # Player-controlled movement:
    def go_left(self):
        """ Quando pressionada tecla seta esquerda. """
        self.change_x = -6

    def go_right(self):
        """ Quando pressionada tecla seta direita. """
        self.change_x = 6

    def stop(self):
        """ Quando nada é pressionado. """
        self.change_x = 0


class Platform(pygame.sprite.Sprite):
    """ Plataforma Normal """

    def __init__(self, width, height):
        """ Platform constructor. """
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(DARK_BROWN)

        self.rect = self.image.get_rect()


class MovingPlatform(Platform):
    """ Esta é uma plataforma especial que pode se mover. """
    change_x = 0
    change_y = 0

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    player = None

    level = None

    def update(self):
        """ Movimenta a plataforma.
            Se o jogador estiver no caminho, ele empurrará o jogador
            para fora do caminho. Isso NÃO lida com o que acontece se
            uma plataforma empurrar um jogador para outro objeto.
            Certifique-se de plataformas móveis têm folga para empurrar
            o jogador ao redor ou adicionar código para lidar com o
            que acontece se não o fizerem. """

        # Movimenta esquerda/direita
        self.rect.x += self.change_x

        # Verifica se colidiu com o jogador
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # Nós atingimos o jogador. Empurrar o jogador e assumir
            # que ele não vai bater em mais nada. Se estivermos
            # nos movendo para a direita, defina nosso lado direito
            # para o lado esquerdo do item que atingimos
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                # Caso contrário se for para esquerda faça o oposto.
                self.player.rect.left = self.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Verifica se colidiu com o jogador
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # Nós atingimos o jogador. Empurrar o jogador e assumir
            # que ele não vai bater em mais nada.

            # Define a posição baseado no topo/base do objeto.
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        # Checa as bordas e se necessário inverter a direção.
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1


class Level(object):
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    def __init__(self, player):
        """ Esta é uma superclasse genérica usada para definir
        um nível. Crie uma classe filha para cada nível
        com informações específicas do nível. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

        # Imagem de fundo
        self.background = None

        # Quão longe este mundo pode ser rolado para a esquerda / direita
        self.world_shift = 0
        self.level_limit = -1000

    def update(self):
        """ Atualiza tudo neste nível."""
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """ Desenha tudo neste nível. """

        # O background
        screen.fill(BLUE)

        # Desenha todas as sprite_lists
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        """ Quando o usuário se move para a esquerda / direita
         e precisamos rolar tudo."""

        # Acompanhe o valor da rolagem
        self.world_shift += shift_x

        # Percorra todas as listas de sprites e move
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

# Cria as plataformas em cada nível
class Level_01(Level):
    """ Nível 1. """

    def __init__(self, player):
        """ Cria Nível 1. """

        # Chama o constructor Pai
        Level.__init__(self, player)

        self.level_limit = -1500

        # Array com as dimensões das plataformas.
        # (width, height, x, and y )
        level = [[210, 70, 500, 500],
                 [210, 70, 800, 400],
                 [210, 70, 1000, 500],
                 [210, 70, 1120, 280],
                 ]

        # Percorre o array acima e adiciona as platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        # Adiciona a moving platform
        block = MovingPlatform(70, 40)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


class Level_02(Level):
    """ Nível 2. """

    def __init__(self, player):
        """ Cria o Nível 1. """

        # Chama o constructor Pai
        Level.__init__(self, player)

        self.level_limit = -1000

        # Array com as dimensões das plataformas.
        # (width, height, x, and y )
        level = [[210, 70, 500, 550],
                 [210, 70, 800, 400],
                 [210, 70, 1000, 500],
                 [210, 70, 1120, 280],
                 ]

        # Percorre o array acima e adiciona as platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        # Adiciona a moving platform
        block = MovingPlatform(70, 70)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


class Room(object):
    ''' Classe Base para todas os quartos. '''
    # Cada quarto tem uma lista de paredes e de sprites inimigos
    wall_list = None
    enemy_sprites = None

    def __init__(self):
        """ Construtor. """
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()


class Room1(Room):
    ''' Cria as paredes no quarto 1'''

    def __init__(self):
        super().__init__()

        # Cria as paredes - (x_pos, y_pos, width, height)
        walls = [[0, 0, 20, 250, GRAY],
                 [0, 350, 20, 250, GRAY],
                 [780, 0, 20, 250, GRAY],
                 [780, 350, 20, 250, GRAY],
                 [20, 0, 760, 20, GRAY],
                 [20, 580, 760, 20, GRAY],
                 [390, 50, 20, 500, BLUE]
                 ]

        # Faz um loop pela lista.
        # Cria a parede e adiciona à lista
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room2(Room):
    ''' Cria as paredes no quarto 2'''

    def __init__(self):
        super().__init__()

        # Cria as paredes - (x_pos, y_pos, width, height)
        walls = [[0, 0, 20, 250, RED],
                 [0, 350, 20, 250, RED],
                 [780, 0, 20, 250, RED],
                 [780, 350, 20, 250, RED],
                 [20, 0, 760, 20, RED],
                 [20, 580, 760, 20, RED],
                 [190, 50, 20, 500, DARK_GREEN],
                 [590, 50, 20, 500, DARK_GREEN]
                 ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room3(Room):
    ''' Cria as paredes no quarto 3'''

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, PURPLE],
                 [0, 350, 20, 250, PURPLE],
                 [780, 0, 20, 250, PURPLE],
                 [780, 350, 20, 250, PURPLE],
                 [20, 0, 760, 20, PURPLE],
                 [20, 580, 760, 20, PURPLE]
                 ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        for x in range(100, 800, 100):
            for y in range(50, 451, 300):
                wall = Wall(x, y, 20, 200, RED)
                self.wall_list.add(wall)

        for x in range(150, 700, 100):
            wall = Wall(x, 200, 20, 200, WHITE)
            self.wall_list.add(wall)


class Room4(Room):
    ''' Cria as paredes no quarto 1'''

    def __init__(self):
        super().__init__()

        # Cria as paredes - (x_pos, y_pos, width, height)
        walls = [[0, 0, 20, 250, ORANGE],
                 [0, 350, 20, 250, ORANGE],
                 [780, 0, 20, 250, ORANGE],
                 [780, 350, 20, 250, ORANGE],
                 [20, 0, 760, 20, ORANGE],
                 [20, 580, 760, 20, ORANGE],
                 [300, 20, 20, 170, YELLOW],
                 [300, 220, 20, 360, YELLOW],
                 [400, 20, 20, 330, YELLOW],
                 [400, 380, 20, 200, YELLOW],
                 ]

        # Faz um loop pela lista.
        # Cria a parede e adiciona à lista
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)



def main():
    global clock, screen

    pygame.init()

    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.display.set_caption("Plataforma com movimento")

    # Loop until the user clicks the close button.
    done = False

    # Cria o jogador e demais objetos do jogo
    player = Player()
    # Cria os níveis
    level_list = []
    level_list.append(Level_01(player))
    level_list.append(Level_02(player))

    # Define nível atual
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
    # Define a posição inicial do jogador
    player.rect.x = 340
    player.rect.y = WINDOWHEIGHT - player.rect.height
    active_sprite_list.add(player)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    score = 0

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        # --- Game Logic ---

        # Atualiza o jogador.
        active_sprite_list.update()

        # Atualiza o nível atual
        current_level.update()

        # Se o jogador se aproximar do lado direito,
        # rola o mundo para a esquerda (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)

        # Se o jogador se aproximar do lado esquerdo,
        # rola o mundo para a direita (+x)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)

        # Se o jogador chegar ao final do nível, vá para o próximo nível:
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            if current_level_no < len(level_list) - 1:
                player.rect.x = 120
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
            else:
                    # Fora dos níveis Isso apenas sai do programa.
                    # Você vai querer fazer algo melhor.
                done = True

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(FPS)

    # Close the window and quit.
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
