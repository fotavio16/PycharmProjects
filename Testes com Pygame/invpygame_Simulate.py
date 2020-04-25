'''
    Simulate (a Simon clone) ou Genius
    http://inventwithpython.com/pygame

'''

import pygame, random, sys, time
from pygame.locals import *

# Definição das Cores
#            R    G    B
BLACK    = (  0,   0,   0)
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
BRIGHTRED = (255,   0,   0)
RED      = (155,   0,   0)
BRIGHTGREEN = (  0, 255,   0)
GREEN    = (  0, 155,   0)
BRIGHTBLUE = (  0,   0, 255)
BLUE     = (  0,   0, 155)
BRIGHTYELLOW = (255, 255,   0)
YELLOW   = (155, 155,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
SKY_BLUE = (135, 206, 235)
DARK_GREEN = (  0, 100,   0)
DARK_SPRING_GREEN = ( 23, 114,  69)
DARK_BROWN = (101,  67,  33)
LIGHT_GRAY = (211, 211, 211)
DARKGRAY = (40, 40, 40)
ORANGE_SUN = (243, 130,  53)

# Definição de Constantes do Jogo.
# Largura e altura da Tela, cores e tamanho do grid
FPS = 30 # frames per second, the general speed of the program
WINDOWWIDTH = 640 # size of window's width in pixels
WINDOWHEIGHT = 480 # size of windows' height in pixels

TITLE = "SIMULATE"
FLASHSPEED = 500 # em milesegundos
FLASHDELAY = 200 # em milesegundos
BUTTONSIZE = 200
BUTTONGAPSIZE = 20
TIMEOUT = 4 # segundos antes de gameover
XMARGIN = int((WINDOWWIDTH - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)
YMARGIN = int((WINDOWHEIGHT - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)
bgColor = BLACK

# Objetos retângulos para cada um dos quatro botões
YELLOWRECT = pygame.Rect(XMARGIN, YMARGIN, BUTTONSIZE, BUTTONSIZE)
BLUERECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN, BUTTONSIZE, BUTTONSIZE)
REDRECT = pygame.Rect(XMARGIN, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
GREENRECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)


class Game(object):
    def __init__(self):
        ''' Construtor. Cria todas as propriedades do jogo. '''
        # Inicializa algumas variáveis para um novo jogo
        self.score = 0
        self.pattern = []  # Armazena o padrão de cores
        self.currentStep = 0  # Próxima cor que deve ser escolhida pelo jogador
        self.lastClickTime = 0  # Tempo decorrido desde a última jogada

        self.waitingForInput = False  # Quando Falso o jogo segue,
        # quando Verdadeiro espera o click num dos botões coloridos

        # Define o texto básico
        self.infoSurf = BASICFONT.render('Repita o padrão clicando no botão ou usando as teclas Q, W, A, S.', 1, DARKGRAY)
        self.infoRect = infoSurf.get_rect()
        self.infoRect.topleft = (10, WINDOWHEIGHT - 25)

    def process_events(self):
        """ Processa todos os eventos.
            Retorna "True" se for para fechar a janela do jogo. """

        self.clickedButton = None  # Botão que foi clicado
        # (marcado para YELLOW, RED, GREEN ou BLUE)

        checkForQuit()
        for event in pygame.event.get():
            #if event.type == pygame.QUIT:
            #    return True
            if event.type == MOUSEBUTTONUP:
                # Pega a posição do mouse
                mousex, mousey = event.pos
                self.clickedButton = getButtonClicked(mousex, mousey)
            elif event.type == KEYDOWN:
                if event.key == K_q:
                    self.clickedButton = YELLOW
                elif event.key == K_w:
                    self.clickedButton = BLUE
                elif event.key == K_a:
                    self.clickedButton = RED
                elif event.key == K_s:
                    self.clickedButton = GREEN

        return False

    def run_logic(self):
        """
        Este método roda cada vez através do frame.
        Ele atualiza as posições.
        """
        if not self.waitingForInput:
            # Roda o Padrão de Cores
            pygame.display.update()
            pygame.time.wait(1000)
            self.pattern.append(random.choice((YELLOW, BLUE, RED, GREEN)))
            for button in self.pattern:
                flashButtonAnimation(button)
                pygame.time.wait(FLASHDELAY)
            self.waitingForInput = True
        else:
            # Espera o jogador apertar os botões
            if self.clickedButton and self.clickedButton == self.pattern[self.currentStep]:
                # Apertou o botão correto
                flashButtonAnimation(self.clickedButton)
                self.currentStep += 1
                self.lastClickTime = time.time()
                if self.currentStep == len(self.pattern):
                    # Apertou o último botão da sequência
                    self.changeBackgroundAnimation()
                    self.score += 1
                    self.waitingForInput = False
                    self.currentStep = 0 # Volta ao ínício
            elif (self.clickedButton and self.clickedButton != self.pattern[self.currentStep]) or (self.currentStep != 0 and time.time() - TIMEOUT > self.lastClickTime):
                # Apertou o botão errado, ou chegou no timeout
                gameOverAnimation()
                # Reseta as variáveis para um novo jogo:
                self.pattern = []
                self.currentStep = 0
                self.waitingForInput = False
                self.score = 0
                pygame.time.wait(1000)
                self.changeBackgroundAnimation()


    def display_frame(self, screen):
        """ Faz o display de todos os componentes do jogo na tela. """

        # Limpa a tela
        SCREEN.fill(bgColor)
        drawButtons()

        scoreSurf = BASICFONT.render('Score: ' + str(score), 1, WHITE)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (WINDOWWIDTH - 100, 10)
        SCREEN.blit(scoreSurf, scoreRect)

        SCREEN.blit(self.infoSurf, self.infoRect)

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.update()


    def changeBackgroundAnimation(self, animationSpeed=40):
        global bgColor
        newBgColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        newBgSurf = pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT))
        newBgSurf = newBgSurf.convert_alpha()
        r, g, b = newBgColor
        for alpha in range(0, 255, animationSpeed):  # Loop de Animação
            checkForQuit()
            SCREEN.fill(bgColor)

            newBgSurf.fill((r, g, b, alpha))
            SCREEN.blit(newBgSurf, (0, 0))

            drawButtons()  # Redesenha os botões no topo da tela

            pygame.display.update()
            FPSCLOCK.tick(FPS)
        bgColor = newBgColor

    def gameOverAnimation(self, color=WHITE, animationSpeed=50):
        # Toca todos os beeps de uma vez, então pisca o fundo da tela
        origSurf = SCREEN.copy()
        flashSurf = pygame.Surface(SCREEN.get_size())
        flashSurf = flashSurf.convert_alpha()
        BEEP1.play()
        BEEP2.play()
        BEEP3.play()
        BEEP4.play()
        r, g, b = color



