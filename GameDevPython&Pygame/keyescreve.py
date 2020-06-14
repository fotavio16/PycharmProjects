import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

pygame.key.set_repeat()
print(pygame.key.get_repeat())
font = pygame.font.SysFont("arial", 32)
font_height = font.get_linesize()
pressed_key_text = ""

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        
    screen.fill((255, 255, 255))

    pressed_keys = pygame.key.get_pressed()
    y = font_height
        
    for key_constant, pressed in enumerate(pressed_keys):
        if pressed:
            key_name = pygame.key.name(key_constant)
            pressed_key_text += key_name
            #y+= font_height

    text_surface = font.render(pressed_key_text, True, (0, 0, 0))
    screen.blit(text_surface, (8, y))

    pygame.display.update()    
