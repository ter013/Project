#основная программа
import pygame
from Graphic_objects import *
from Time_manager import *

Field_size = 10
CELL_SIZE = 65
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
rulls_button = button(LEFT//2,TOP , LEFT+WIDTH+LEFT/4, TOP+HEIGHT-TOP//2, "RULES")
pause_button = button(LEFT//2,TOP ,LEFT+WIDTH+LEFT/4, TOP-TOP//2, "PAUSE")
Clocks=Сhronometer(200,200,0,100)

all_sprites.add(rulls_button)
all_sprites.add(pause_button)
all_sprites.add(Play_window)


pygame.mixer.music.play(loops=-1)
running = True
score=0
flag1=True
flag2=True
flag3=True
pause=False
rules=False

while running:

    if Play_window.comatose and not score:
        score=Play_window.field.score

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if not pause:
                all_sprites.update(event)
            else:
                pause=False
                rules=False
            if rulls_button.update(event):
                pause=True
                rules=True
            if pause_button.update(event):
                pause=True

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
    draw_background(screen, WIDTH, HEIGHT, Field_size, CELL_SIZE, LEFT, TOP, pause)
    if pause:
        rulls_button.draw(pause)
        if rules:
            draw_rules(screen, WIDTH+2*LEFT, HEIGHT+2*TOP)
        else:
            draw_pause(screen, WIDTH+2*LEFT, HEIGHT+2*TOP)
    if not pause:
        Clocks.time-=600/FPS
        all_draw(all_sprites,screen,Play_window,[rulls_button,pause_button],pause,Clocks)

    pygame.display.flip()
    Clocks.clock.tick(FPS)
