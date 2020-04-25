import pygame as pg
import random, sys


FPS = 30 # frames per second. Velocidade do programa
COR_INATIVA = pg.Color('lightskyblue3')
print(COR_INATIVA)
COR_ATIVA = pg.Color('dodgerblue2')
print(COR_ATIVA)
BGCOLOR = pg.Color('gold')
print(BGCOLOR)
COR_FONTE = pg.Color('navyblue')
print(COR_FONTE)


LARGURA_JANELA = 600
ALTURA_JANELA = 800
BOX_LADO = 50
TAM_FONTE = 32
DIGITOS = 3
LINHAS = DIGITOS * 2




class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COR_INATIVA
        self.font_color = COR_FONTE
        self.text = text
        self.txt_surface = FONTE.render(text, True, self.font_color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COR_ATIVA if self.active else COR_INATIVA
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONTE.render(self.text, True, self.font_color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(50, self.txt_surface.get_width()+10)
        #width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 0)
        # pg.draw.rect(screen, self.color, self.rect, 2)
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + (self.rect.w - TAM_FONTE / 3) / 2, self.rect.y + (self.rect.h - TAM_FONTE) / 2))





def main():
    global FPSCLOCK, TELA, FONTE
    pg.init()
    FPSCLOCK = pg.time.Clock()
    TELA = pg.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
    TELA.fill(BGCOLOR)
    FONTE = pg.font.SysFont('arial', TAM_FONTE)
    boxes = list()

    pg.display.set_caption('Jogo da Senha')

    box1 = InputBox(50, 50, BOX_LADO, BOX_LADO, 'X')
    boxes.append(box1)
    box1 = InputBox(150, 50, BOX_LADO, BOX_LADO, 'X')
    boxes.append(box1)
    box1 = InputBox(250, 50, BOX_LADO, BOX_LADO, 'X')
    boxes.append(box1)
    box1 = InputBox(50, 150, BOX_LADO, BOX_LADO, '1')
    boxes.append(box1)
    box1 = InputBox(150, 150, BOX_LADO, BOX_LADO, '2')
    boxes.append(box1)
    box1 = InputBox(250, 150, BOX_LADO, BOX_LADO, '3')
    boxes.append(box1)
    boxText = InputBox(50, 300, BOX_LADO, BOX_LADO)


    while True:

        for event in pg.event.get():  # event handling loop
            if event.type == pg.QUIT or (event.type == pg.KEYUP and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

        for box in boxes:
            box.update()

        boxText.update()

        for box in boxes:
            box.draw(TELA)

        boxText.draw(TELA)


        # Desenha a janela e espera o clock tick.
        pg.display.update()
        FPSCLOCK.tick(FPS)





if __name__ == '__main__':
    main()






