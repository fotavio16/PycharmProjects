"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/

http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
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


class Wall(pygame.sprite.Sprite):
    '''Esta classe representa a barra na parte inferior que o jogador controla'''

    def __init__(self, x, y, width, height, color):
        # Chama o construtor pai
        super().__init__()

        # Cria uma parede AZUL, do tamanho especificado nos parâmetros
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Posiciona o retângulo nas coordenadas passadas
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Player(pygame.sprite.Sprite):
    '''Esta classe representa a barra na parte inferior que o jogador controla'''

    # Cria o vetor de velocidade
    change_x = 0
    change_y = 0

    def __init__(self, x, y):
        # Chama o construtor pai
        super().__init__()

        # Cria a imagem como superfície
        self.image = pygame.Surface([15, 15])
        self.image.fill(WHITE)

        # Posiciona o retângulo nas coordenadas passadas
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def changespeed(self, x1, y1):
        """ Muda a velocidade do jogador. Chamado com um pressionamento de tecla. """
        self.change_x += x1
        self.change_y += y1

    def move(self, walls):
        ''' Define a nova posição do jogador. Chamado com um pressionamento de tecla. '''
        # Movimenta esquerda / direita
        self.rect.x += self.change_x

        # Verifica se o movimento causa colisão com a parede
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # Se estivermos nos movendo para a direita, defina nosso lado direito
            # para o lado esquerdo do item que atingimos
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Caso contrário, se estamos nos movendo para a esquerda,
                # faça o oposto.
                self.rect.left = block.rect.right

        # Movimenta acima / abaixo
        self.rect.y += self.change_y

        # Verifica se colidiu com algo
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:

            # Redefine a posição com base na parte superior / inferior do objeto.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom


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

    pygame.display.set_caption("Maze Runner")

    # Loop until the user clicks the close button.
    done = False

    # Cria o jogador e demais objetos do jogo
    player = Player(50, 50)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)

    rooms = []

    room = Room1()
    rooms.append(room)

    room = Room2()
    rooms.append(room)

    room = Room3()
    rooms.append(room)

    room = Room4()
    rooms.append(room)

    current_room_no = 0
    current_room = rooms[current_room_no]

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
                    player.changespeed(-5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)

        # --- Game Logic ---

        player.move(current_room.wall_list)

        if player.rect.x < -15:
            if current_room_no == 0:
                current_room_no = 3
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 2:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 3:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 790
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 790

        if player.rect.x > 801:
            if current_room_no == 0:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 1:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 2:
                current_room_no = 3
                current_room = rooms[current_room_no]
                player.rect.x = 0
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 0

        # Limpa a tela
        screen.fill(BLACK)

        # Desenha todos os objetos
        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(FPS)

    # Close the window and quit.
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
