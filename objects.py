import random as rnd
import pygame

WHITE = (255, 255, 255)
GOLD = (255, 215, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)

Colors=[RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

class Ball:
    "фишечка"
    def __init__(self, x, y, r, color, live=1):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.live = bool(live)
        self.type="ball"

    def draw(self, screen):
        "Рисуем шарик"
        pygame.draw.circle(screen, self.color, (self.x,self.y), self.r)
        "Потом надо засунуть фишки Лехи"


class wave:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Field:
    def __init__(self, n, w, h):
        self.n = n
        self.w=w
        self.h=h
        self.massive=[[Ball(i*self.h-self.w//2,j*self.h-self.h//2,self.h//2,BLACK,1 if(i==0 or j==0 or i==n+1 or j==n+1) else 0)
                       for j in range(n+2)] for i in range(n+2)]
        self.score=0
        self.create_balls()

    def create_balls(self):
        global Colors
        for i in range(1,self.n+1):
            for j in range(1,self.n+1):
                if not self.massive[i][j].live:
                    t= rnd.randint(0, 5)
                    while (self.massive[i][j-1].color==Colors[t] or self.massive[i-1][j].color==Colors[t]):
                        t = rnd.randint(0, 5)
                    self.massive[i][j]=Ball(i*self.w-self.w//2,j*self.h-self.h//2,self.h//2,Colors[t])

    def update(self):
        flag=True
        while flag:
            flag=False
            for i in range(self.n,1,-1):
                for j in range(1,self.n+1):
                    if not self.massive[i][j+1].live and self.massive[i][j].live:
                        self.massive[i][j+1].live=True
                        self.massive[i][j].live=False
                        self.massive[i][j].color,self.massive[i][j+1].color = \
                            self.massive[i][j+1].color,self.massive[i][j].color
                        flag=True
        self.create_balls()

    def check(self):
        for i in range(1,self.n+1):
            for j in range(1,self.n+1):
                if self.massive[i][j].live:
                    self.walk_the_line((i,j))

        for i in range(1, self.n + 1):
            for j in range(1, self.n + 1):
                if not self.massive[i][j].live:
                    return True

        return False

    def walk_the_line(self,coords):
        x0=coords[0]
        y0=coords[1]
        vol=[wave(x0,y0)]
        self.massive[x0][y0].live=False
        current_color=self.massive[x0][y0].color
        go=[wave(1,0),wave(-1,0),wave(0,1),wave(0,-1),]
        for v in vol:
            for g in go:
                if self.massive[v.x+g.x][v.y+g.y].color==current_color and self.massive[v.x+g.x][v.y+g.y].live:
                    vol+=[wave(v.x+g.x,v.y+g.y)]
                    self.massive[v.x + g.x][v.y + g.y].live=False

        if len(vol)>=3:
            self.score+=len(vol)
            for v in vol:
                self.massive[v.x][v.y].color=WHITE
        else:
            for v in vol:
                self.massive[v.x][v.y].live=True