def main():
    global FPSCLOCK, SCREEN, BASICFONT, BEEP1, BEEP2, BEEP3, BEEP4

    pygame.init()

    SCREEN = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.display.set_caption(TITLE)

    # Select the font to use, size, bold, italics
    BASICFONT = pygame.font.Font('freesansbold.ttf', 16)

    # Carregue os arquivos de som
    BEEP1 = pygame.mixer.Sound('beep1.ogg')
    BEEP2 = pygame.mixer.Sound('beep2.ogg')
    BEEP3 = pygame.mixer.Sound('beep3.ogg')
    BEEP4 = pygame.mixer.Sound('beep4.ogg')

    # Used to manage how fast the screen updates
    FPSCLOCK = pygame.time.Clock()

    # Create an instance of the Game class
    game = Game()

    # Loop until the user clicks the close button.
    done = False

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop


        # Process events (keystrokes, mouse clicks, etc)
        done = game.process_events()

        # Update object positions, check for collisions
        game.run_logic()

        # Draw the current frame
        game.display_frame(SCREEN)

        # --- Limit to 60 frames per second
        FPSCLOCK.tick(FPS)

def terminate():
    # Close the window and quit.
    pygame.quit()
    sys.exit()

def checkForQuit():
    for event in pygame.event.get(QUIT): # Pega todos os Quit events
        terminate() # termina
    for event in pygame.event.get(KEYUP): # Paga os KEYUP events
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event)

def flashButtonAnimation(color, animationSpeed=50):
    if color == YELLOW:
        sound = BEEP1
        flashColor = BRIGHTYELLOW
        rectangle = YELLOWRECT
    elif color == BLUE:
        sound = BEEP2
        flashColor = BRIGHTBLUE
        rectangle = BLUERECT
    elif color == RED:
        sound = BEEP3
        flashColor = BRIGHTRED
        rectangle = REDRECT
    elif color == GREEN:
        sound = BEEP4
        flashColor = BRIGHTGREEN
        rectangle = GREENRECT

    origSurf = SCREEN.copy()
    flashSurf = pygame.Surface((BUTTONSIZE, BUTTONSIZE))
    flashSurf = flashSurf.convert_alpha()
    r, g, b = flashColor
    sound.play()
    for start, end, step in ((0, 255, 1), (255, 0, -1)): # Loop de Animação
        for alpha in range(start, end, animationSpeed * step):
            checkForQuit()
            SCREEN.blit(origSurf, (0,0))
            flashSurf.fill((r,g,b, alpha))
            SCREEN.blit(flashSurf, rectangle.topleft)
            pygame.display.update()
            FPSCLOCK.tick(FPS)
    SCREEN.blit(origSurf, (0,0))

def drawButtons():
    pygame.draw.rect(SCREEN, YELLOW, YELLOWRECT)
    pygame.draw.rect(SCREEN, BLUE,   BLUERECT)
    pygame.draw.rect(SCREEN, RED,    REDRECT)
    pygame.draw.rect(SCREEN, GREEN,  GREENRECT)




if __name__ == '__main__':
    main()

