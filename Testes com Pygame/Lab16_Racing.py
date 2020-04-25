'''
    Programa de uma corrida usando grids

'''

import pygame, random, sys, math
from os import path

# Definição das Cores
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
DARKGREY = (40, 40, 40)
ORANGE_SUN = (243, 130,  53)

# Definição de Constantes do Jogo.
# Largura e altura da Tela, cores e tamanho do grid
FPS = 60 # frames per second, the general speed of the program
WINDOWWIDTH = 1280 # size of window's width in pixels - 40 * 32 or 80 * 16
WINDOWHEIGHT = 768 # size of windows' height in pixels - 24 * 32 or 48 * 16

TITLE = "Corrida NASCAR"
BGCOLOR = DARK_SPRING_GREEN

TILESIZE = 32
GRIDWIDTH = WINDOWWIDTH / TILESIZE
GRIDHEIGHT = WINDOWHEIGHT / TILESIZE
#DIRECTIONS = [['D',18], ['S',21], ['E',26], ['N',21], ['D',8]]
DIRECTIONS = [['D',17], ['S',21], ['E',26], ['N',21], ['D',9]]
CARROS = [
    ['Porsche 911', 'Fernando Fonseca', BLUE],
    ['Ferrari F430', 'Giles Vileneuve', RED],
    ['Lamborghini Gallardo', 'Juan Manuel Fangio', ORANGE_SUN],
    ['McLaren 720S', 'Alain Prost', GREEN]
]

PILOTOS = ['Jackie Stewart', 'Jim Clark', 'Niki Lauda', 'Nelson Piquet', 'Nigel Mansell', 'Ayrton Senna', 'Michael Schumacher']
CARS = ['Mercedes W196', 'Gulf/Mirage Ford GT40', 'Porsche 917',
        'Lola T330', 'Porsche 956', 'McLaren F1 GTR', 'Audi R8', ]
DISTVOLTA = 94
POSINICIAL = 94
POSFINAL = POSINICIAL - len(CARROS)
TOTALVOLTAS = 60


def draw_grid(screen):
    for x in range(0, WINDOWWIDTH, TILESIZE):
        pygame.draw.line(screen, LIGHT_GRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, TILESIZE):
        pygame.draw.line(screen, LIGHT_GRAY, (0, y), (WINDOWWIDTH, y))

def load_data():
    game_folder = path.dirname(__file__)
    map_data = []
    with open(path.join(game_folder, 'map_circuito_01.txt'), 'rt') as f:
        for line in f:
            map_data.append(line)
    return map_data

