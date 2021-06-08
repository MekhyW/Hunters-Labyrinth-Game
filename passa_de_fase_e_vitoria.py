import pygame
import Sounds
pygame.init()
Sounds.Musica('victory')

#mostrar quem venceu 
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.display.set_caption('Hunters')

IMG4 = pygame.image.load("Graficos/player_1v.jpg")
IMG5 = pygame.image.load("Graficos/player_1.jpg")
IMG6 = pygame.image.load("Graficos/player_2v.jpg")
IMG7 = pygame.image.load("Graficos/player_2.jpg")

def vencedor(player): 
    if player == 0:
        #mostra o player 1 
        render_img4 = True 
        state = "INIT"
        while state != "QUIT":
            pygame.display.update()
            pygame.time.wait(500)
            if state == "INIT":
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN: 
                        state = "QUIT"
                if render_img4 == True: 
                    render_img4 = False
                    window.blit(IMG5, (0,0))
                else:
                    render_img4 = True 
                    window.blit(IMG4, (0,0))
            else: 
                state = "QUIT"
    else: 
        #mostrar o player 2
        render_img6 = True 
        state = "INIT"
        while state != "QUIT":
            pygame.display.update()
            pygame.time.wait(500)
            if state == "INIT":
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN: 
                        state = "QUIT"
                if render_img6 == True: 
                    render_img6 = False
                    window.blit(IMG7, (0,0))
                else:
                    render_img6 = True 
                    window.blit(IMG6, (0,0)) 
            else: 
                state = "QUIT"