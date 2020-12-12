import pygame
from draw import *

class Сhronometer():
    def __init__(self, width, height, left, top, time_start):

        self.width=width
        self.height=height
        self.left = left
        self.top = top
        self.time_start=time_start
        self.time=time_start
        self.clock=pygame.time.Clock()

    def draw(self,surf):
        draw_watch(surf,self.left+self.width//2,self.top+self.height//2,self.width//2,self.time,self.time_start)

