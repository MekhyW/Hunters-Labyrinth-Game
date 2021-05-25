import pygame
import random

pygame.init()
pygame.mixer.init()

#Imagem do menu



# ----- Gera tela principal
window = pygame.display.set_mode((1000,800))
pygame.display.set_caption('Hunters')

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = game_screen(window)
    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
