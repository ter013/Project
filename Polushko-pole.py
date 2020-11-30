import random
from os import path
import random
import pygame
from objects import *

snd_dir = path.join(path.dirname(__file__),'snd')

from objects import Field

Field_size = 10
CELL_SIZE = 50

WIDTH = CELL_SIZE * Field_size
HEIGHT = CELL_SIZE * Field_size
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255, 255,0)


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
clock = pygame.time.Clock()

class Window(pygame.sprite.Sprite):
    def __init__(self, size=10):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.touch_number=0
        self.touch_square=(-1,-1)
        self.size=size+2
        self.field=Field(size,CELL_SIZE,CELL_SIZE)

        for i in range(Field_size):
            pygame.draw.line(self.image,BLACK, (i*CELL_SIZE,0) , (i*CELL_SIZE,HEIGHT))
            pygame.draw.line(self.image,BLACK, (0,i*CELL_SIZE) ,(WIDTH ,i*CELL_SIZE))

        self.draw_field()

    def draw_field(self):
        for i in range(Field_size+2):
            for j in range(Field_size+2):
                self.draw_chip((i,j))

    def draw_chip(self, coords):

        self.field.massive[coords[0]][coords[1]].draw(self.image)



    def fill_square(self,coords,color):
        i=coords[0]
        j=coords[1]
        pygame.draw.rect(self.image, color,
                         ((i - 1) * CELL_SIZE, (j - 1) * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def search_the_square (self, event):
        mp = event.pos
        for i in range(Field_size + 1):
            if (i * CELL_SIZE - mp[0]) // CELL_SIZE == 0:
                for j in range(Field_size + 1):
                    if (j * CELL_SIZE - mp[1]) // CELL_SIZE == 0:
                        return (i,j)

    def swap(self,coords1,coords2):
        #махнуть местами фишки

        self.field.massive[coords1[0]][coords1[1]].color,self.field.massive[coords2[0]][coords2[1]].color = \
            self.field.massive[coords2[0]][coords2[1]].color,self.field.massive[coords1[0]][coords1[1]].color
        move_sound.play()
        self.draw_chip(coords1)
        self.draw_chip(coords2)


    def update (self, event=0):
        if event==0:
            return
        self.touch_number+=1

        if self.touch_number==2:
            self.touch_number=0

            coords1=self.touch_square
            coords2=self.search_the_square(event)
            self.fill_square(coords1, WHITE)

            if abs(coords1[0]-coords2[0])+abs(coords1[1]-coords2[1])<=1:
                self.swap(coords1, coords2)
            else:
                self.draw_chip(coords1)

            self.field.walk_the_line(coords1)
            self.field.walk_the_line(coords2)

            while self.field.check():
                self.field.update()
                self.draw_field()
                clock.tick(2)
        else:
            self.touch_square=self.search_the_square(event)
            self.color = WHITE
            flag=(event.type == pygame.MOUSEBUTTONUP)
            if flag:
                flag=False
                self.fill_square(self.touch_square,BLACK)

        for i in range(Field_size):
            pygame.draw.line(self.image,BLACK, (i*CELL_SIZE,0) , (i*CELL_SIZE,HEIGHT))
            pygame.draw.line(self.image,BLACK, (0,i*CELL_SIZE) ,(WIDTH ,i*CELL_SIZE))

move_sound = pygame.mixer.Sound(path.join(snd_dir, 'blip.wav'))
pygame.mixer.music.load(path.join(snd_dir, 'regression_cyclone.ogg'))
pygame.mixer.music.set_volume(0.4)

all_sprites = pygame.sprite.Group()
s = Window()
all_sprites.add(s)




pygame.mixer.music.play(loops = -1)
running = True
while running:
    
       
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if  event.type == pygame.MOUSEBUTTONUP:
            all_sprites.update(event)
    all_sprites.update()
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()
    
        
