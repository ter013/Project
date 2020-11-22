#прорисовка объектов
import pygame, sys
from pygame.draw import *
import math

DIMGREY = (105, 105, 105)

RED = (255, 0, 0)
CRIMSON = (220, 20, 60)

PURPLE = (128, 0, 128)
INDIGO = (75, 0, 130)

YELLOW = (255, 255, 0)
GOLD = (255, 215, 0)

ROYALBLUE = (65, 105, 225)
BLUE = (0, 0, 255)

DARKORANGE = (255, 140, 0)
ORANGERED = (255, 69, 0)

GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255,255,255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, BLACK]

FPS = 30
screen = pygame.display.set_mode((800, 600))
screen.fill(WHITE)


def draw1(a, color1, color2, n, surface, k, alpha):
    '''
    фунцкия рисует основу некоторых фишек
    :param color1: основной цвет фишки
    :param color2: цвет окантовки
    :param a: размер ячейки, на которой находится фишка
    :param n: число углов у многоугольника
    :param k: масштабный коэффициент
    :param alpha: позволяет вращать фигуру

    '''

    u =2*math.pi/n #характерный угол

    list = [] #лист для координат вершин n-угольника

    for i in range(0, n + 1, 1):
        list.append((int(a/2 + k*a*math.sin(alpha + u/2 + u*i)), int(a/2 + k*a*math.cos(alpha + u/2 + u*i))))

    polygon(surface, color1, list)

    for i in range(1, n + 1, 1):
        pygame.draw.line(surface, color2, list[i], list[i-1], 5)






def draw2(a, color, n, surface, k, alpha):
    '''
    функция рисует внутреннюю n-угольную рамочку у фишки
    :param a: размер плоскти ячейки
    :param color: цвет рамочки
    :param n: число улов
    :param surface: плоскость, на которой рисуется
    :param k: масштабный факторa
    :param alpha: угол поворота рамки
    '''
    u = 2 * math.pi / n  # характерный угол

    list = []  # лист для координат вершин n-угольника

    for i in range(0, n + 1, 1):
        list.append((int(a / 2 + math.sqrt(2) * k * a / 3 * math.sin(alpha + u / 2 + u * i)),
                     int(a / 2 + math.sqrt(2) * k * a / 3 * math.cos(alpha + u / 2 + u * i))))

    pygame.draw.lines(surface, color, False, list, 3)


def red_chip(a, surf, color, k, x, y):
    '''
    функция рисует красную фишку с орнаментом
    :param a: размер ячейки
    :param color: цвет основы ячейки
    :param surf: экран, куда отображается плоскость
    :param k: масштаб изображения внутри ячейкм
    :param x: положение ячейки на экране по оси x
    :param y: положение ячейки на экране по оси y
    '''

    surface = pygame.Surface((a, a), pygame.SRCALPHA, 32)
    surface.fill(color)

    draw1(a, RED, CRIMSON, 8, surface, k, 0)


    pygame.draw.line(surface, DIMGREY, [a / 2 - k * a / 3, a / 2 - k * a / 7],
                     [a / 2 + k * a / 7, a / 2 - k * a / 7])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - k * a / 7), int(a / 2 + k * a / 3)],
                     [int(a / 2 - k * a / 7), int(a / 2 - k * a / 7)])

    pygame.draw.line(surface, DIMGREY, [a / 2 + k * a / 7, a / 2 + k * a / 7], [a / 2 + k * a / 7, a / 2 - k * a / 3])

    pygame.draw.line(surface, DIMGREY, [a / 2 + k * a / 3, a / 2 + k * a / 7], [a / 2 - k * a / 7, a / 2 + k * a / 7])

    pygame.draw.lines(surface, DIMGREY, False,
                      [[a / 2 + k * a / 3, a / 2 + 4 * k * a / 5], [a / 2 - k * a / 3, a / 2 + 4 * k * a / 5],
                       [a / 2 - k * a / 3, a / 2 + 2 * k * a / 5], [a / 2 + k * a / 3, a / 2 + 2 * k * a / 5],
                       [a / 2 + k * a / 3, a / 2 + 3.5 * k * a / 5], [a / 2 - 1 * k * a / 5, a / 2 + 3.5 * k * a / 5],
                       [a / 2 - 1 * k * a / 5, a / 2 + 2.5 * k * a / 5],
                       [a / 2 + 1 * k * a / 5, a / 2 + 2.5 * k * a / 5],
                       [a / 2 + 1 * k * a / 5, a / 2 + 3 * k * a / 5], [a / 2, a / 2 + 3 * k * a / 5]])

    pygame.draw.lines(surface, DIMGREY, False,
                      [[a / 2 - k * a / 3, a / 2 - 4 * k * a / 5], [a / 2 + k * a / 3, a / 2 - 4 * k * a / 5],
                       [a / 2 + k * a / 3, a / 2 - 2 * k * a / 5], [a / 2 - k * a / 3, a / 2 - 2 * k * a / 5],
                       [a / 2 - k * a / 3, a / 2 - 3.5 * k * a / 5], [a / 2 + 1 * k * a / 5, a / 2 - 3.5 * k * a / 5],
                       [a / 2 + 1 * k * a / 5, a / 2 - 2.5 * k * a / 5],
                       [a / 2 - 1 * k * a / 5, a / 2 - 2.5 * k * a / 5],
                       [a / 2 - 1 * k * a / 5, a / 2 - 3 * k * a / 5], [a / 2, a / 2 - 3 * k * a / 5]])

    pygame.draw.lines(surface, DIMGREY, False,
                      [[a / 2 - 4 * k * a / 5, a / 2 + k * a / 3], [a / 2 - 4 * k * a / 5, a / 2 - k * a / 3],
                       [a / 2 - 2 * k * a / 5, a / 2 - k * a / 3], [a / 2 - 2 * k * a / 5, a / 2 + k * a / 3],
                       [a / 2 - 3.5 * k * a / 5, a / 2 + k * a / 3], [a / 2 - 3.5 * k * a / 5, a / 2 - 1 * k * a / 5],
                       [a / 2 - 2.5 * k * a / 5, a / 2 - 1 * k * a / 5],
                       [a / 2 - 2.5 * k * a / 5, a / 2 + 1 * k * a / 5],
                       [a / 2 - 3 * k * a / 5, a / 2 + 1 * k * a / 5], [a / 2 - 3 * k * a / 5, a / 2]])

    pygame.draw.lines(surface, DIMGREY, False,
                      [[a / 2 + 4 * k * a / 5, a / 2 - k * a / 3], [a / 2 + 4 * k * a / 5, a / 2 + k * a / 3],
                       [a / 2 + 2 * k * a / 5, a / 2 + k * a / 3], [a / 2 + 2 * k * a / 5, a / 2 - k * a / 3],
                       [a / 2 + 3.5 * k * a / 5, a / 2 - k * a / 3], [a / 2 + 3.5 * k * a / 5, a / 2 + 1 * k * a / 5],
                       [a / 2 + 2.5 * k * a / 5, a / 2 + 1 * k * a / 5],
                       [a / 2 + 2.5 * k * a / 5, a / 2 - 1 * k * a / 5],
                       [a / 2 + 3 * k * a / 5, a / 2 - 1 * k * a / 5], [a / 2 + 3 * k * a / 5, a / 2]])

    pygame.draw.line(surface, DIMGREY, [a / 2 - 4 * k * a / 5, a / 2 - 2 * k * a / 5],
                     [a / 2 - 2 * k * a / 5, a / 2 - 4 * k * a / 5])

    pygame.draw.line(surface, DIMGREY, [a / 2 - 3 * k * a / 5, a / 2 - 2 * k * a / 5],
                     [a / 2 - 2 * k * a / 5, a / 2 - 3 * k * a / 5])

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

    draw2(a, CRIMSON, 4, surface, k, 0)

    surf.blit(surface, (x, y), special_flags=pygame.BLEND_RGBA_MIN)

