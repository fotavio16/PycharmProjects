import pygame as pg
import random, sys
#from colors import *

#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
BLACK    = (  0,   0,   0)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)


class Block ( pg.sprite.Sprite ):

    def __init__(self, color = BLUE, width = 64, height = 64, texto = "X", cor_fonte = NAVYBLUE ):

        super( Block, self).__init__()

        self.image = pg.Surface(( width, height ))
        self.image.fill ( color )

        textsurface = FONT.render(texto, True, cor_fonte)

        textrect = textsurface.get_rect(center=self.image.get_rect().center)
        print(textrect)

        self.image.blit(textsurface, textrect)
        #self.rect = self.image.get_rect(center=pos)

        self.rect = self.image.get_rect()

    def set_position(self, x, y):

        self.rect.x = x
        self.rect.y = y




if ( __name__ == "__main__" ):
    pg.init()

    window_size = window_width, window_height = 640, 480
    window = pg.display.set_mode(window_size, pg.RESIZABLE)

    FONT = pg.font.SysFont('Arial', 20)

    pg.display.set_caption("Teste com Sprites")

    window.fill( WHITE )

    clock = pg.time.Clock()
    FPS = 60

    block_group = pg.sprite.Group()

    a_block = Block(cor_fonte = BLACK)
    a_block.set_position( window_width/2, window_height/2 )
    another_block = Block( RED, cor_fonte = BLACK )
    another_block.set_position( 100, 100 )

    block_group.add( a_block, another_block )

    block_group.draw( window )


    running = True

    while ( running ):
        for event in pg.event.get():
            if ( event.type == pg.QUIT):
                running = False

        clock.tick( FPS )
        pg.display.update()

    pg.quit()




