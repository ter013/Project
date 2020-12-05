#основная программа
import pygame
from Graphic_objects import *

Field_size = 10
CELL_SIZE = 70
LEFT=100
TOP=70

WIDTH = CELL_SIZE * Field_size
HEIGHT = CELL_SIZE * Field_size

pygame.init()
screen = pygame.display.set_mode((WIDTH+LEFT*2, HEIGHT+TOP*2))
screen.fill(WHITE)
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
s = Window(Field_size, Field_size, CELL_SIZE, LEFT, TOP)
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
    s.draw_field()
    all_sprites.draw(screen)
    pygame.display.flip()
    s.fall()