class Status(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(NAVYBLUE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Teclado(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Pista(pygame.sprite.Sprite):
    def __init__(self, contador, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(DARKGREY)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.seq = contador # Estabelece o sequencial do bloco da pista.
        self.ocupada = False
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Carro(pygame.sprite.Sprite):
    def __init__(self, modelo, piloto, cor):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(cor)
        self.rect = self.image.get_rect()
        self.modelo = modelo
        self.piloto = piloto
        self.x = 0
        self.y = 0
        self.dist = 0
        self.voltas = 0
        self.rect.x = 0
        self.rect.y = 0

    def calcDistancia(self, delta):
        if self.dist + delta > DISTVOLTA:
            return self.dist + delta - DISTVOLTA
        else:
            return self.dist + delta

    def update(self, valor):
        self.dist = valor
        return

class Game(object):
    def __init__(self):
        ''' Construtor. Cria todas as propriedades do jogo. '''
        self.score = 0
        self.game_over = False
        self.nova_tecla = False

        # Carrega o arquivo de mapa do jogo]
        self.map_data = load_data()

        # Cria as sprites lists
        self.all_sprites = pygame.sprite.Group()
        self.pista_sprites = pygame.sprite.Group()
        #self.carros_sprites = pygame.sprite.Group()
        self.carros_sprites = []
        self.teclado_sprites = pygame.sprite.Group()

        # Popula as sprites lists de acordo com o mapa
        cont_pista = 0
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == 'B':
                    wall = Status(col, row)
                    self.all_sprites.add(wall)
                elif tile == 'T':
                    bloco = Pista(cont_pista, col, row)
                    self.pista_sprites.add(bloco)
                    self.all_sprites.add(bloco)
                    cont_pista += 1
                if tile == 'C':
                    tecla = Teclado(col, row)
                    self.all_sprites.add(tecla)
                    self.teclado_sprites.add(tecla)

        # Sequencia os blocos da pista
        posAtual = [10,1]
        contador = 1
        for coord in DIRECTIONS:
            for i in range(coord[1]):
                for bloco in self.pista_sprites:
                    if bloco.x == posAtual[0] and bloco.y == posAtual[1]:
                        print(f'{posAtual} - seq: {contador}')
                        bloco.seq = contador
                        contador += 1
                if coord[0] == 'D':
                    posAtual[0] += 1
                elif coord[0] == 'S':
                    posAtual[1] += 1
                elif coord[0] == 'E':
                    posAtual[0] -= 1
                else: # Direção Norte
                    posAtual[1] -= 1


        # Cria um carro
        self.criaCarro()


    def process_events(self):
        """ Processa todos os eventos.
            Retorna "True" se for para fechar a janela do jogo. """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Pega a posição do mouse
                pos = pygame.mouse.get_pos()
                posX = pos[0] // TILESIZE
                posY = pos[1] // TILESIZE
                for tecla in self.teclado_sprites:
                    if tecla.x == posX and tecla.y == posY:
                        self.nova_tecla = True

        return False

    def run_logic(self):
        """
        Este método roda cada vez através do frame.
        Ele atualiza as posições.
        """
        if not self.game_over:
            # Verifica se foi pressionada uma nova tecla
            if self.nova_tecla:
                # Teste com o carro
                self.posicionaCarros()
                self.nova_tecla = False
                self.atualizaClassificação()
            if 1 == 6:
                self.game_over = True

    def display_frame(self, screen):
        """ Faz o display de todos os componentes do jogo na tela. """

        # Limpa a tela
        screen.fill(BGCOLOR)

        # Desenha os blocos de sprites
        self.all_sprites.draw(screen)

        # Imprime a Classificação
        self.mostraClassificação()

        # Desenha a grade
        #draw_grid(screen)

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    def criaCarro(self):
        #self.classifica = []
        posTemp = POSINICIAL
        while posTemp > POSFINAL:
            for bloco in self.pista_sprites:
                if bloco.seq == posTemp:
                    bloco.ocupada = True
                    car = Carro(CARROS[94 - posTemp][0],CARROS[94 - posTemp][1],CARROS[94 - posTemp][2])
                    car.rect.x = bloco.rect.x
                    car.rect.y = bloco.rect.y
                    car.dist = posTemp
                    self.all_sprites.add(car)
                    self.carros_sprites.append(car)
                    #print(f'{car.modelo} - {car.dist}')

            posTemp -= 1

    def posicionaCarros(self):
        for i in range(len(self.carros_sprites)):
            car = self.carros_sprites[i]
            distAtual = car.dist
            for bloco in self.pista_sprites:
                if bloco.seq == distAtual:
                    blocoAtual = bloco
            distNova = car.calcDistancia(random.randint(1, 5))

            achei = False
            passLoop = 0
            while not achei:
                passLoop += 1
                if passLoop > 10: break
                print(f'PasseiLoop : {passLoop}')
                for blocoNovo in self.pista_sprites:
                    if blocoNovo.seq == distNova:
                        if blocoNovo.ocupada == True:
                            distNova -= 1
                        else:
                            achei = True
                            blocoAtual.ocupada = False
                            blocoNovo.ocupada = True
                            car.update(distNova)
                            if distAtual > distNova:
                                car.voltas += 1
                            car.rect.x = blocoNovo.rect.x
                            car.rect.y = blocoNovo.rect.y

    def atualizaClassificação(self):
        #self.classifica.sort(key=lambda x: x[0].dist, reverse=True)
        #self.classifica = sorted(self.classifica, key=self.classifica[0].dist, reverse=True)
        n = len(self.carros_sprites)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.carros_sprites[j].voltas < self.carros_sprites[j+1].voltas:
                    self.carros_sprites[j], self.carros_sprites[j + 1] = self.carros_sprites[j + 1], self.carros_sprites[j]
                elif self.carros_sprites[j].voltas == self.carros_sprites[j+1].voltas:
                    if self.carros_sprites[j].dist < self.carros_sprites[j+1].dist:
                        self.carros_sprites[j], self.carros_sprites[j+1] = self.carros_sprites[j+1], self.carros_sprites[j]

    def mostraClassificação(self):
        voltaLider = self.carros_sprites[0].voltas
        distLider = self.carros_sprites[0].dist
        texto = 'Volta: ' + str(voltaLider) + ' de ' + str(TOTALVOLTAS)
        self.text = FONTE.render(texto, True, SKY_BLUE)
        self.text_rect = self.text.get_rect()
        self.text_rect = ((1000), (20))
        screen.blit(self.text, self.text_rect)
        for i, car in enumerate(self.carros_sprites):
            difLider = (voltaLider - car.voltas)*DISTVOLTA + distLider - car.dist
            texto = car.piloto + ' - ' + car.modelo + ' : ' + str(difLider)
            self.text = FONTE.render(texto, True, YELLOW)
            self.text_rect = self.text.get_rect()
            self.text_rect = ((1000),(i * 20 + 40))
            screen.blit(self.text, self.text_rect)

def main():
    global clock, screen, FONTE

    pygame.init()

    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.display.set_caption(TITLE)

    # Select the font to use, size, bold, italics
    FONTE = pygame.font.SysFont('Calibri', 14, True, False)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Create an instance of the Game class
    game = Game()

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop

        # Process events (keystrokes, mouse clicks, etc)
        done = game.process_events()

        # Update object positions, check for collisions
        game.run_logic()

        # Draw the current frame
        game.display_frame(screen)

        # --- Limit to 60 frames per second
        clock.tick(FPS)

    # Close the window and quit.
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()

