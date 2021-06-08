import pygame

window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

pygame.display.set_caption('Hunters')

IMG1 = pygame.transform.scale(pygame.image.load("Graficos/fig1.jpg"), (pygame.display.get_surface().get_size()[0], pygame.display.get_surface().get_size()[1]))
IMG2 = pygame.transform.scale(pygame.image.load("Graficos/fig2.jpg"), (pygame.display.get_surface().get_size()[0], pygame.display.get_surface().get_size()[1]))
IMG3 = pygame.transform.scale(pygame.image.load("Graficos/menu.png"), (pygame.display.get_surface().get_size()[0], pygame.display.get_surface().get_size()[1]))

