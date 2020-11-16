#прорисовка объектов
import pygame, sys
from pygame.draw import *
import math

DIMGREY = (105, 105, 105)
CRIMSON = (220, 20, 60)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255,255,255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, BLACK]

FPS = 30
screen = pygame.display.set_mode((800, 600))
screen.fill(WHITE)


def draw(a, color1, color2, n, surf, k, x, y):
    '''
    фунцкия рисует красивую фишку
    :param color1: основной цвет фишки
    :param color2: дополнительный оттенок
    :param a: размер ячейки, на которой находится фишка
    :param n: число углов у многоугольника
    :param k: масштабный коэффициент
    :param surf: экран, на которой отрисовывается плоскость с рисунком
    :param x: положение плоскости на экране по оси x
    :param y: положение плосккости на экране по оси y
    '''
    surface = pygame.Surface((a, a), pygame.SRCALPHA, 32)
    surface.fill(WHITE)

    u = 2*math.pi/n #характерный угол

    list = [] #лист для координат вершин n-угольника

    for i in range(0, n + 1, 1):
        list.append((a/2 + k*a*math.sin(u/2 + u*i), a/2 + k*a*math.cos(u/2 + u*i)))

    polygon(surface, color1, list )





    pygame.draw.line(surface, DIMGREY, [a/2 - k*a/3, a/2 - k*a/7], [a/2 + k*a/7, a/2 - k*a/7])

    pygame.draw.line(surface, DIMGREY, [a/2 - k*a/7, a/2 + k*a/3], [a/2 - k*a/7, a/2 - k*a/7])

    pygame.draw.line(surface, DIMGREY, [a/2 + k*a/7, a/2 + k*a/7], [a/2 + k*a/7, a/2 - k*a/3])

    pygame.draw.line(surface, DIMGREY, [a/2 + k*a/3, a/2 + k*a/7], [a/2 - k*a/7, a/2 + k * a/7])

    pygame.draw.lines(surface, DIMGREY, False,[[a/2 + k*a/3, a/2 + 4*k*a/5], [a/2 - k*a/3, a/2 + 4*k*a/5],
                                                [a/2 - k*a/3, a/2 + 2*k*a/5], [a/2 + k*a/3, a/2 + 2*k*a/5],
                                                [a/2 + k*a/3, a/2 + 3.5*k*a/5], [a/2 - 1*k*a/5, a/2 + 3.5*k*a/5],
                                                [a/2 - 1*k*a/5, a/2 + 2.5*k*a/5], [a/2 + 1*k*a/5, a/2 + 2.5*k*a/5],
                                                [a/2 + 1*k*a/5, a/2 + 3*k*a/5], [a/2, a/2 + 3*k*a/5]])

    pygame.draw.lines(surface, DIMGREY, False,
                      [[a/2 - k*a/3, a/2 - 4*k*a/5], [a/2 + k*a/3, a/2 - 4*k*a/5],
                       [a/2 + k*a/3, a/2 - 2*k*a/5], [a/2 - k*a/3, a/2 - 2*k*a/5],
                       [a/2 - k*a/3, a/2 - 3.5*k*a/5], [a/2 + 1*k*a/5, a/2 - 3.5* k*a/5],
                       [a/2 + 1*k*a/5, a/2 - 2.5*k*a/5], [a/2 - 1*k*a/5, a/2 - 2.5*k*a/5],
                       [a/2 - 1*k*a/5, a/2 - 3* k*a/5], [a/2, a/2 - 3*k*a/5]])

    pygame.draw.lines(surface, DIMGREY, False,
                      [[a/2 - 4*k*a/5, a/2 + k*a/3], [a/2 - 4*k*a/5, a/2 - k*a/3],
                       [a/2 - 2*k*a/5, a/2 - k*a/3], [a/2 - 2*k*a/5, a/2 + k*a/3],
                       [a/2 - 3.5*k*a/5, a/2 + k*a/3], [a/2 - 3.5*k*a/5, a/2 - 1*k*a/5],
                       [a/2 - 2.5*k*a/5, a/2 - 1*k*a/5], [a/2 - 2.5*k*a/5, a/2 + 1*k*a/5],
                       [a/2 - 3*k*a/5, a/2 + 1*k*a/5], [a/2 - 3* k*a/5, a/2]])

    pygame.draw.lines(surface, DIMGREY, False,
                      [[a/2 + 4*k*a/5, a/2 - k*a/3], [a/2 + 4*k*a/5, a/2 + k*a/3],
                       [a/2 + 2*k*a/5, a/2 + k*a/3], [a/2 + 2*k*a/5, a/2 - k*a/3],
                       [a/2 + 3.5*k*a/5, a/2 - k*a/3], [a/2 + 3.5*k*a/5, a/2 + 1*k*a/5],
                       [a/2 + 2.5*k*a/5, a/2 + 1*k*a/5], [a/2 + 2.5*k*a/5, a/2 - 1*k*a/5],
                       [a/2 + 3*k*a/5, a/2 - 1*k*a/5], [a/2 + 3*k*a/5, a/2]])

    pygame.draw.line(surface, DIMGREY, [a/2 - 4*k*a/5, a/2 - 2*k*a/5], [a/2 -2*k*a/5, a/2 - 4*k*a/5 ])

    pygame.draw.line(surface, DIMGREY, [a/2 - 3*k*a/5, a/2 - 2*k*a/5],[a/2 - 2*k*a/5, a/2 - 3*k*a/5])

    pygame.draw.line(surface, DIMGREY, [a / 2 + 4 * k * a / 5, a / 2 - 2 * k * a / 5],
                     [a / 2 + 2 * k * a / 5, a / 2 - 4 * k * a / 5])

    pygame.draw.line(surface, DIMGREY, [a / 2 + 3 * k * a / 5, a / 2 - 2 * k * a / 5],
                     [a / 2 + 2 * k * a / 5, a / 2 - 3 * k * a / 5])

    pygame.draw.line(surface, DIMGREY, [a / 2 + 4 * k * a / 5, a / 2 + 2 * k * a / 5],
                     [a / 2 + 2 * k * a / 5, a / 2 + 4 * k * a / 5])

    pygame.draw.line(surface, DIMGREY, [a / 2 + 3 * k * a / 5, a / 2 + 2 * k * a / 5],
                     [a / 2 + 2 * k * a / 5, a / 2 + 3 * k * a / 5])

    pygame.draw.line(surface, DIMGREY, [a / 2 - 4 * k * a / 5, a / 2 + 2 * k * a / 5],
                     [a / 2 - 2 * k * a / 5, a / 2 + 4 * k * a / 5])

    pygame.draw.line(surface, DIMGREY, [a / 2 - 3 * k * a / 5, a / 2 + 2 * k * a / 5],
                     [a / 2 - 2 * k * a / 5, a / 2 + 3 * k * a / 5])

    pygame.draw.rect(surface, color2, (a/2 - k*a/3, a/2 - k*a/3, 2*k*a/3, 2*k*a/3), 3)


    pygame.draw.aalines(surface, color2, True, list)

    surf.blit(surface, (x, y), special_flags=pygame.BLEND_RGBA_MIN)
draw(250, RED, CRIMSON, 8, screen, 0.4, 300, 400)


pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()