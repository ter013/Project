import random as rnd
import pygame
from Colors import *
from draw import *

Colors=[RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, DIMGREY]

class Ball:
    "фишечка"
    def __init__(self, x, y, r, color, live=1):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.live = bool(live)
        self.type="ball"

        bonus=rnd.randint(0,70)
        if color==BLACK:
            self.cristall=self.bomb=self.cross=self.rainbow=False
        else:
            self.cristall=(bonus%5==0)
            bonus = rnd.randint(0, 70)
            self.bomb=(bonus==1)
            self.cross=(bonus==2)
            bonus = rnd.randint(0, 70)
            self.rainbow=(bonus%20==0)

    def draw(self, screen):
        "Рисуем шарик"
        if not self.live:
            return
        beautiful_draw(screen, self.x-self.r, self.y-self.r, 2*self.r, self.color,
                       self.cristall,self.rainbow, int(self.bomb)+int(self.cross)*2)

        "Потом надо засунуть фишки Лехи"


class wave:
    def __init__(self,x,y):
        self.x=x
        self.y=y


class Field:
    def __init__(self, n, w, h,boom_sound):
        self.n = n
        self.w=w
        self.h=h
        self.massive=[[Ball(i*self.h-self.w//2,j*self.h-self.h//2,self.h//2,BLACK,1 if(i==0 or j==0 or i==n+1 or j==n+1) else 0)
                       for j in range(n+2)] for i in range(n+2)]
        self.score=0
        self.create_balls()
        self.boom_sound = boom_sound

    def create_balls(self):
        global Colors
        for i in range(1,self.n+1):
            for j in range(1,self.n+1):
                if not self.massive[i][j].live:
                    t= rnd.randint(0, len(Colors)-1)
                    while (self.massive[i][j-1].color==Colors[t] or self.massive[i-1][j].color==Colors[t]):
                        t = rnd.randint(0, len(Colors)-1)
                    self.massive[i][j]=Ball(i*self.w-self.w//2,j*self.h-self.h//2,self.h//2,Colors[t])

    def update(self):
        flag=False
        for i in range(self.n,0,-1):
            for j in range(1,self.n+1):
                if not self.massive[i][j+1].live and self.massive[i][j].live:
                    self.massive[i][j+1].live=True
                    self.massive[i][j].live=False
                    self.swap((i,j),(i,j+1))
                    flag=True
        return flag

    def swap(self,coords1,coords2):
        self.massive[coords1[0]][coords1[1]].color, self.massive[coords2[0]][coords2[1]].color = \
            self.massive[coords2[0]][coords2[1]].color, self.massive[coords1[0]][coords1[1]].color
        self.massive[coords1[0]][coords1[1]].bomb, self.massive[coords2[0]][coords2[1]].bomb = \
            self.massive[coords2[0]][coords2[1]].bomb, self.massive[coords1[0]][coords1[1]].bomb
        self.massive[coords1[0]][coords1[1]].cross, self.massive[coords2[0]][coords2[1]].cross = \
            self.massive[coords2[0]][coords2[1]].cross, self.massive[coords1[0]][coords1[1]].cross
        self.massive[coords1[0]][coords1[1]].rainbow, self.massive[coords2[0]][coords2[1]].rainbow = \
            self.massive[coords2[0]][coords2[1]].rainbow, self.massive[coords1[0]][coords1[1]].rainbow
        self.massive[coords1[0]][coords1[1]].cristall, self.massive[coords2[0]][coords2[1]].cristall = \
            self.massive[coords2[0]][coords2[1]].cristall, self.massive[coords1[0]][coords1[1]].cristall

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
        if self.massive[x0][y0].rainbow:

            for g in go:
                if(x0+g.x>=1 and x0+g.x<=self.n and y0+g.y>=1 and y0+g.y<=n):
                    self.walk_the_line((x0+g.x,y0+g.y))
            return
        for v in vol:
            for g in go:
                #print(self.massive[v.x][v.y].color, self.massive[v.x+g.x][v.y+g.y].color)
                if (self.massive[v.x+g.x][v.y+g.y].color==current_color or self.massive[v.x+g.x][v.y+g.y].rainbow) \
                        and self.massive[v.x+g.x][v.y+g.y].live:
                    vol+=[wave(v.x+g.x,v.y+g.y)]
                    self.massive[v.x + g.x][v.y + g.y].live=False

        if len(vol)>=3:
            for v in vol:
                self.kill(v.x,v.y)
            return True
        else:
            for v in vol:
                self.massive[v.x][v.y].live=True
            return False

    def kill(self,x,y):
        self.massive[x][y].live = False
        current_chip = self.massive[x][y]
        self.score += current_chip.cristall
        if current_chip.bomb:
            self.bomb_bonus(x,y)
        if current_chip.cross:
            self.cross_bonus(x,y)

    def bomb_bonus(self,x,y):
        deltax=[0,1,-1,2,-2]
        deltay=[0,1,-1,2,-2]
        self.boom_sound.play()
        for dx in deltax:
            for dy in deltay:
                if x+dx<=0 or x+dx>=self.n+1 or y+dy<=0 or y+dy>=self.n+1 or not self.massive[x+dx][y+dy].live:
                    continue
                self.kill(x+dx,y+dy)

    def cross_bonus(self,x,y):
        for i in range(1,self.n+1):
            if self.massive[x][i].live:
                self.kill(x,i)
            if self.massive[i][y].live:
                self.kill(i,y)
