import pygame

window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

pygame.display.set_caption('Hunters')



IMG8 = pygame.image.load("Graficos/muda_jogador.jpeg")
render_img8 = True
state = "INIT"
i = 0
while state != "QUIT":
    if i == 1: 
        window.blit(IMG8, (0,0))
    if i >= 2:
        state = "GAME"
        import Jogo
        state = "QUIT"
        break
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            state = "INFORMATIVO"
            i+=1
        if event.type == pygame.QUIT:
            state = "QUIT"
            break
    pygame.display.update()
pygame.quit() 
    


