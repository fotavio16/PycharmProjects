"""
Exemplo de Jogo com Python/Pygame Programs
Baseado no site:
http://programarcadegames.com/
http://simpson.edu/computer-science/

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
LARG_BORDA = 15


class Wall(pygame.sprite.Sprite):
    ''' Esta classe representa a barra retangular
     que é usada como parede ou borda nas Salas. '''

    def __init__(self, x, y, width, height, color):
        # Chama o construtor pai
        super().__init__()

        # Cria uma superfície retangular, do tamanho
        # e cor especificado nos parâmetros
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Posiciona o retângulo nas coordenadas passadas
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Block(pygame.sprite.Sprite):
    '''
    Esta classe representa um bloco.
    O bloco pode ser qualquer objeto do jogo.
    Deriva da classe 'Sprite'
    '''

    def __init__(self, cor, width, height, vel_max):
        # Chama a classe pai do construtor
        super().__init__()

        # Cria a imagem do bloco
        self.image = pygame.Surface([width, height])
        #self.image = pygame.image.load(filename).convert()
        self.image.fill(cor)

        # Cria o retângulo com as dimensões da imagem
        self.rect = self.image.get_rect()

        # Cria as velocidades
        self.vel_max = vel_max
        self.dx = random.randint(-self.vel_max, self.vel_max)
        self.dy = random.randint(-self.vel_max, self.vel_max)

    def update(self):
        """ Roda automaticamente quando atualiza as listas de blocos. """
        self.rect.x += self.dx
        self.rect.y += self.dy
        # Verifica se o bloco atingiu a borda
        if self.rect.x < LARG_BORDA:
            self.rect.x = LARG_BORDA
        if self.rect.x > WINDOWWIDTH - LARG_BORDA - self.rect.width:
            self.rect.x = WINDOWWIDTH - LARG_BORDA - self.rect.width
        if self.rect.y < LARG_BORDA:
            self.rect.y = LARG_BORDA
        if self.rect.y > WINDOWHEIGHT - LARG_BORDA - self.rect.height:
            self.rect.y = WINDOWHEIGHT - LARG_BORDA - self.rect.height

        if self.vel_max != 0:
            self.dx = random.randint(-self.vel_max, self.vel_max)
            self.dy = random.randint(-self.vel_max, self.vel_max)


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
        self.image.fill(BLUE)

        # Posiciona o retângulo nas coordenadas passadas
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def changespeed(self, x1, y1):
        """ Muda a velocidade do jogador. Chamado com um pressionamento de tecla. """
        self.change_x += x1
        self.change_y += y1

    def update(self, walls):
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

    def __init__(self, cor):
        """ Construtor. """
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.good_sprites = pygame.sprite.Group()
        self.bad_sprites = pygame.sprite.Group()
        self.all_sprite_list = pygame.sprite.Group()

        # Cria as paredes - (x_pos, y_pos, width, height)
        # EsqSup, EsqInf, DirSup, DirInf, CentSup, CentInf
        walls = [[0, 0, 15, 250],
                 [0, 350, 15, 250],
                 [785, 0, 15, 250],
                 [785, 350, 15, 250],
                 [15, 0, 770, 15],
                 [15, 585, 770, 15]
                 ]

        # Faz um loop pela lista.
        # Cria a parede e adiciona à lista
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], cor)
            self.wall_list.add(wall)


class Room1(Room):
    ''' Cria as paredes no quarto 1'''

    def __init__(self, cor):
        super().__init__(cor)

        # Cria as paredes - (x_pos, y_pos, width, height)
        # EsqSup, EsqInf, DirSup, DirInf, CentSup, CentInf
        walls = [[265, 65, 15, 520, BLUE],
                 [530, 15, 15, 520, BLUE]
                 ]

        # Faz um loop pela lista.
        # Cria a parede e adiciona à lista
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        # Cria os Good Sprites
        for i in range(20):
            #bloco = Block('gold_bar.png', 20, 15)
            bloco = Block(YELLOW, 20, 15, 0)

            bloco.rect.x = random.randrange(15, WINDOWWIDTH - 35)
            bloco.rect.y = random.randrange(15, WINDOWHEIGHT - 30)

            # Adiciona às listas de objetos
            self.good_sprites.add(bloco)
            self.all_sprite_list.add(bloco)


        # Cria os Bad Sprites
        for i in range(15):
            #bloco = Block('poison-30x30.png', 20, 15)
            bloco = Block(RED, 20, 15, 1)

            bloco.rect.x = random.randrange(15, WINDOWWIDTH - 35)
            bloco.rect.y = random.randrange(15, WINDOWHEIGHT - 30)

            # Adiciona às listas de objetos
            self.bad_sprites.add(bloco)
            self.all_sprite_list.add(bloco)


class Room2(Room):
    ''' Cria as paredes no quarto 2'''

    def __init__(self, cor):
        super().__init__(cor)

        # Cria as paredes - (x_pos, y_pos, width, height)
        walls = [[155, 15, 15, 520, DARK_GREEN],
                 [315, 15, 15, 185, DARK_GREEN],
                 [315, 250, 15, 335, DARK_GREEN],
                 [480, 15, 15, 400, DARK_GREEN],
                 [480, 465, 15, 120, DARK_GREEN],
                 [640, 65, 15, 520, DARK_GREEN]
                 ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        # Cria os Good Sprites
        for i in range(20):
            #bloco = Block('gold_bar.png', 20, 15)
            bloco = Block(YELLOW, 20, 15, 0)

            bloco.rect.x = random.randrange(15, WINDOWWIDTH - 35)
            bloco.rect.y = random.randrange(15, WINDOWHEIGHT - 30)

            # Adiciona às listas de objetos
            self.good_sprites.add(bloco)
            self.all_sprite_list.add(bloco)

        # Cria os Bad Sprites
        for i in range(20):
            #bloco = Block('poison-30x30.png', 20, 15)
            bloco = Block(RED, 20, 15, 2)

            bloco.rect.x = random.randrange(15, WINDOWWIDTH - 35)
            bloco.rect.y = random.randrange(15, WINDOWHEIGHT - 30)

            # Adiciona às listas de objetos
            self.bad_sprites.add(bloco)
            self.all_sprite_list.add(bloco)

class Room3(Room):
    ''' Cria as paredes no quarto 3'''

    def __init__(self, cor):
        super().__init__(cor)

        for x in range(100, 800, 100):
            for y in range(15, 451, 325):
                wall = Wall(x, y, 15, 245, RED)
                self.wall_list.add(wall)

        for x in range(150, 700, 100):
            wall = Wall(x, 150, 15, 300, WHITE)
            self.wall_list.add(wall)

        # Cria os Good Sprites
        for i in range(30):
            #bloco = Block('gold_bar.png', 20, 15)
            bloco = Block(YELLOW, 20, 15, 1)

            bloco.rect.x = random.randrange(15, WINDOWWIDTH - 35)
            bloco.rect.y = random.randrange(15, WINDOWHEIGHT - 30)

            # Adiciona às listas de objetos
            self.good_sprites.add(bloco)
            self.all_sprite_list.add(bloco)

        # Cria os Bad Sprites
        for i in range(30):
            #bloco = Block('poison-30x30.png', 20, 15)
            bloco = Block(RED, 20, 15, 2)

            bloco.rect.x = random.randrange(15, WINDOWWIDTH - 35)
            bloco.rect.y = random.randrange(15, WINDOWHEIGHT - 30)

            # Adiciona às listas de objetos
            self.bad_sprites.add(bloco)
            self.all_sprite_list.add(bloco)

class Room4(Room):
    ''' Cria as paredes no quarto 1'''

    def __init__(self, cor):
        super().__init__(cor)

        # Cria as paredes - (x_pos, y_pos, width, height)
        walls = [[200, 15, 15, 450, YELLOW],
                 [200, 495, 15, 90, YELLOW],
                 [300, 15, 15, 175, YELLOW],
                 [300, 220, 15, 365, YELLOW],
                 [400, 15, 15, 335, YELLOW],
                 [400, 380, 15, 205, YELLOW],
                 [600, 15, 15, 50, YELLOW],
                 [600, 95, 15, 490, YELLOW],
                 ]

        # Faz um loop pela lista.
        # Cria a parede e adiciona à lista
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        # Cria os Good Sprites
        for i in range(30):
            #bloco = Block('gold_bar.png', 20, 15)
            bloco = Block(YELLOW, 20, 15, 1)

            bloco.rect.x = random.randrange(15, WINDOWWIDTH - 35)
            bloco.rect.y = random.randrange(15, WINDOWHEIGHT - 30)

            # Adiciona às listas de objetos
            self.good_sprites.add(bloco)
            self.all_sprite_list.add(bloco)

        # Cria os Bad Sprites
        for i in range(40):
            #bloco = Block('poison-30x30.png', 20, 15)
            bloco = Block(RED, 20, 15, 3)

            bloco.rect.x = random.randrange(15, WINDOWWIDTH - 35)
            bloco.rect.y = random.randrange(15, WINDOWHEIGHT - 30)

            # Adiciona às listas de objetos
            self.bad_sprites.add(bloco)
            self.all_sprite_list.add(bloco)

class Game(object):
    '''
    Esta Classe representa o modelo de um jogo.
    Cada novo jogo será uma nova instancia desta classe.
    '''

    def __init__(self):
        ''' Construtor que inicializa os atributos do jogo.'''

        self.score = 0
        self.game_over = False

        # Aqui são criadas as listas de Sprites
        self.block_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
        self.movingsprites = pygame.sprite.Group()

        # Cria o jogador e adiciona nas listas de sprites
        self.player = Player(50, 50)
        self.movingsprites.add(self.player)

        # Cria as Salas do jogo
        self.rooms = []
        room = Room1(GRAY)
        self.rooms.append(room)
        room = Room2(RED)
        self.rooms.append(room)
        room = Room3(PURPLE)
        self.rooms.append(room)
        room = Room4(ORANGE)
        self.rooms.append(room)
        self.current_room_no = 0
        self.current_room = self.rooms[self.current_room_no]

    def process_events(self):
        ''' Processa os eventos do jogo.
        :return: Retorna True se for fechada a tela.
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(-5, 0)
                if event.key == pygame.K_RIGHT:
                    self.player.changespeed(5, 0)
                if event.key == pygame.K_UP:
                    self.player.changespeed(0, -5)
                if event.key == pygame.K_DOWN:
                    self.player.changespeed(0, 5)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(5, 0)
                if event.key == pygame.K_RIGHT:
                    self.player.changespeed(-5, 0)
                if event.key == pygame.K_UP:
                    self.player.changespeed(0, 5)
                if event.key == pygame.K_DOWN:
                    self.player.changespeed(0, -5)

        return False

    def run_logic(self):
        '''
        Este método roda a cada frame do jogo.
        Atualiza as posições e checa por colisões.
        :return:
        '''
        if not self.game_over:
            # Movimenta as sprites
            self.all_sprites_list.update()
            self.current_room.all_sprite_list.update()

            self.player.update(self.current_room.wall_list)

            if self.player.rect.x < -15:
                if self.current_room_no == 0:
                    self.current_room_no = 3
                    self.current_room = self.rooms[self.current_room_no]
                    self.player.rect.x = 790
                elif self.current_room_no == 2:
                    self.current_room_no = 1
                    self.current_room = self.rooms[self.current_room_no]
                    self.player.rect.x = 790
                elif self.current_room_no == 3:
                    self.current_room_no = 2
                    self.current_room = self.rooms[self.current_room_no]
                    self.player.rect.x = 790
                else:
                    self.current_room_no = 0
                    self.current_room = self.rooms[self.current_room_no]
                    self.player.rect.x = 790

            if self.player.rect.x > 801:
                if self.current_room_no == 0:
                    self.current_room_no = 1
                    self.current_room = self.rooms[self.current_room_no]
                    self.player.rect.x = 0
                elif self.current_room_no == 1:
                    self.current_room_no = 2
                    self.current_room = self.rooms[self.current_room_no]
                    self.player.rect.x = 0
                elif self.current_room_no == 2:
                    self.current_room_no = 3
                    self.current_room = self.rooms[self.current_room_no]
                    self.player.rect.x = 0
                else:
                    self.current_room_no = 0
                    self.current_room = self.rooms[self.current_room_no]
                    self.player.rect.x = 0

            # Verifica se o jogador colidiu com algo
            good_blocks_hit_list = pygame.sprite.spritecollide(self.player, self.current_room.good_sprites, True)
            bad_blocks_hit_list = pygame.sprite.spritecollide(self.player, self.current_room.bad_sprites, True)

            # Procura por colisões
            for block in good_blocks_hit_list:
                self.score += 1
                print(self.score)
            for block in bad_blocks_hit_list:
                self.score -= 1
                print(self.score)
            # You can do something with "block" here.

            #if len(self.block_list) == 0:
            #    self.game_over = True

    def display_frame(self, screen):
        ''' Atualiza a tela. '''
        screen.fill(BLACK)

        if self.game_over:
            # font = pygame.font.Font("Serif", 25)
            font = pygame.font.SysFont("serif", 25)
            text = font.render("Game Over, click to restart", True, BLACK)
            center_x = (WINDOWWIDTH // 2) - (text.get_width() // 2)
            center_y = (WINDOWHEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])

        if not self.game_over:
            # Desenha todos os objetos
            self.movingsprites.draw(screen)
            self.current_room.good_sprites.draw(screen)
            self.current_room.bad_sprites.draw(screen)
            self.all_sprites_list.draw(screen)
            self.current_room.wall_list.draw(screen)

        pygame.display.flip()




def main():
    ''' Inicializa Pygame e cria a janela. '''
    global clock, screen

    pygame.init()

    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.display.set_caption("Labirinto Louco")
    pygame.mouse.set_visible(False)

    # Cria os objetos e instancia o Jogo.
    done = False
    clock = pygame.time.Clock()
    jogo = Game()

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event processing
        # --- Processa os eventos (teclas, mouse clicks)
        done = jogo.process_events()

        # --- Atualiza as posições dos objetos e verifica colisões
        jogo.run_logic()

        # --- Desenha o frame atual
        jogo.display_frame(screen)

        # --- Limite de 60 frames por segundo
        clock.tick(FPS)


    # Close the window and quit.
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
