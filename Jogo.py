import Gerador_Labirinto
import math
import os
import pygame
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 20)
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption('Hunters')
imagewall = pygame.image.load(os.path.join("Graficos/imagewall.png"))
imagecell = pygame.image.load(os.path.join("Graficos/imagecell.png"))
imagedark = pygame.image.load(os.path.join("Graficos/imagedark.png"))
imagewall.convert()
imagecell.convert()
imagedark.convert()

class Maze():
    def __init__(self, labirinto):
        self.labirinto = labirinto
        self.wallcenters = []
    def draw(self):
        self.wallcenters = []
        x = 0
        y = 0
        for linha in range(len(self.labirinto)):
            x = 0
            for coluna in range(len(self.labirinto[linha])):
                if self.labirinto[linha][coluna] == 'c':
                    window.blit(imagecell, (x, y))
                elif self.labirinto[linha][coluna] == 'w':
                    window.blit(imagewall, (x, y))
                    self.wallcenters.append([x+15, y+15])
                if math.sqrt(((Player1.x+(Player1.largura/2))-(x+15+15))**2 + ((Player1.y+(Player1.altura/2))-(y+15))**2) > 100 and math.sqrt(((Player2.x+(Player2.largura/2))-(x+15+15))**2 + ((Player2.y+(Player2.altura/2))-(y+15))**2) > 100:
                    window.blit(imagedark, (x, y)) 
                x += 30
            y += 30
    

class CenterPoint():
    def __init__(self, largura, altura, startx, starty, cor):
        self.largura = largura
        self.altura = altura
        self.x = startx
        self.y = starty
        self.cor = cor
    def draw(self):
        pygame.draw.rect(window, self.cor ,(self.x, self.y, self.largura, self.altura), 0)

class Player():
    def __init__(self, is_hunter, largura, altura, startx, starty, cor):
        self.is_hunter = is_hunter
        self.largura = largura
        self.altura = altura
        self.x = startx
        self.y = starty
        self.cor = cor
    def draw(self):
        pygame.draw.rect(window, self.cor ,(self.x, self.y, self.largura, self.altura), 0)
    def move(self, dirn):
        if self.is_hunter == True:
            self.velocity = 1.5
        else:
            self.velocity = 1
        if dirn == 0:
            canmove = 1
            for wallcenter in Labirinto.wallcenters:
                if math.sqrt((((self.x+self.largura+2)-wallcenter[0])**2) + (((self.y+(self.altura/2))-wallcenter[1])**2)) <= 22:
                    canmove = 0
                    break
            if canmove == 1:
                self.x += self.velocity
        elif dirn == 1:
            canmove = 1
            for wallcenter in Labirinto.wallcenters:
                if math.sqrt((((self.x-2)-wallcenter[0])**2) + (((self.y+(self.altura/2))-wallcenter[1])**2)) <= 22:
                    canmove = 0
                    break
            if canmove == 1:
                self.x -= self.velocity
        elif dirn == 2:
            canmove = 1
            for wallcenter in Labirinto.wallcenters:
                if math.sqrt((((self.x+(self.largura/2))-wallcenter[0])**2) + (((self.y-2)-wallcenter[1])**2)) <= 22:
                    canmove = 0
                    break
            if canmove == 1:
                self.y -= self.velocity
        else:
            canmove = 1
            for wallcenter in Labirinto.wallcenters:
                if math.sqrt((((self.x+(self.largura/2))-wallcenter[0])**2) + (((self.y+self.altura+2)-wallcenter[1])**2)) <= 22:
                    canmove = 0
                    break
            if canmove == 1:
                self.y += self.velocity

posicao_inicial_player1_x = 40
posicao_inicial_player1_y = 10
posicao_inicial_player2_x = pygame.display.get_surface().get_size()[0] - 40
posicao_inicial_player2_y = pygame.display.get_surface().get_size()[1] - 10
Player1 = Player(True, 10, 10, posicao_inicial_player1_x, posicao_inicial_player1_y, (255, 0, 0))
Player2 = Player(False, 10, 10, posicao_inicial_player2_x, posicao_inicial_player2_y, (0, 0, 255))
Centro = CenterPoint(100, 100, (pygame.display.get_surface().get_size()[0]/2)-50, (pygame.display.get_surface().get_size()[1]/2)-50, (0, 255, 0))

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

tamanho_labirinto_y = round(pygame.display.get_surface().get_size()[1]/(3*Player1.altura))
tamanho_labirinto_x = round(pygame.display.get_surface().get_size()[0]/(3*Player1.largura))
jogo_clock = pygame.time.Clock()
tempos_player1 = []
tempos_player2 = []
for i in range(6):
    Labirinto = Maze(Gerador_Labirinto.GerarLabirinto(tamanho_labirinto_y, tamanho_labirinto_x))
    tempo_inicial_partida = pygame.time.get_ticks()/1000
    while True:
        Labirinto.draw()
        Centro.draw()
        Player1.draw()
        Player2.draw()
        MoverPlayers()
        if math.sqrt(((Player1.x+(Player1.largura/2))-(Player2.x+(Player2.largura/2)))**2 + ((Player1.y+(Player1.altura/2))-(Player2.y+(Player2.altura/2)))**2) < max(Player1.largura, Player2.largura):
            Player1.x = posicao_inicial_player1_x
            Player1.y = posicao_inicial_player1_y
            Player2.x = posicao_inicial_player2_x
            Player2.y = posicao_inicial_player2_y
        if Player1.is_hunter == False and math.sqrt(((Player1.x+(Player1.largura/2))-(Centro.x+(Centro.largura/2)))**2 + ((Player1.y+(Player1.altura/2))-(Centro.y+(Centro.altura/2)))**2) < Centro.largura/1.5 or Player2.is_hunter == False and math.sqrt(((Player2.x+(Player2.largura/2))-(Centro.x+(Centro.largura/2)))**2 + ((Player2.y+(Player2.altura/2))-(Centro.y+(Centro.altura/2)))**2) < Centro.largura/1.5:
            Player1.x = posicao_inicial_player1_x
            Player1.y = posicao_inicial_player1_y
            Player2.x = posicao_inicial_player2_x
            Player2.y = posicao_inicial_player2_y
            if Player1.is_hunter == False:
                tempos_player1.append(round(tempo_atual_partida, 2))
            elif Player2.is_hunter == False:
                tempos_player2.append(round(tempo_atual_partida, 2))
            Player1.is_hunter = not Player1.is_hunter
            Player2.is_hunter = not Player2.is_hunter
            break
        jogo_clock.tick()
        tempo_atual_partida = pygame.time.get_ticks()/1000 - tempo_inicial_partida
        textsurface = myfont.render(str(round(tempo_atual_partida, 2)), False, (255, 255, 255))
        window.blit(textsurface, (pygame.display.get_surface().get_size()[0]/2, 0))
        pygame.time.wait(10)
        pygame.display.update()