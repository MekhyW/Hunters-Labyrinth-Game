import pygame

pygame.init()

#Imagens do menu
window = pygame.display.set_mode((1000,800))

pygame.display.set_caption('Hunters')

fig1 = pygame.image.load("Graficos/fig1.jpg")
fig2 = pygame.image.load("Graficos/fig2.jpg")


# Tela de inicialização 

IMG1 = pygame.transform.scale(fig1, (1000, 800))
IMG2 = pygame.transform.scale(fig2, (1000, 800))

render_img1 = True
state = "INIT"
while state != "QUIT":
    pygame.display.update()
    pygame.time.wait(100)
    if state == "INIT":
        if render_img1 == True:
            render_img1 = False
            window.blit(IMG2, (0,0))
        else:
            render_img1 = True
            window.blit(IMG1, (0,0))
    elif state == "GAME":
        render_img1 = False
    else:         
        state = "QUIT"
