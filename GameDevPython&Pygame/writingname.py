SKY_BLUE = (135, 206, 235)

my_name = "Fernando Otávio"
import pygame
pygame.init()

my_font = pygame.font.SysFont("arial", 64)
name_surface = my_font.render(my_name, True, (0, 0, 0), SKY_BLUE)
pygame.image.save(name_surface, "name.png")