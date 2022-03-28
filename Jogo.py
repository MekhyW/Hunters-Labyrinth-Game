from pygame import sprite
import Gerador_Labirinto
import Sounds
import math
import os
import pygame
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 20)
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption('Hunters')
mudajogador = pygame.image.load(os.path.join("Graficos/muda.jpeg"))
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
    def appendsprites(self):
        repeat = 10
        for x in range(repeat):
            self.sprites_hunter_frente.append(pygame.image.load(os.path.join("Graficos/Take 1 - Frente - Caçador.png")))
        for x in range(repeat):
            self.sprites_hunter_frente.append(pygame.image.load(os.path.join("Graficos/Take 2 - Frente - Caçador.png")))
        for x in range(repeat):
            self.sprites_hunter_frente.append(pygame.image.load(os.path.join("Graficos/Take 3 - Frente - Caçador.png")))
        for x in range(repeat):
            self.sprites_hunter_esquerda.append(pygame.image.load(os.path.join("Graficos/Take 4 - Esquerda - Caçador.png")))
        for x in range(repeat):
            self.sprites_hunter_esquerda.append(pygame.image.load(os.path.join("Graficos/Take 5 - Esquerda - Caçador.png")))
        for x in range(repeat):
            self.sprites_hunter_esquerda.append(pygame.image.load(os.path.join("Graficos/Take 6 - Esquerda - Caçador.png")))
        for x in range(repeat):
            self.sprites_hunter_direita.append(pygame.image.load(os.path.join("Graficos/Take 7 - Direita - Caçador.png")))
        for x in range(repeat):
            self.sprites_hunter_direita.append(pygame.image.load(os.path.join("Graficos/Take 8 - Direita - Caçador.png")))
        for x in range(repeat):
            self.sprites_hunter_direita.append(pygame.image.load(os.path.join("Graficos/Take 9 - Direita - Caçador.png")))
        for x in range(repeat):
            self.sprites_hunter_costas.append(pygame.image.load(os.path.join("Graficos/Take 10 - Costa - Caçador.png")))
        for x in range(repeat):
            self.sprites_hunter_costas.append(pygame.image.load(os.path.join("Graficos/Take 11 - Costa - Caçador.png")))
        for x in range(repeat):
            self.sprites_hunter_costas.append(pygame.image.load(os.path.join("Graficos/Take 12 - Costa - Caçador.png")))
        for x in range(repeat):
            self.sprites_hunted_frente.append(pygame.image.load(os.path.join("Graficos/Caçado - Take 1 - Frente.png")))
        for x in range(repeat):
            self.sprites_hunted_frente.append(pygame.image.load(os.path.join("Graficos/Caçado - Take 2 - Frente.png")))
        for x in range(repeat):
            self.sprites_hunted_frente.append(pygame.image.load(os.path.join("Graficos/Caçado - Take 3 - Frente.png")))
        for x in range(repeat):
            self.sprites_hunted_esquerda.append(pygame.image.load(os.path.join("Graficos/Caçado - Take 4 - Esquerda.png")))
        for x in range(repeat):
            self.sprites_hunted_esquerda.append(pygame.image.load(os.path.join("Graficos/Caçado - Take 5 - Esquerda.png")))
        for x in range(repeat):
            self.sprites_hunted_esquerda.append(pygame.image.load(os.path.join("Graficos/Caçado - Take 6 - Esquerda.png")))
        for x in range(repeat):
            self.sprites_hunted_direita.append(pygame.image.load(os.path.join("Graficos/Caçado - Take 7 - Direita.png")))
        for x in range(repeat):
            self.sprites_hunted_direita.append(pygame.image.load(os.path.join("Graficos/Caçado - Take 8 - Direita.png")))
        for x in range(repeat):
            self.sprites_hunted_direita.append(pygame.image.load(os.path.join("Graficos/Caçado - Take 9 - Direita.png")))
        for x in range(repeat):
            self.sprites_hunted_costas.append(pygame.image.load(os.path.join("Graficos/Caçado - Take 10 - Costa.png")))
        for x in range(repeat):
            self.sprites_hunted_costas.append(pygame.image.load(os.path.join("Graficos/Caçado - Take 11 - Costa.png")))
        for x in range(repeat):
            self.sprites_hunted_costas.append(pygame.image.load(os.path.join("Graficos/Caçado - Take 12 - Costa.png")))
    def __init__(self, is_hunter, largura, altura, startx, starty, cor):
        self.is_hunter = is_hunter
        self.largura = largura
        self.altura = altura
        self.x = startx
        self.y = starty
        self.cor = cor
        self.direction = 3
        self.current_sprite = 0
        self.sprites_hunter_frente = []
        self.sprites_hunter_direita = []
        self.sprites_hunter_esquerda = []
        self.sprites_hunter_costas = []
        self.sprites_hunted_frente = []
        self.sprites_hunted_direita = []
        self.sprites_hunted_esquerda = []
        self.sprites_hunted_costas = []
        self.appendsprites()
    def draw(self):
        if self.is_hunter == False and self.direction == 0:
            sprites = self.sprites_hunted_direita
        elif self.is_hunter == False and self.direction == 1:
            sprites = self.sprites_hunted_esquerda
        elif self.is_hunter == False and self.direction == 2:
            sprites = self.sprites_hunted_costas
        elif self.is_hunter == False and self.direction == 3:
            sprites = self.sprites_hunted_frente
        elif self.is_hunter == True and self.direction == 0:
            sprites = self.sprites_hunter_direita
        elif self.is_hunter == True and self.direction == 1:
            sprites = self.sprites_hunter_esquerda
        elif self.is_hunter == True and self.direction == 2:
            sprites = self.sprites_hunter_costas
        elif self.is_hunter == True and self.direction == 3:
            sprites = self.sprites_hunter_frente
        window.blit(sprites[self.current_sprite], (self.x-10, self.y-10))
        #pygame.draw.rect(window, self.cor ,(self.x, self.y, self.largura, self.altura), 0)

    def moveDireita(self,canmove):
        if self.is_hunter == True and math.sqrt((((self.x+self.largura+2)-(Centro.x+(Centro.largura/2)))**2) + (((self.y+(self.altura/2))-(Centro.y+(Centro.altura/2)))**2)) <= 50:
            canmove = 0
        for wallcenter in Labirinto.wallcenters:
            if math.sqrt((((self.x+self.largura+2)-wallcenter[0])**2) + (((self.y+(self.altura/2))-wallcenter[1])**2)) <= 22:
                canmove = 0
                break
        if canmove == 1:
            self.x += self.velocity
            self.direction = 0
    def moveEsquerda(self,canmove):
        if self.is_hunter == True and math.sqrt((((self.x-2)-(Centro.x+(Centro.largura/2)))**2) + (((self.y+(self.altura/2))-(Centro.y+(Centro.altura/2)))**2)) <= 50:
            canmove = 0
        for wallcenter in Labirinto.wallcenters:
            if math.sqrt((((self.x-2)-wallcenter[0])**2) + (((self.y+(self.altura/2))-wallcenter[1])**2)) <= 22:
                canmove = 0
                break
        if canmove == 1:
            self.x -= self.velocity
            self.direction = 1
    def moveCima(self,canmove):
        if self.is_hunter == True and math.sqrt((((self.x+(self.largura/2))-(Centro.x+(Centro.largura/2)))**2) + (((self.y-2)-(Centro.y+(Centro.altura/2)))**2)) <= 50:
            canmove = 0
        for wallcenter in Labirinto.wallcenters:
            if math.sqrt((((self.x+(self.largura/2))-wallcenter[0])**2) + (((self.y-2)-wallcenter[1])**2)) <= 22:
                canmove = 0
                break
        if canmove == 1:
            self.y -= self.velocity
            self.direction = 2
    def moveBaixo(self,canmove):
        if self.is_hunter == True and math.sqrt((((self.x+(self.largura/2))-(Centro.x+(Centro.largura/2)))**2) + (((self.y+self.altura+2)-(Centro.y+(Centro.altura/2)))**2)) <= 50:
            canmove = 0
        for wallcenter in Labirinto.wallcenters:
            if math.sqrt((((self.x+(self.largura/2))-wallcenter[0])**2) + (((self.y+self.altura+2)-wallcenter[1])**2)) <= 22:
                canmove = 0
                break
        if canmove == 1:
            self.y += self.velocity
            self.direction = 3
        
    def move(self, dirn):
        self.current_sprite += 1
        if self.current_sprite > 28:
            self.current_sprite = 0
        if self.is_hunter == True:
            self.velocity = 1.5
        else:
            self.velocity = 1
        canmove = 1

        if dirn == 0:
            self.moveDireita(canmove)
        elif dirn == 1: 
            self.moveEsquerda(canmove)
        elif dirn == 2: 
            self.moveCima(canmove)
        else: 
            self.moveBaixo(canmove)

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
    if i == 0:
        Sounds.Musica('partida')
    elif i == 3:
        Sounds.Musica('partida2')
    Labirinto = Maze(Gerador_Labirinto.GerarAjustarPrintarLabirinto(tamanho_labirinto_y, tamanho_labirinto_x))
    if i != 0:
        window.blit(mudajogador, (0, 0))
        pygame.display.update()
        pygame.time.delay(2000)
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
            Sounds.EfeitoSonoro('encontro')
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
            Sounds.EfeitoSonoro('centro')
            break
        jogo_clock.tick()
        tempo_atual_partida = pygame.time.get_ticks()/1000 - tempo_inicial_partida
        textsurface = myfont.render(str(round(tempo_atual_partida, 2)), False, (255, 255, 255))
        window.blit(textsurface, (pygame.display.get_surface().get_size()[0]/2, 0))
        pygame.time.wait(10)
        pygame.display.update()
from passa_de_fase_e_vitoria import *
if sum(tempos_player1) <= sum(tempos_player2):
    vencedor(0)
else:
    vencedor(1)