import pygame

pygame.init()

#mostrar quem venceu 
window = pygame.display.set_mode((1000, 800))

pygame.display.set_caption('Hunters')

fig4 = pygame.image.load("Graficos/player_1v.jpg")
fig5 = pygame.image.load("Graficos/player_1.jpg")
fig6 = pygame.image.load("Graficos/player_2v.jpg")
fig7 = pygame.image.load("Graficos/player_2.jpg")

IMG4 = pygame.transform.scale(fig4, (1000, 800))
IMG5 = pygame.transform.scale(fig5, (1000, 800))
IMG6 = pygame.transform.scale(fig6, (1000, 800))
IMG7 = pygame.transform.scale(fig7, (1000, 800))

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
                        state = "GAME"
                if render_img4 == True: 
                    render_imag4 = False
                    window.blit(IMG5, (0,0))
                else:
                    render_img4 = True 
                    window.blit(IMG4, (0,0))
            elif state == "GAME":
                render_img4 = False 
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
                        state = "GAME"
                if render_img6 == True: 
                    render_imag6 = False
                    window.blit(IMG7, (0,0))
                else:
                    render_img4 = True 
                    window.blit(IMG6, (0,0))
            elif state == "GAME":
                render_img6 = False 
            else: 
                state = "QUIT"
vencedor(0)

    
         
               
