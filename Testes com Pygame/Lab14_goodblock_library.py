'''
Este programa contém a classe GoodBlock.
Esta classe recebe herança da classe Block.
Será importado pelo programa principal.

'''

import pygame, random
from Lab14_block_library import *
from Lab14_Main_Moving import *

class GoodBlock(Block):
    '''
    Esta classe representa um objeto.
    Deriva da classe 'Sprite' e 'Block'
    '''

    def update(self):
        self.rect.x += random.randint(-3, 3)
        self.rect.y += random.randint(-3, 3)

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > WINDOWWIDTH - self.rect.width:
            self.rect.x = WINDOWWIDTH - self.rect.width
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > WINDOWHEIGHT - self.rect.width:
            self.rect.y = WINDOWHEIGHT - self.rect.width