#основная программа
import pygame
from Graphic_objects import *

Field_size = 10
CELL_SIZE = 70
LEFT=300
TOP=70
FPS=30

WIDTH = CELL_SIZE * Field_size
HEIGHT = CELL_SIZE * Field_size

pygame.init()
screen = pygame.display.set_mode((WIDTH+LEFT*2, HEIGHT+TOP*2))
screen.fill(WHITE)
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
Play_window = Window(Field_size, Field_size, CELL_SIZE, LEFT, TOP)

all_sprites.add(Play_window)

pygame.mixer.music.play(loops=-1)
running = True
score=0
flag1=True
flag2=True
flag3=True

while running:

    if Play_window.comatose and not score:
        score=Play_window.field.score

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            all_sprites.update(event)

    all_sprites.update()

    if not Play_window.comatose and score and Play_window.field.score-score>=5:
        wow_sound.play()
    if score and not Play_window.comatose:
        score=0
    if Play_window.field.score>=50 and flag1:
        sound_1.play()
        flag1=False
    if Play_window.field.score>=100 and flag2:
        sound_2.play()
        flag2=False
    if Play_window.field.score>=500 and flag3:
        sound_3.play()
        flag3=False

    screen.fill(WHITE)
    draw_background(screen,WIDTH,HEIGHT,Field_size,CELL_SIZE,LEFT,TOP)
    Play_window.draw_score(screen)
    Play_window.draw_field()
    all_sprites.draw(screen)
    pygame.display.flip()
    Play_window.fall()
    clock.tick(FPS)
