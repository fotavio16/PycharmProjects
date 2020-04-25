"""
 Pygame base template for opening a window


"""

import pygame, random, sys, math
from os import path

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
DARKGREY = (40, 40, 40)
ORANGE_SUN = (243, 130,  53)

# Set the width and height of the screen [width, height]
FPS = 60 # frames per second, the general speed of the program
WINDOWWIDTH = 512 # size of window's width in pixels - 16 * 32 or 32 * 16 or 64 * 8
WINDOWHEIGHT = 768 # size of windows' height in pixels - 16 * 48 or 32 * 24 or 64 * 12

TITLE = "Jogo da SENHA"
BGCOLOR = DARKGREY

TILESIZE = 32
GRIDWIDTH = WINDOWWIDTH / TILESIZE
GRIDHEIGHT = WINDOWHEIGHT / TILESIZE
LACUNAS = 6
RESULTADOS = 2
#DIGITOS = ['0','1','2','3','4','5','6','7','8','9']
DIGITOS = [0,1,2,3,4,5,6,7,8,9]



def draw_grid(screen):
    for x in range(0, WINDOWWIDTH, TILESIZE):
        pygame.draw.line(screen, LIGHT_GRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, TILESIZE):
        pygame.draw.line(screen, LIGHT_GRAY, (0, y), (WINDOWWIDTH, y))

def load_data():
    game_folder = path.dirname(__file__)
    map_data = []
    with open(path.join(game_folder, 'map_grid_01.txt'), 'rt') as f:
        for line in f:
            map_data.append(line)
    return map_data