def purple_chip(a, surf, color, k, x, y):
    '''
    функция рисует фиолетовую фишку с орнаментом
    :param a: размер ячейки
    :param color: цвет основы ячейки
    :param surf: экран, куда отображается плоскость
    :param k: масштаб изображения внутри ячейкм
    :param x: положение ячейки на экране по оси x
    :param y: положение ячейки на экране по оси y
    '''

    surface = pygame.Surface((a, a), pygame.SRCALPHA, 32)
    surface.fill(color)

    draw1(a, PURPLE, INDIGO, 8, surface, k, -math.pi/8)

    pygame.draw.line(surface, DIMGREY, [a / 2, a / 2 + 4.7 * k * a / 5], [a / 2, a / 2 + 3.2 * k * a / 5])

    pygame.draw.arc(surface, DIMGREY, (a / 2 - k * a / 3 , a / 2 + k * a / 3, k * a / 3,
                                       2 * (3.2 / 5 - 1 / 3) * k * a ), 0, math.pi / 2)

    pygame.draw.arc(surface, DIMGREY, (a / 2,  a / 2 + k * a / 3, k * a / 3,
                                       2 * (3.2 / 5 - 1 / 3) * k * a), math.pi / 2, -math.pi)


    pygame.draw.line(surface, DIMGREY, [a / 2, a / 2 - 4.7 * k * a / 5], [a / 2, a / 2 - 3.2 * k * a / 5])

    pygame.draw.arc(surface, DIMGREY, (a / 2 - k * a / 3, a / 2 - k * a / 3 - 2 * (3.2 / 5 - 1 / 3) * k * a,
                                       k * a / 3,
                                       2 * (3.2 / 5 - 1 / 3) * k * a), 3 / 2 * math.pi , 0)

    pygame.draw.arc(surface, DIMGREY, (a / 2, a / 2 - k * a / 3 - 2 * (3.2 / 5 - 1 / 3) * k * a , k * a / 3,
                                       2 * (3.2 / 5 - 1 / 3) * k * a), math.pi , -math.pi / 2)



    pygame.draw.line(surface, DIMGREY, [a / 2 + 4.7 * k * a / 5, a / 2], [a / 2 + 3.2 * k * a / 5, a / 2])

    pygame.draw.arc(surface, DIMGREY, (a / 2 + k * a / 3, a / 2 - k * a / 3, 2 * (3.2 / 5 - 1 / 3) * k * a,
                                       k * a / 3), math.pi, - math.pi / 2)

    pygame.draw.arc(surface, DIMGREY, (a / 2 + k * a / 3, a / 2 , 2 * (3.2 / 5 - 1 / 3) * k * a,
                                       k * a / 3), math.pi / 2, -math.pi)


    pygame.draw.line(surface, DIMGREY, [a / 2 - 4.7 * k * a / 5, a / 2], [a / 2 - 3.2 * k * a / 5, a / 2])

    pygame.draw.arc(surface, DIMGREY, (a / 2 - k * a / 3 - 2 * (3.2 / 5 - 1 / 3) * k * a,
                                       a / 2 - k * a / 3, 2 * (3.2 / 5 - 1 / 3) * k * a,
                                       k * a / 3), 3 / 2 * math.pi, 0)

    pygame.draw.arc(surface, DIMGREY, (a / 2 - k * a / 3 - 2 * (3.2 / 5 - 1 / 3) * k * a,
                                       a / 2, 2 * (3.2 / 5 - 1 / 3) * k * a,
                                       k * a / 3), 0, - 3 / 2 * math.pi)


    pygame.draw.arc(surface, DIMGREY, (a / 2 - k * a / 3, a / 2 - 2 * k * a / 3, k * a / 3,
                                       2 * k * a / 3), math.pi / 2, -math.pi)

    pygame.draw.arc(surface, DIMGREY, (a / 2 - 2 * k * a / 3, a / 2 - k * a / 3, 2 * k * a / 3,
                                       k * a / 3), math.pi / 2, -math.pi  )

    pygame.draw.circle(surface, DIMGREY, (int(a / 2 - k * a / 1.7), int(a / 2 - k * a / 1.7)), int(k * a / 8), 1)


    pygame.draw.arc(surface, DIMGREY, (a / 2 , a / 2 - 2 * k * a / 3, k * a / 3,
                                       2 * k * a / 3), 0, - 3 / 2 * math.pi)

    pygame.draw.arc(surface, DIMGREY, (a / 2, a / 2 - k * a / 3, 2 * k * a / 3,
                                       k * a / 3), 0, -3 / 2 * math.pi)

    pygame.draw.circle(surface, DIMGREY, (int(a / 2 + k * a / 1.7), int(a / 2 - k * a / 1.7)), int(k * a / 8), 1)


    pygame.draw.arc(surface, DIMGREY, (a / 2, a / 2, 2 * k * a / 3,
                                       k * a / 3), 3 /2 * math.pi, 0)

    pygame.draw.arc(surface, DIMGREY, (a / 2, a / 2 , k * a / 3,
                                       2 * k * a / 3), 3 / 2 * math.pi, 0)

    pygame.draw.circle(surface, DIMGREY, (int(a / 2 + k * a / 1.7), int(a / 2 + k * a / 1.7)), int(k * a / 8), 1)


    pygame.draw.arc(surface, DIMGREY, (a / 2 - k * a / 3, a / 2, k * a / 3,
                                       2 * k * a / 3), math.pi , - math. pi / 2)

    pygame.draw.arc(surface, DIMGREY, (a / 2 - 2 / 3 * k * a, a / 2, 2 * k * a / 3,
                                       k * a / 3), math.pi,  - math.pi / 2)

    pygame.draw.circle(surface, DIMGREY, (int(a / 2 - k * a / 1.7), int(a / 2 + k * a / 1.7)), int(k * a / 8), 1)

    pygame.draw.circle(surface, DIMGREY,(int(a /2), int(a / 2)), int(k * a / 20))

    pygame.draw.circle(surface, DIMGREY, (int(a / 2), int(a / 2)), int(k * a / 8), 1)

    m = 20 #коэффициент, регулирующий угол наклона лучиков

    pygame.draw.line(surface, DIMGREY, [a / 2 + (k * a / 8) * math.sin(math.pi / m),
                                        a / 2 + (k * a / 8) * math.cos(math.pi / m)],
                                        [a / 2 + k * a / 3 * math.tan(math.pi / m), a / 2 + k * a / 3])

    pygame.draw.line(surface, DIMGREY, [a / 2 - (k * a / 8) * math.sin(math.pi / m),
                                        a / 2 + (k * a / 8) * math.cos(math.pi / m)],
                                        [a / 2 - k * a / 3 * math.tan(math.pi / m), a / 2 + k * a / 3])

    pygame.draw.line(surface, DIMGREY, [a / 2 - (k * a / 8) * math.sin(math.pi / m),
                                        a / 2 - (k * a / 8) * math.cos(math.pi / m)],
                                        [a / 2 - k * a / 3 * math.tan(math.pi / m), a / 2 - k * a / 3])

    pygame.draw.line(surface, DIMGREY, [a / 2 + (k * a / 8) * math.sin(math.pi / m),
                                        a / 2 - (k * a / 8) * math.cos(math.pi / m)],
                                        [a / 2 + k * a / 3 * math.tan(math.pi / m), a / 2 - k * a / 3])

    pygame.draw.line(surface, DIMGREY, [a / 2 + (k * a / 8) * math.cos(math.pi / m),
                                        a / 2 - (k * a / 8) * math.sin(math.pi / m)],
                                        [a / 2 + k * a / 3, a / 2 - k * a / 3 * math.tan(math.pi / m)])

    pygame.draw.line(surface, DIMGREY, [a / 2 + (k * a / 8) * math.cos(math.pi / m),
                                        a / 2 + (k * a / 8) * math.sin(math.pi / m)],
                                        [a / 2 + k * a / 3, a / 2 + k * a / 3 * math.tan(math.pi / m)])

    pygame.draw.line(surface, DIMGREY, [a / 2 - (k * a / 8) * math.cos(math.pi / m),
                                        a / 2 - (k * a / 8) * math.sin(math.pi / m)],
                                        [a / 2 - k * a / 3, a / 2 - k * a / 3 * math.tan(math.pi / m)])

    pygame.draw.line(surface, DIMGREY, [a / 2 - (k * a / 8) * math.cos(math.pi / m),
                                        a / 2 + (k * a / 8) * math.sin(math.pi / m)],
                                        [a / 2 - k * a / 3, a / 2 + k * a / 3 * math.tan(math.pi / m)])


    pygame.draw.line(surface, DIMGREY, [a / 2 + k * a / 4, a /2 + k * a /4],
                                        [a /2 + k * a / 4, a / 2 + k * a / 3])

    pygame.draw.line(surface, DIMGREY, [a / 2 + k * a / 4, a / 2 + k * a / 4],
                                        [a / 2 + k * a / 3, a / 2 + k * a / 4])

    pygame.draw.line(surface, DIMGREY, [a / 2 - k * a / 4, a / 2 + k * a / 4],
                                        [a / 2 - k * a / 4, a / 2 + k * a / 3])

    pygame.draw.line(surface, DIMGREY, [a / 2 - k * a / 4, a / 2 + k * a / 4],
                     [a / 2 - k * a / 3, a / 2 + k * a / 4])

    pygame.draw.line(surface, DIMGREY, [a / 2 - k * a / 4, a / 2 - k * a / 4],
                     [a / 2 - k * a / 4, a / 2 - k * a / 3])

    pygame.draw.line(surface, DIMGREY, [a / 2 - k * a / 4, a / 2 - k * a / 4],
                     [a / 2 - k * a / 3, a / 2 - k * a / 4])

    pygame.draw.line(surface, DIMGREY, [a / 2 + k * a / 4, a / 2 - k * a / 4],
                     [a / 2 + k * a / 4, a / 2 - k * a / 3])

    pygame.draw.line(surface, DIMGREY, [a / 2 + k * a / 4, a / 2 - k * a / 4],
                     [a / 2 + k * a / 3, a / 2 - k * a / 4])

    draw2(a, INDIGO, 4, surface, k, 0)


    surf.blit(surface, (x, y), special_flags=pygame.BLEND_RGBA_MIN)

