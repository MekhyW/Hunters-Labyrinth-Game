#https://www.youtube.com/watch?v=-3B1v-K1oXE&t=135s
import pygame
import socket

SERVER_IP = ''

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = SERVER_IP
        self.port = 5555
        self.addr = (self.host, self.port)
        self.id = self.connect()
    def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(10000).decode()
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            reply = self.client.recv(10000).decode()
            return reply
        except socket.error as e:
            return str(e)


class Player():
    width = height = 50
    def __init__(self, startx, starty, color=(255,0,0)):
        self.x = startx
        self.y = starty
        self.velocity = 2
        self.color = color
    def draw(self, g):
        pygame.draw.rect(g, self.color ,(self.x, self.y, self.width, self.height), 0)
    def move(self, dirn):
        if dirn == 0:
            self.x += self.velocity
        elif dirn == 1:
            self.x -= self.velocity
        elif dirn == 2:
            self.y -= self.velocity
        else:
            self.y += self.velocity


class Game:

    def __init__(self, w, h):
        self.net = Network()
        self.width = w
        self.height = h
        self.player = Player(50, 50)
        self.player2 = Player(100,100)
        self.canvas = Canvas(self.width, self.height, "Teste SOCKETS")

    def run(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.K_ESCAPE:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                if self.player.x <= self.width - self.player.velocity:
                    self.player.move(0)
            if keys[pygame.K_LEFT]:
                if self.player.x >= self.player.velocity:
                    self.player.move(1)
            if keys[pygame.K_UP]:
                if self.player.y >= self.player.velocity:
                    self.player.move(2)
            if keys[pygame.K_DOWN]:
                if self.player.y <= self.height - self.player.velocity:
                    self.player.move(3)
            self.player2.x, self.player2.y = self.parse_data(self.send_data())
            self.canvas.draw_background()
            self.player.draw(self.canvas.get_canvas())
            self.player2.draw(self.canvas.get_canvas())
            self.canvas.update()

        pygame.quit()

    def send_data(self):
        data = str(self.net.id) + ":" + str(self.player.x) + "," + str(self.player.y)
        reply = self.net.send(data)
        return reply

    @staticmethod
    def parse_data(data):
        try:
            d = data.split(":")[1].split(",")
            return int(d[0]), int(d[1])
        except:
            return 0,0


class Canvas:

    def __init__(self, w, h, name="None"):
        self.width = w
        self.height = h
        self.screen = pygame.display.set_mode((w,h))
        pygame.display.set_caption(name)

    @staticmethod
    def update():
        pygame.display.update()

    def get_canvas(self):
        return self.screen

    def draw_background(self):
        self.screen.fill((255,255,255))


g = Game(1000,1000)
g.run()