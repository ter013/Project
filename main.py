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
score=0
flag1=True
flag2=True
flag3=True

while running:

    if s.comatose and not score:
        score=s.field.score
        print("!")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            all_sprites.update(event)

    all_sprites.update()

    if not s.comatose and score and s.field.score-score>=5:
        print("!!!!")
        wow_sound.play()
    if score and not s.comatose:
        score=0
    if s.field.score>=50 and flag1:
        sound_1.play()
        flag1=False
    if s.field.score>=100 and flag2:
        sound_2.play()
        flag2=False
    if s.field.score>=500 and flag3:
        sound_3.play()
        flag3=False

    screen.fill(WHITE)
    s.draw_score(screen)
    s.draw_field()
    all_sprites.draw(screen)
    pygame.display.flip()
    s.fall()
