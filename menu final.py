import pygame

pygame.init()

#Imagens do menu
window = pygame.display.set_mode((1000,800))

pygame.display.set_caption('Hunters')

fig1 = pygame.image.load("Graficos/fig1.jpg")
fig2 = pygame.image.load("Graficos/fig2.jpg")
fig3 = pygame.image.load("Graficos/menu.png")


# Tela de inicialização 

IMG1 = pygame.transform.scale(fig1, (1000, 800))
IMG2 = pygame.transform.scale(fig2, (1000, 800))
IMG3 = pygame.transform.scale(fig3, (1000, 800))

render_img1 = True
render_img3 = True
state = "INIT"
i = 0
while state != "QUIT":
    if i <= 0:
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
    if i == 1: 
        window.blit(IMG3, (0,0))
    if i >= 2:
        state == "GAME"
        state == "QUIT"
        break
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            state = "INFORMATIVO"
            i+=1
        if event.type == pygame.QUIT:
            state == "QUIT"
            break
    pygame.display.update()
pygame.quit() 
    
        