def yellow_chip(a, surf, color, k, x, y):
    '''
        функция рисует жёлтую фишку с орнаментом
        :param a: размер ячейки
        :param color: цвет основы ячейки
        :param surf: экран, куда отображается плоскость
        :param k: масштаб изображения внутри ячейкм
        :param x: положение ячейки на экране по оси x
        :param y: положение ячейки на экране по оси y
        '''

    surface = pygame.Surface((a, a), pygame.SRCALPHA, 32)
    surface.fill(color)

    pygame.draw.circle(surface, YELLOW, (int(a / 2) , int(a / 2)), int(k * a))
    pygame.draw.circle(surface, GOLD, (int(a / 2), int(a / 2)), int(k * a) , 2)

    pygame.draw.circle(surface, DIMGREY, (int(a / 2), int(a / 2)), int(k * a / 8), 1)

    pygame.draw.line(surface, DIMGREY, [a / 2, a / 2 + k * a /6], [a / 2, a / 2 + k * a / 3])

    pygame.draw.line(surface, DIMGREY, [a / 2, a / 2 - k * a / 6], [a / 2, a / 2 - k * a / 3])

    pygame.draw.line(surface, DIMGREY, [a / 2 - k * a /6, a / 2], [a / 2 - k * a / 3, a / 2])

    pygame.draw.line(surface, DIMGREY, [a / 2 + k * a / 6, a / 2], [a / 2 + k * a / 3, a / 2])

    pygame.draw.line(surface, DIMGREY, [a / 2 + k * a / 7, a / 2 - k * a / 7],
                                        [a / 2 + k * a / 4, a / 2 - k * a / 4])

    pygame.draw.line(surface, DIMGREY, [a / 2 - k * a / 7, a / 2 - k * a / 7],
                                        [a / 2 - k * a / 4, a / 2 - k * a / 4])

    pygame.draw.line(surface, DIMGREY, [a / 2 + k * a / 7, a / 2 + k * a / 7],
                                        [a / 2 + k * a / 4, a / 2 + k * a / 4])

    pygame.draw.line(surface, DIMGREY, [a / 2 - k * a / 7, a / 2 + k * a / 7],
                                        [a / 2 - k * a / 4, a / 2 + k * a / 4])


    #рисуем узорчик в правом верхнем углу

    pygame.draw.line(surface, DIMGREY, [a / 2 + k * a / 4 - k * a / 8, a / 2 - k * a / 4 - k * a / 8 ],
                                        [a / 2 + k * a /4 - k * a / 8 + k * a / 8,
                                         a / 2 - k * a / 4 - k * a / 8 - k * a / 8])

    pygame.draw.line(surface, DIMGREY, [a / 2 + k * a / 4 + k * a / 8, a / 2 - k * a / 4 + k * a / 8],
                                        [a / 2 + k * a / 4 + k * a / 8 + k * a / 8,
                                        a / 2 - k * a / 4 + k * a / 8 - k * a / 8])

    pygame.draw.line(surface, DIMGREY, [a / 2 + k * a /4 - k * a / 8 + k * a / 8,
                                        a / 2 - k * a / 4 - k * a / 8 - k * a / 8],
                                        [a / 2 + k * a / 4 + k * a / 8 + k * a / 8,
                                        a / 2 - k * a / 4 + k * a / 8 - k * a / 8])

    pygame.draw.line(surface, DIMGREY, [a / 2 + 0.37 * k * a - k * a / 20, a / 2 - 0.37 * k * a - k * a / 20],
                                        [a / 2 + 0.37 * k * a - k * a / 20 + k * a / 8,
                                        a / 2 - 0.37 * k * a - k * a / 20 - k * a / 8])

    pygame.draw.line(surface, DIMGREY, [a / 2 + 0.37 * k * a + k * a / 20, a / 2 - 0.37 * k * a + k * a / 20],
                                        [a / 2 + 0.37 * k * a + k * a / 20 + k * a / 8,
                                        a / 2 - 0.37 * k * a + k * a / 20 - k * a / 8])

    pygame.draw.line(surface, DIMGREY, [a / 2 + 0.37 * k * a - k * a / 20 + k * a / 8,
                                        a / 2 - 0.37 * k * a - k * a / 20 - k * a / 8],
                                        [a / 2 + 0.37 * k * a + k * a / 20 + k * a / 8,
                                        a / 2 - 0.37 * k * a + k * a / 20 - k * a / 8])
    pygame.draw.line(surface, DIMGREY, [a / 2 + 0.37 * k * a, a / 2 - 0.37 * k * a],
                                        [a / 2 + 0.43 * k * a, a / 2 - 0.43 * k * a ])

    pygame.draw.line(surface, DIMGREY, [a / 2, a / 2 - math.sqrt(2) * k * a / 3],
                                        [a / 2 + 0.18 * k * a, a / 2 - math.sqrt(2) * k * a / 3 - 0.18 * k * a])

    pygame.draw.line(surface, DIMGREY, [a / 2 + math.sqrt(2) * k * a / 3, a / 2],
                                        [a / 2 + math.sqrt(2) * k * a / 3 + 0.18 * k * a,
                                         a / 2 - 0.18 * k * a])

    pygame.draw.line(surface, DIMGREY, [a / 2 + math.sqrt(2) * k * a / 3 + 0.18 * k * a, a / 2 - 0.18 * k * a],
                                        [a / 2 + math.sqrt(2) * k * a / 3 + 0.18 * k * a - 0.19 * k * a,
                                         a / 2 - 0.18 * k * a - 0.19 * k * a])

    pygame.draw.line(surface, DIMGREY, [a / 2 + 0.18 * k * a, a / 2 - math.sqrt(2) * k * a / 3 - 0.18 * k * a],
                                        [a / 2 + 0.18 * k * a + 0.19 * k * a,
                                         a / 2 - math.sqrt(2) * k * a / 3 - 0.18 * k * a + 0.19 * k * a])

    # рисуем узорчок в левом верхнем угле
    pygame.draw.line(surface, DIMGREY, [a / 2 - k * a / 4 + k * a / 8, a / 2 - k * a / 4 - k * a / 8],
                     [a / 2 - k * a / 4 + k * a / 8 - k * a / 8,
                      a / 2 - k * a / 4 - k * a / 8 - k * a / 8])

    pygame.draw.line(surface, DIMGREY, [a / 2 - k * a / 4 - k * a / 8, a / 2 - k * a / 4 + k * a / 8],
                     [a / 2 - k * a / 4 - k * a / 8 - k * a / 8,
                      a / 2 - k * a / 4 + k * a / 8 - k * a / 8])

    pygame.draw.line(surface, DIMGREY, [a / 2 - k * a / 4 + k * a / 8 - k * a / 8,
                                        a / 2 - k * a / 4 - k * a / 8 - k * a / 8],
                     [a / 2 - k * a / 4 - k * a / 8 - k * a / 8,
                      a / 2 - k * a / 4 + k * a / 8 - k * a / 8])

    pygame.draw.line(surface, DIMGREY, [a / 2 - 0.37 * k * a + k * a / 20, a / 2 - 0.37 * k * a - k * a / 20],
                     [a / 2 - 0.37 * k * a + k * a / 20 - k * a / 8,
                      a / 2 - 0.37 * k * a - k * a / 20 - k * a / 8])

    pygame.draw.line(surface, DIMGREY, [a / 2 - 0.37 * k * a - k * a / 20, a / 2 - 0.37 * k * a + k * a / 20],
                     [a / 2 - 0.37 * k * a - k * a / 20 - k * a / 8,
                      a / 2 - 0.37 * k * a + k * a / 20 - k * a / 8])

    pygame.draw.line(surface, DIMGREY, [a / 2 - 0.37 * k * a + k * a / 20 - k * a / 8,
                                        a / 2 - 0.37 * k * a - k * a / 20 - k * a / 8],
                     [a / 2 - 0.37 * k * a - k * a / 20 - k * a / 8,
                      a / 2 - 0.37 * k * a + k * a / 20 - k * a / 8])
    pygame.draw.line(surface, DIMGREY, [a / 2 - 0.37 * k * a, a / 2 - 0.37 * k * a],
                     [a / 2 - 0.43 * k * a, a / 2 - 0.43 * k * a])

    pygame.draw.line(surface, DIMGREY, [a / 2, a / 2 - math.sqrt(2) * k * a / 3],
                     [a / 2 - 0.18 * k * a, a / 2 - math.sqrt(2) * k * a / 3 - 0.18 * k * a])

    pygame.draw.line(surface, DIMGREY, [a / 2 - math.sqrt(2) * k * a / 3, a / 2],
                     [a / 2 - math.sqrt(2) * k * a / 3 - 0.18 * k * a,
                      a / 2 - 0.18 * k * a])

    pygame.draw.line(surface, DIMGREY, [a / 2 - math.sqrt(2) * k * a / 3 - 0.18 * k * a, a / 2 - 0.18 * k * a],
                     [a / 2 - math.sqrt(2) * k * a / 3 - 0.18 * k * a + 0.19 * k * a,
                      a / 2 - 0.18 * k * a - 0.19 * k * a])

    pygame.draw.line(surface, DIMGREY, [a / 2 - 0.18 * k * a, a / 2 - math.sqrt(2) * k * a / 3 - 0.18 * k * a],
                     [a / 2 - 0.18 * k * a - 0.19 * k * a,
                      a / 2 - math.sqrt(2) * k * a / 3 - 0.18 * k * a + 0.19 * k * a])

    #рисуем узорчик в левом нижнем уголке

    pygame.draw.line(surface, DIMGREY, [a / 2 - k * a / 4 + k * a / 8, a / 2 + k * a / 4 + k * a / 8],
                     [a / 2 - k * a / 4 + k * a / 8 - k * a / 8,
                      a / 2 + k * a / 4 + k * a / 8 + k * a / 8])

    pygame.draw.line(surface, DIMGREY, [a / 2 - k * a / 4 - k * a / 8, a / 2 + k * a / 4 - k * a / 8],
                     [a / 2 - k * a / 4 - k * a / 8 - k * a / 8,
                      a / 2 + k * a / 4 - k * a / 8 + k * a / 8])

    pygame.draw.line(surface, DIMGREY, [a / 2 - k * a / 4 + k * a / 8 - k * a / 8,
                                        a / 2 + k * a / 4 + k * a / 8 + k * a / 8],
                     [a / 2 - k * a / 4 - k * a / 8 - k * a / 8,
                      a / 2 + k * a / 4 - k * a / 8 + k * a / 8])

    pygame.draw.line(surface, DIMGREY, [a / 2 - 0.37 * k * a + k * a / 20, a / 2 + 0.37 * k * a + k * a / 20],
                     [a / 2 - 0.37 * k * a + k * a / 20 - k * a / 8,
                      a / 2 + 0.37 * k * a + k * a / 20 + k * a / 8])

    pygame.draw.line(surface, DIMGREY, [a / 2 - 0.37 * k * a - k * a / 20, a / 2 + 0.37 * k * a - k * a / 20],
                     [a / 2 - 0.37 * k * a - k * a / 20 - k * a / 8,
                      a / 2 + 0.37 * k * a - k * a / 20 + k * a / 8])

    pygame.draw.line(surface, DIMGREY, [a / 2 - 0.37 * k * a + k * a / 20 - k * a / 8,
                                        a / 2 + 0.37 * k * a + k * a / 20 + k * a / 8],
                     [a / 2 - 0.37 * k * a - k * a / 20 - k * a / 8,
                      a / 2 + 0.37 * k * a - k * a / 20 + k * a / 8])
    pygame.draw.line(surface, DIMGREY, [a / 2 - 0.37 * k * a, a / 2 + 0.37 * k * a],
                     [a / 2 - 0.43 * k * a, a / 2 + 0.43 * k * a])

    pygame.draw.line(surface, DIMGREY, [a / 2, a / 2 + math.sqrt(2) * k * a / 3],
                     [a / 2 - 0.18 * k * a, a / 2 + math.sqrt(2) * k * a / 3 + 0.18 * k * a])

    pygame.draw.line(surface, DIMGREY, [a / 2 - math.sqrt(2) * k * a / 3, a / 2],
                     [a / 2 - math.sqrt(2) * k * a / 3 - 0.18 * k * a,
                      a / 2 + 0.18 * k * a])

    pygame.draw.line(surface, DIMGREY, [a / 2 - math.sqrt(2) * k * a / 3 - 0.18 * k * a, a / 2 + 0.18 * k * a],
                     [a / 2 - math.sqrt(2) * k * a / 3 - 0.18 * k * a + 0.19 * k * a,
                      a / 2 + 0.18 * k * a + 0.19 * k * a])

    pygame.draw.line(surface, DIMGREY, [a / 2 - 0.18 * k * a, a / 2 + math.sqrt(2) * k * a / 3 + 0.18 * k * a],
                     [a / 2 - 0.18 * k * a - 0.19 * k * a,
                      a / 2 + math.sqrt(2) * k * a / 3 + 0.18 * k * a - 0.19 * k * a])

    #рисуем узорчик в правом нижнем уголке

    pygame.draw.line(surface, DIMGREY, [a / 2 + k * a / 4 - k * a / 8, a / 2 + k * a / 4 + k * a / 8],
                     [a / 2 + k * a / 4 - k * a / 8 + k * a / 8,
                      a / 2 + k * a / 4 + k * a / 8 + k * a / 8])

    pygame.draw.line(surface, DIMGREY, [a / 2 + k * a / 4 + k * a / 8, a / 2 + k * a / 4 - k * a / 8],
                     [a / 2 + k * a / 4 + k * a / 8 + k * a / 8,
                      a / 2 + k * a / 4 - k * a / 8 + k * a / 8])

    pygame.draw.line(surface, DIMGREY, [a / 2 + k * a / 4 - k * a / 8 + k * a / 8,
                                        a / 2 + k * a / 4 + k * a / 8 + k * a / 8],
                     [a / 2 + k * a / 4 + k * a / 8 + k * a / 8,
                      a / 2 + k * a / 4 - k * a / 8 + k * a / 8])

    pygame.draw.line(surface, DIMGREY, [a / 2 + 0.37 * k * a - k * a / 20, a / 2 + 0.37 * k * a + k * a / 20],
                     [a / 2 + 0.37 * k * a - k * a / 20 + k * a / 8,
                      a / 2 + 0.37 * k * a + k * a / 20 + k * a / 8])

    pygame.draw.line(surface, DIMGREY, [a / 2 + 0.37 * k * a + k * a / 20, a / 2 + 0.37 * k * a - k * a / 20],
                     [a / 2 + 0.37 * k * a + k * a / 20 + k * a / 8,
                      a / 2 + 0.37 * k * a - k * a / 20 + k * a / 8])

    pygame.draw.line(surface, DIMGREY, [a / 2 + 0.37 * k * a - k * a / 20 + k * a / 8,
                                        a / 2 + 0.37 * k * a + k * a / 20 + k * a / 8],
                     [a / 2 + 0.37 * k * a + k * a / 20 + k * a / 8,
                      a / 2 + 0.37 * k * a - k * a / 20 + k * a / 8])
    pygame.draw.line(surface, DIMGREY, [a / 2 + 0.37 * k * a, a / 2 + 0.37 * k * a],
                     [a / 2 + 0.43 * k * a, a / 2 + 0.43 * k * a])

    pygame.draw.line(surface, DIMGREY, [a / 2, a / 2 + math.sqrt(2) * k * a / 3],
                     [a / 2 + 0.18 * k * a, a / 2 + math.sqrt(2) * k * a / 3 + 0.18 * k * a])

    pygame.draw.line(surface, DIMGREY, [a / 2 + math.sqrt(2) * k * a / 3, a / 2],
                     [a / 2 + math.sqrt(2) * k * a / 3 + 0.18 * k * a,
                      a / 2 + 0.18 * k * a])

    pygame.draw.line(surface, DIMGREY, [a / 2 + math.sqrt(2) * k * a / 3 + 0.18 * k * a, a / 2 + 0.18 * k * a],
                     [a / 2 + math.sqrt(2) * k * a / 3 + 0.18 * k * a - 0.19 * k * a,
                      a / 2 + 0.18 * k * a + 0.19 * k * a])

    pygame.draw.line(surface, DIMGREY, [a / 2 + 0.18 * k * a, a / 2 + math.sqrt(2) * k * a / 3 + 0.18 * k * a],
                     [a / 2 + 0.18 * k * a + 0.19 * k * a,
                      a / 2 + math.sqrt(2) * k * a / 3 + 0.18 * k * a - 0.19 * k * a])

    pygame.draw.lines(surface, DIMGREY, False, [[a / 2 - 0.3 * k * a, a / 2 + 0.9 * k * a - 0.3 * k * a ],
                      [a / 2, a / 2 + 0.9 * k * a ],
                      [a / 2 + 0.3 * k * a, a / 2 + 0.9 * k * a - 0.3 * k * a]])

    pygame.draw.lines(surface, DIMGREY, False, [[a / 2 - 0.3 * k * a, a / 2 - 0.9 * k * a + 0.3 * k * a],
                                                [a / 2, a / 2 - 0.9 * k * a],
                                                [a / 2 + 0.3 * k * a, a / 2 - 0.9 * k * a + 0.3 * k * a]])

    pygame.draw.lines(surface, DIMGREY, False, [[a / 2 - 0.9 * k * a + 0.3 * k * a, a / 2 - 0.3 * k * a],
                                                [a / 2 - 0.9 * k * a, a / 2],
                                                [a / 2 - 0.9 * k * a + 0.3 * k * a, a / 2 + 0.3 * k * a]])

    pygame.draw.lines(surface, DIMGREY, False, [[a / 2 + 0.9 * k * a - 0.3 * k * a, a / 2 - 0.3 * k * a],
                                                [a / 2 + 0.9 * k * a, a / 2],
                                                [a / 2 + 0.9 * k * a - 0.3 * k * a, a / 2 + 0.3 * k * a]])

    draw2(a, GOLD, 4, surface, k, math.pi / 4)




    surf.blit(surface, (x, y), special_flags=pygame.BLEND_RGBA_MIN)

