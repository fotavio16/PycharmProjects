'''
Este programa contém a classe Block.
Será importado pelo programa principal.

'''

import pygame, random

class Block(pygame.sprite.Sprite):
    '''
    Esta classe representa um objeto.
    Deriva da classe 'Sprite'
    '''

    def __init__(self, filename, width, height):
        # Chama a classe pai do construtor
        super().__init__()

        # Cria a imagem do bloco
        #self.image = pygame.Surface([width, height])
        self.image = pygame.image.load(filename).convert()
        #self.image.fill(color)

        # Cria o retângulo com as dimensões da imagem
        self.rect = self.image.get_rect()
