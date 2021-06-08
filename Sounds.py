import pygame
import os
pygame.mixer.init()

def Musica(qual):
    pygame.mixer.stop()
    if qual == 'menu':
        pygame.mixer.music.load(os.path.join('Sons/menu.mp3'))
        pygame.mixer.music.play(-1)
    elif qual == 'partida':
        pygame.mixer.music.load(os.path.join('Sons/Partida.mp3'))
        pygame.mixer.music.play(-1)
    elif qual == 'partida2':
        pygame.mixer.music.load(os.path.join('Sons/Partida2.mp3'))
        pygame.mixer.music.play(-1)
    elif qual == 'victory':
        pygame.mixer.music.load(os.path.join('Sons/Victory.mp3'))
        pygame.mixer.music.play(-1)

def EfeitoSonoro(qual):
    if qual == 'encontro':
        pygame.mixer.Sound(os.path.join('Sons/encontro.wav')).play()
    elif qual == 'centro':
        pygame.mixer.Sound(os.path.join('Sons/centro.ogg')).play()