class Borda(pygame.sprite.Sprite):
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
    def __init__(self, tecla, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        #self.image = pygame.image.load('0-icon.png').convert()
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        if tecla == 'E':
            self.valor = tecla
        elif tecla == '<':
            self.valor = tecla
        else:
            self.valor = int(tecla)
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.text = FONTE.render(tecla, True, NAVYBLUE)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.image.get_rect().center
        self.image.blit(self.text, self.text_rect)

class Display(pygame.sprite.Sprite):
    def __init__(self, contador, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.color = BLUE
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.fila = contador // LACUNAS
        self.coluna = contador % LACUNAS
        self.valor = ""

    def atualiza_valor(self, valor):
        self.image.fill(self.color)
        self.valor = valor
        self.text = FONTE.render(str(self.valor), True, YELLOW)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.image.get_rect().center
        self.image.blit(self.text, self.text_rect)

class Result(pygame.sprite.Sprite):
    def __init__(self, contador, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.color = WHITE
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.fila = contador // RESULTADOS
        self.coluna = contador % RESULTADOS
        self.valor = ''

    def atualiza_valor(self, valor):
        self.image.fill(self.color)
        self.valor = valor
        self.text = FONTE.render(str(self.valor), True, NAVYBLUE)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.image.get_rect().center
        self.image.blit(self.text, self.text_rect)

class Game(object):
    def __init__(self):
        ''' Construtor. Cria todas as propriedades do jogo. '''
        self.score = 0
        self.game_over = False
        self.fila_atual = 0
        self.coluna_atual = 0
        self.nova_tecla = False
        self.palpite = []
        self.corretos = 0
        self.foradepos = 0

        # Carrega o arquivo de mapa do jogo]
        self.map_data = load_data()

        # Cria as sprites lists
        self.all_sprites = pygame.sprite.Group()
        self.teclado_sprites = pygame.sprite.Group()
        self.display_sprites = pygame.sprite.Group()
        self.result_sprites = pygame.sprite.Group()
        self.final_sprites = pygame.sprite.Group()

        # Popula as sprites lists de acordo com o mapa
        cont_display = 0
        cont_result = 0
        cont_final = 0
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == 'B':
                    wall = Borda(col, row)
                    self.all_sprites.add(wall)
                elif tile == 'G':
                    bloco = Display(cont_display, col, row)
                    self.display_sprites.add(bloco)
                    cont_display += 1
                elif tile == 'R':
                    bloco = Result(cont_result, col, row)
                    self.result_sprites.add(bloco)
                    cont_result += 1
                elif tile == 'F':
                    bloco = Display(cont_final, col, row)
                    bloco.color = DARK_GREEN
                    self.final_sprites.add(bloco)
                    cont_final += 1
                if tile in 'E<0123456789':
                    tecla = Teclado(tile, col, row)
                    self.all_sprites.add(tecla)
                    self.teclado_sprites.add(tecla)
                    # print(f'posX = {tecla.x} e posY = {tecla.y}.')

        # Deixa visível a primeira fila de sprites display
        self.mostra_display()

        # Sorteia os números da SENHA
        self.senha = []
        for i in range(LACUNAS):
            indice = random.randrange(len(DIGITOS))
            self.senha.append(DIGITOS[indice])
            DIGITOS.pop(indice)
        print(f'Senha = {self.senha}')


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
                        #print(f'Tecla = {tecla.valor}')
                        self.nova_tecla = True
                        self.tecla = tecla


        return False

    def run_logic(self):
        """
        Este método roda cada vez através do frame.
        Ele atualiza as posições.
        """
        if not self.game_over:
            # Verifica se foi pressionada uma nova tecla
            if self.nova_tecla:
                # Identifica a tecla
                if self.tecla.valor == "E":
                    # Processa o ENTER
                    if len(self.palpite) == 6:
                        self.processa_palpite()
                        print(f'Palpite é {self.palpite}')
                        self.enche_result()
                        self.foradepos = 0
                        self.corretos = 0
                        self.coluna_atual = 0
                        self.fila_atual += 1
                        self.palpite = []
                        self.mostra_display()
                elif self.tecla.valor == '<':
                    # Processa a deleção
                    self.limpa_display()
                else: # É uma tecla numérica
                    self.enche_display()
                self.nova_tecla = False
            if self.fila_atual == 6:
                self.mostra_final()
                self.game_over = True

    def display_frame(self, screen):
        """ Faz o display de todos os componentes do jogo na tela. """

        # Limpa a tela
        screen.fill(BGCOLOR)

        # Desenha os blocos de sprites
        self.all_sprites.draw(screen)

        # Desenha a grade
        draw_grid(screen)

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    def mostra_display(self):
        ''' Inclui uma fileira de blocos de display na lista de sprites
        que serão exibidos. '''
        for bloco in self.display_sprites:
            if bloco.fila == self.fila_atual:
                bloco.atualiza_valor('')
                self.all_sprites.add(bloco)
        return

    def enche_display(self):
        ''' Processa a entrada de valores nos blocos do display atual'''
        # Se o display atual estiver cheio não aceita mais teclas numéricas
        if self.coluna_atual == LACUNAS:
            return
        for bloco in self.display_sprites:
            if bloco.fila == self.fila_atual and bloco.coluna == self.coluna_atual:
                bloco.atualiza_valor(self.tecla.valor)
        # Insere o valor na lista de palpites
        self.palpite.append(self.tecla.valor)
        self.coluna_atual += 1
        return

    def enche_result(self):
        ''' Armazena resultados nos blocos result'''
        for bloco in self.result_sprites:
            if bloco.fila == self.fila_atual and bloco.coluna == 0:
                bloco.atualiza_valor(self.corretos)
                self.all_sprites.add(bloco)
            if bloco.fila == self.fila_atual and bloco.coluna == 1:
                bloco.atualiza_valor(self.foradepos)
                self.all_sprites.add(bloco)
        return

    def limpa_display(self):
        ''' Limpa o último bloco do diaplay. '''
        # Impede valores negativos da coluna atual
        if self.coluna_atual > 0:
            self.coluna_atual -= 1
            # Faz a busca pelo bloco a ser limpo
            for bloco in self.display_sprites:
                if bloco.fila == self.fila_atual and bloco.coluna == self.coluna_atual:
                    bloco.atualiza_valor('')
            # Retira o valor da lista de palpites
            self.palpite.pop()
            print(f'Palpite é {self.palpite}')
        else:
            return

    def processa_palpite(self):
        ''' Calcula número de posições certas no palpite. '''
        # Compara self.senha com self.palpite
        for indSenha, valSenha in enumerate(self.senha):
            for indPalpite, valPalpite in enumerate(self.palpite):
                if valSenha == valPalpite:
                    self.corretos += 1
                    if indSenha != indPalpite:
                        self.corretos -= 1
                        self.foradepos += 1
        return

    def mostra_final(self):
        ''' Inclui os blocos do Final (Senha) na lista de sprites
        exibidos. '''
        painel1 = '#SENHA' # Texto do Título
        cont1 = 0 # Contador para o título
        cont2 = 0 # Contador para o display dos números da senha
        for bloco in self.final_sprites:
            if bloco.fila == 0:
                bloco.atualiza_valor(painel1[cont1])
                cont1 += 1
            elif bloco.fila == 1:
                bloco.atualiza_valor(self.senha[cont2])
                cont2 += 1

            self.all_sprites.add(bloco)

def main():
    global clock, screen, FONTE

    pygame.init()

    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.display.set_caption(TITLE)

    # Select the font to use, size, bold, italics
    FONTE = pygame.font.SysFont('Calibri', 25, True, False)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Create an instance of the Game class
    game = Game()

    # Exemplos de criação de displays e resultados
    '''
    cont = 1
    for bloco in game.display_sprites:
        if bloco.fila == 0:
            bloco.atualiza_valor(cont)
            game.all_sprites.add(bloco)
            cont += 1
    
    cont = 1
    for bloco in game.result_sprites:
        if bloco.fila == 0:
            bloco.atualiza_valor(cont)
            game.all_sprites.add(bloco)
            cont += 1

    for bloco in game.display_sprites:
        print(f'posX = {bloco.x} e posY = {bloco.y}.')
    '''

    # Cria um array 10 x 10
    grid = []
    for row in range(10):
        grid.append([])
        for col in range(10):
            grid[row].append(0)

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
