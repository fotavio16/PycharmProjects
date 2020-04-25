'''
Este programa contém a classe GoodBlock.
Esta classe recebe herança da classe Block.
Será importado pelo programa principal.

'''

import pygame, random
from Lab14_block_library import *
from Lab14_Main_Moving import *

class BadBlock(Block):
    '''
    Esta classe representa um objeto.
    Deriva da classe 'Sprite' e 'Block'
    '''

    def update(self):
        self.rect.y += 1

        if self.rect.y > WINDOWWIDTH - self.rect.height:
            self.rect.y = random.randint(-100, -10)
            self.rect.x = random.randint(0, WINDOWWIDTH - self.rect.width)
