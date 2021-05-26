import math
import pygame
pygame.init()

window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption('Hunters')

class Background():
    def __init__(self, Image):
        image = Image
    def draw(self):
        #desenhar o fundo na tela
        pass
    
class Player():
    def __init__(self, largura, altura, startx, starty, cor):
        self.largura = largura
        self.altura = altura
        self.x = startx
        self.y = starty
        self.velocity = 2
        self.cor = cor
    def draw(self):
        pygame.draw.rect(window, self.cor ,(self.x, self.y, self.largura, self.altura), 0)
    def move(self, dirn):
        if dirn == 0:
            self.x += self.velocity
        elif dirn == 1:
            self.x -= self.velocity
        elif dirn == 2:
            self.y -= self.velocity
        else:
            self.y += self.velocity

posicao_inicial_player1_x = 100
posicao_inicial_player1_y = 100
posicao_inicial_player2_x = 200
posicao_inicial_player2_y = 200
Player1 = Player(50, 50, posicao_inicial_player1_x, posicao_inicial_player1_y, (255, 0, 0))
Player2 = Player(50, 50, posicao_inicial_player2_x, posicao_inicial_player2_y, (0, 0, 255))

def MoverPlayers():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        quit()
    if keys[pygame.K_DOWN]:
        Player1.move(3)
    if keys[pygame.K_UP]:
        Player1.move(2)
    if keys[pygame.K_RIGHT]:
        Player1.move(0)
    if keys[pygame.K_LEFT]:
        Player1.move(1)
    if keys[pygame.K_s]:
        Player2.move(3)
    if keys[pygame.K_w]:
        Player2.move(2)
    if keys[pygame.K_d]:
        Player2.move(0)
    if keys[pygame.K_a]:
        Player2.move(1)

jogo_clock = pygame.time.Clock()
for i in range(5):
    tempo_inicial_partida = pygame.time.get_ticks()/1000
    while True:
        window.fill((255, 255, 255))
        Player1.draw()
        Player2.draw()
        MoverPlayers()
        if math.sqrt(((Player1.x+(Player1.largura/2))-(Player2.x+(Player2.largura/2)))**2 + ((Player1.y+(Player1.altura/2))-(Player2.y+(Player2.altura/2)))**2) < 50:
            Player1.x = posicao_inicial_player1_x
            Player1.y = posicao_inicial_player1_y
            Player2.x = posicao_inicial_player2_x
            Player2.y = posicao_inicial_player2_y
            break
        jogo_clock.tick()
        tempo_atual_partida = pygame.time.get_ticks()/1000 - tempo_inicial_partida
        pygame.time.wait(10)
        pygame.display.update()