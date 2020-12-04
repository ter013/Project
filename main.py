#основная программа
from os import path
import random
import pygame
from Graphic_objects import *

Field_size = 10
CELL_SIZE = 50

WIDTH = CELL_SIZE * Field_size
HEIGHT = CELL_SIZE * Field_size

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH+200, HEIGHT+200))
screen.fill(WHITE)
clock = pygame.time.Clock()


snd_dir = path.join(path.dirname(__file__),'snd')

move_sound = pygame.mixer.Sound(path.join(snd_dir, 'blip.wav'))
pygame.mixer.music.load(path.join(snd_dir, 'Explosion.wav'))
pygame.mixer.music.set_volume(0.4)

all_sprites = pygame.sprite.Group()
s = Window(10, 10, 50, move_sound, 100, 100)
all_sprites.add(s)

pygame.mixer.music.play(loops=-1)
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            all_sprites.update(event)

    all_sprites.update()
    screen.fill(WHITE)
    s.draw_score(screen)
    all_sprites.draw(screen)
    pygame.display.flip()
    s.fall()