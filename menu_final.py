import pygame
import Sounds
pygame.init()
Sounds.Musica('menu')

#Imagens do menu
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

pygame.display.set_caption('Hunters')

IMG1 = pygame.transform.scale(pygame.image.load("Graficos/fig1.jpg"), (pygame.display.get_surface().get_size()[0], pygame.display.get_surface().get_size()[1]))
IMG2 = pygame.transform.scale(pygame.image.load("Graficos/fig2.jpg"), (pygame.display.get_surface().get_size()[0], pygame.display.get_surface().get_size()[1]))
IMG3 = pygame.transform.scale(pygame.image.load("Graficos/menu.png"), (pygame.display.get_surface().get_size()[0], pygame.display.get_surface().get_size()[1]))


# Tela de inicialização 

render_img1 = True
render_img3 = True
state = "INIT"
telaJogo = 0
while state != "QUIT":
    if telaJogo <= 0:
        pygame.display.update()
        pygame.time.wait(600)
        if state == "INIT":
            
            if render_img1 == True:
                render_img1 = False
                window.blit(IMG2, (0,0))
            else:
                render_img1 = True
                window.blit(IMG1, (0,0))
        elif state == "INFORMATIVO":
            render_img1 = False
        else:         
            state = "QUIT"
    if telaJogo == 1: 
        window.blit(IMG3, (0,0))
    if telaJogo >= 2:
        state = "GAME"
        import Jogo
        state = "QUIT"
        break
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            state = "INFORMATIVO"
            telaJogo+=1
        if event.type == pygame.QUIT:
            state = "QUIT"
            break
    pygame.display.update()
pygame.quit() 