def blue_chip(a, surf, color, k, x, y):
    '''
    функция рисует синию фишку с орнаментом
    :param a: размер ячейки
    :param color: цвет основы ячейки
    :param surf: экран, куда отображается плоскость
    :param k: масштаб изображения внутри ячейкм
    :param x: положение ячейки на экране по оси x
    :param y: положение ячейки на экране по оси y
    '''

    surface = pygame.Surface((a, a), pygame.SRCALPHA, 32)
    surface.fill(color)

    draw1(a, ROYALBLUE, BLUE, 6, surface, k, math.pi / 6)


    pygame.draw.circle(surface, DIMGREY, (int(a / 2), int(a / 2)), int(k * a / 8) , 1 )

    for i in range(0,6,1):
        pygame.draw.lines(surface, DIMGREY, False, [[a / 2 + k * a / 8 * math.sin(math.pi * i / 3),
                                                    a / 2 - k * a / 8 * math.cos(math.pi * i / 3)],
                                                    [a / 2 + (k * a / 8 + k * a / 16) * math.sin(math.pi * i/ 3) +
                                                    k * a / 40 * math.cos(math.pi * i/ 3),
                                                     a / 2 - (k * a / 8 + k * a / 16) * math.cos(math.pi * i/ 3) +
                                                    k * a / 40 * math.sin(math.pi * i/ 3)],
                                                    [a / 2 + k * a / 4 * math.sin(math.pi * i/ 3),
                                                    a / 2 - k * a / 4 * math.cos(math.pi * i/ 3)]])

    # рисуем "палочки" в узорах
    for i in range(0,6,1):
        pygame.draw.line(surface, DIMGREY, [a / 2 - 0.98 * k * a * math.sin(i * math.pi / 3),
                                            a / 2 + 0.98 * k * a * math.cos(i * math.pi / 3)],
                                            [a / 2 - 0.56 * k * a * math.sin(i * math.pi / 3),
                                             a / 2 + 0.56 * k * a * math.cos(i * math.pi / 3)])
    #дуги нижний угол
    pygame.draw.arc(surface, DIMGREY, (a / 2 - k * a / 3, a / 2 + 0.45 * k * a, k * a / 3, k * a / 3), 0, -1.7)

    pygame.draw.arc(surface, DIMGREY, (a / 2 , a / 2 + 0.45 * k * a, k * a / 3, k * a / 3), - math.pi + 1.7, - math.pi)


    #дуги верхний угол
    pygame.draw.arc(surface, DIMGREY, (a / 2 - k * a / 3, a / 2 - 0.45 * k * a - k * a / 3,
                                       k * a / 3, k * a / 3), 1.7, 0)

    pygame.draw.arc(surface, DIMGREY, (a / 2, a / 2 - 0.45 * k * a - k * a / 3,
                                       k * a / 3, k * a / 3), math.pi, math.pi - 1.7)

    #дуги левый нижний угол
    pygame.draw.arc(surface, DIMGREY, (a / 2 - 0.56*k*a, a / 2 + 0.26 * k * a, k * a / 3, k * a / 3),
                    -math.pi + 0.65, 5 / 6 *math.pi)

    pygame.draw.arc(surface, DIMGREY, (a / 2 - 0.73 * k * a, a / 2  - 0.02 * k * a, k * a / 3, k * a / 3),
                    -1.05, 4.25)

    #дуги левый верхний угол
    pygame.draw.arc(surface, DIMGREY, (a / 2 - 0.58 * k * a, a / 2 - 0.59 * k * a, k * a / 3, k * a / 3),
                    -2.09, 2.49)

    pygame.draw.arc(surface, DIMGREY, (a / 2 - 0.73 * k * a, a / 2 - 0.31 * k * a, k * a / 3, k * a / 3),
                    -3.54, 1.05)
    #дуги правый верхний угол
    pygame.draw.arc(surface, DIMGREY, (a / 2 + 0.26 * k * a, a / 2 - 0.58 * k * a, k * a / 3, k * a / 3),
                    0.65, 5.24)

    pygame.draw.arc(surface, DIMGREY, (a / 2 + 0.44 * k * a, a / 2 - 0.32 * k * a, k * a / 3, k * a / 3),
                    - 4.19, 0.65)
    #дуги правый нижний угол
    pygame.draw.arc(surface, DIMGREY, (a / 2 + 0.40 * k * a, a / 2 -0.02 * k * a, k * a / 3, k * a / 3),
                    -0.39, 4.19)

    pygame.draw.arc(surface, DIMGREY, (a / 2 + 0.26 * k * a, a / 2 + 0.27 * k * a, k * a / 3, k * a / 3),
                    1.05, 5.89)

    pygame.draw.circle(surface, BLUE, (int(a / 2), int(a / 2)), int(k * a / 3), 2)
    surf.blit(surface, (x, y), special_flags=pygame.BLEND_RGBA_MIN)

def orange_chip(a, surf, color, k, y):
    '''
    функция рисует оранжевую фишку с орнаментом
    :param a: размер ячейки
    :param color: цвет основы ячейки
    :param surf: экран, куда отображается плоскость
    :param k: масштаб изображения внутри ячейкм
    :param x: положение ячейки на экране по оси x
    :param y: положение ячейки на экране по оси y
     '''

    surface = pygame.Surface((a, a), pygame.SRCALPHA, 32)
    surface.fill(color)

    







purple_chip(100, screen, WHITE, 0.45, 100, 200)

red_chip(200, screen, WHITE, 0.4, 500, 400)

yellow_chip(200, screen, WHITE, 0.3, 600, 100)

blue_chip(500, screen, WHITE, 0.1, 200, 100 )

pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()