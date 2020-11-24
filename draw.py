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

SILVER = (192, 192, 192)
GRAY = (169, 169,169)

GREEN = (0, 255, 0)
DARKGREEN = (0, 100, 0)

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


    pygame.draw.line(surface, DIMGREY, [int(a / 2 - k * a / 3), int(a / 2 - k * a / 7)],
                     [int(a / 2 + k * a / 7), int(a / 2 - k * a / 7)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - k * a / 7), int(a / 2 + k * a / 3)],
                     [int(a / 2 - k * a / 7), int(a / 2 - k * a / 7)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + k * a / 7), int(a / 2 + k * a / 7)],
                     [int(a / 2 + k * a / 7), int(a / 2 - k * a / 3)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + k * a / 3), int(a / 2 + k * a / 7)],
                     [int(a / 2 - k * a / 7), int(a / 2 + k * a / 7)])

    pygame.draw.lines(surface, DIMGREY, False,
                      [[int(a / 2 + k * a / 3), int(a / 2 + 4 * k * a / 5)],
                       [int(a / 2 - k * a / 3), int(a / 2 + 4 * k * a / 5)],
                       [int(a / 2 - k * a / 3), int(a / 2 + 2 * k * a / 5)],
                       [int(a / 2 + k * a / 3), int(a / 2 + 2 * k * a / 5)],
                       [int(a / 2 + k * a / 3), int(a / 2 + 3.5 * k * a / 5)],
                       [int(a / 2 - 1 * k * a / 5), int(a / 2 + 3.5 * k * a / 5)],
                       [int(a / 2 - 1 * k * a / 5), int(a / 2 + 2.5 * k * a / 5)],
                       [int(a / 2 + 1 * k * a / 5), int(a / 2 + 2.5 * k * a / 5)],
                       [int(a / 2 + 1 * k * a / 5), int(a / 2 + 3 * k * a / 5)],
                       [int(a / 2), int(a / 2 + 3 * k * a / 5)]])

    pygame.draw.lines(surface, DIMGREY, False,
                      [[int(a / 2 - k * a / 3), int(a / 2 - 4 * k * a / 5)],
                       [int(a / 2 + k * a / 3), int(a / 2 - 4 * k * a / 5)],
                       [int(a / 2 + k * a / 3), int(a / 2 - 2 * k * a / 5)],
                       [int(a / 2 - k * a / 3), int(a / 2 - 2 * k * a / 5)],
                       [int(a / 2 - k * a / 3), int(a / 2 - 3.5 * k * a / 5)],
                       [int(a / 2 + 1 * k * a / 5), int(a / 2 - 3.5 * k * a / 5)],
                       [int(a / 2 + 1 * k * a / 5), int(a / 2 - 2.5 * k * a / 5)],
                       [int(a / 2 - 1 * k * a / 5), int(a / 2 - 2.5 * k * a / 5)],
                       [int(a / 2 - 1 * k * a / 5), int(a / 2 - 3 * k * a / 5)],
                       [int(a / 2), int(a / 2 - 3 * k * a / 5)]])

    pygame.draw.lines(surface, DIMGREY, False,
                      [[int(a / 2 - 4 * k * a / 5), int(a / 2 + k * a / 3)],
                       [int(a / 2 - 4 * k * a / 5), int(a / 2 - k * a / 3)],
                       [int(a / 2 - 2 * k * a / 5), int(a / 2 - k * a / 3)],
                       [int(a / 2 - 2 * k * a / 5), int(a / 2 + k * a / 3)],
                       [int(a / 2 - 3.5 * k * a / 5), int(a / 2 + k * a / 3)],
                       [int(a / 2 - 3.5 * k * a / 5), int(a / 2 - 1 * k * a / 5)],
                       [int(a / 2 - 2.5 * k * a / 5), int(a / 2 - 1 * k * a / 5)],
                       [int(a / 2 - 2.5 * k * a / 5), int(a / 2 + 1 * k * a / 5)],
                       [int(a / 2 - 3 * k * a / 5), int(a / 2 + 1 * k * a / 5)],
                       [int(a / 2 - 3 * k * a / 5), int(a / 2)]])

    pygame.draw.lines(surface, DIMGREY, False,
                      [[int(a / 2 + 4 * k * a / 5), int(a / 2 - k * a / 3)],
                       [int(a / 2 + 4 * k * a / 5), int(a / 2 + k * a / 3)],
                       [int(a / 2 + 2 * k * a / 5), int(a / 2 + k * a / 3)],
                       [int(a / 2 + 2 * k * a / 5), int(a / 2 - k * a / 3)],
                       [int(a / 2 + 3.5 * k * a / 5), int(a / 2 - k * a / 3)],
                       [int(a / 2 + 3.5 * k * a / 5), int(a / 2 + 1 * k * a / 5)],
                       [int(a / 2 + 2.5 * k * a / 5), int(a / 2 + 1 * k * a / 5)],
                       [int(a / 2 + 2.5 * k * a / 5), int(a / 2 - 1 * k * a / 5)],
                       [int(a / 2 + 3 * k * a / 5), int(a / 2 - 1 * k * a / 5)],
                       [int(a / 2 + 3 * k * a / 5), int(a / 2)]])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - 4 * k * a / 5), int(a / 2 - 2 * k * a / 5)],
                     [int(a / 2 - 2 * k * a / 5), int(a / 2 - 4 * k * a / 5)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - 3 * k * a / 5), int(a / 2 - 2 * k * a / 5)],
                     [int(a / 2 - 2 * k * a / 5), int(a / 2 - 3 * k * a / 5)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + 4 * k * a / 5), int(a / 2 - 2 * k * a / 5)],
                     [int(a / 2 + 2 * k * a / 5), int(a / 2 - 4 * k * a / 5)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + 3 * k * a / 5), int(a / 2 - 2 * k * a / 5)],
                     [int(a / 2 + 2 * k * a / 5), int(a / 2 - 3 * k * a / 5)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + 4 * k * a / 5), int(a / 2 + 2 * k * a / 5)],
                     [int(a / 2 + 2 * k * a / 5), int(a / 2 + 4 * k * a / 5)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + 3 * k * a / 5), int(a / 2 + 2 * k * a / 5)],
                     [int(a / 2 + 2 * k * a / 5), int(a / 2 + 3 * k * a / 5)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - 4 * k * a / 5), int(a / 2 + 2 * k * a / 5)],
                     [int(a / 2 - 2 * k * a / 5), int(a / 2 + 4 * k * a / 5)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - 3 * k * a / 5), int(a / 2 + 2 * k * a / 5)],
                     [int(a / 2 - 2 * k * a / 5), int(a / 2 + 3 * k * a / 5)])

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

    pygame.draw.line(surface, DIMGREY, [int(a / 2), int(a / 2 + 4.7 * k * a / 5)],
                     [int(a / 2), int(a / 2 + 3.2 * k * a / 5)])

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - k * a / 3), int(a / 2 + k * a / 3), int(k * a / 3),
                                       int(2 * (3.2 / 5 - 1 / 3) * k * a)), 0, math.pi / 2)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2),  int(a / 2 + k * a / 3), int(k * a / 3),
                                       int(2 * (3.2 / 5 - 1 / 3) * k * a)), math.pi / 2, -math.pi)


    pygame.draw.line(surface, DIMGREY, [int(a / 2), int(a / 2 - 4.7 * k * a / 5)],
                     [int(a / 2), int(a / 2 - 3.2 * k * a / 5)])

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - k * a / 3), int(a / 2 - k * a / 3 - 2 * (3.2 / 5 - 1 / 3) * k * a),
                                       int(k * a / 3),
                                       int(2 * (3.2 / 5 - 1 / 3) * k * a)), 3 / 2 * math.pi , 0)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2), int(a / 2 - k * a / 3 - 2 * (3.2 / 5 - 1 / 3) * k * a),
                                       int(k * a / 3), int(2 * (3.2 / 5 - 1 / 3) * k * a)), math.pi , -math.pi / 2)



    pygame.draw.line(surface, DIMGREY, [int(a / 2 + 4.7 * k * a / 5), int(a / 2)],
                     [int(a / 2 + 3.2 * k * a / 5), int(a / 2)])

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + k * a / 3), int(a / 2 - k * a / 3),
                                       int(2 * (3.2 / 5 - 1 / 3) * k * a), int(k * a / 3)), math.pi, - math.pi / 2)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + k * a / 3), int(a / 2 ), int(2 * (3.2 / 5 - 1 / 3) * k * a),
                                       int(k * a / 3)), math.pi / 2, -math.pi)


    pygame.draw.line(surface, DIMGREY, [int(a / 2 - 4.7 * k * a / 5), int(a / 2)],
                     [int(a / 2 - 3.2 * k * a / 5), int(a / 2)])

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - k * a / 3 - 2 * (3.2 / 5 - 1 / 3) * k * a),
                                       int(a / 2 - k * a / 3), int(2 * (3.2 / 5 - 1 / 3) * k * a),
                                       int(k * a / 3)), 3 / 2 * math.pi, 0)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - k * a / 3 - 2 * (3.2 / 5 - 1 / 3) * k * a),
                                       int(a / 2), int(2 * (3.2 / 5 - 1 / 3) * k * a),
                                       int(k * a / 3)), 0, - 3 / 2 * math.pi)


    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - k * a / 3), int(a / 2 - 2 * k * a / 3), int(k * a / 3),
                                       int(2 * k * a / 3)), math.pi / 2, -math.pi)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 2 * k * a / 3), int(a / 2 - k * a / 3), int(2 * k * a / 3),
                                       int(k * a / 3)), math.pi / 2, -math.pi  )

    pygame.draw.circle(surface, DIMGREY, (int(a / 2 - k * a / 1.7), int(a / 2 - k * a / 1.7)), int(k * a / 8), 1)


    pygame.draw.arc(surface, DIMGREY, (int(a / 2), int(a / 2 - 2 * k * a / 3), int(k * a / 3),
                                       int(2 * k * a / 3)), 0, - 3 / 2 * math.pi)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2), int(a / 2 - k * a / 3), int(2 * k * a / 3),
                                       int(k * a / 3)), 0, -3 / 2 * math.pi)

    pygame.draw.circle(surface, DIMGREY, (int(a / 2 + k * a / 1.7), int(a / 2 - k * a / 1.7)), int(k * a / 8), 1)


    pygame.draw.arc(surface, DIMGREY, (int(a / 2), int(a / 2), int(2 * k * a / 3),
                                       int(k * a / 3)), 3 /2 * math.pi, 0)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2), int(a / 2), int(k * a / 3),
                                       int(2 * k * a / 3)), 3 / 2 * math.pi, 0)

    pygame.draw.circle(surface, DIMGREY, (int(a / 2 + k * a / 1.7), int(a / 2 + k * a / 1.7)), int(k * a / 8), 1)


    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - k * a / 3), int(a / 2), int(k * a / 3),
                                       int(2 * k * a / 3)), math.pi , - math. pi / 2)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 2 / 3 * k * a), int(a / 2), int(2 * k * a / 3),
                                       int(k * a / 3)), math.pi,  - math.pi / 2)

    pygame.draw.circle(surface, DIMGREY, (int(a / 2 - k * a / 1.7), int(a / 2 + k * a / 1.7)), int(k * a / 8), 1)

    pygame.draw.circle(surface, DIMGREY,(int(a /2), int(a / 2)), int(k * a / 20))

    pygame.draw.circle(surface, DIMGREY, (int(a / 2), int(a / 2)), int(k * a / 8), 1)

    m = 20 #коэффициент, регулирующий угол наклона лучиков

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + (k * a / 8) * math.sin(math.pi / m)),
                                        int(a / 2 + (k * a / 8) * math.cos(math.pi / m))],
                                        [int(a / 2 + k * a / 3 * math.tan(math.pi / m)), int(a / 2 + k * a / 3)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - (k * a / 8) * math.sin(math.pi / m)),
                                        int(a / 2 + (k * a / 8) * math.cos(math.pi / m))],
                                        [int(a / 2 - k * a / 3 * math.tan(math.pi / m)), int(a / 2 + k * a / 3)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - (k * a / 8) * math.sin(math.pi / m)),
                                        int(a / 2 - (k * a / 8) * math.cos(math.pi / m))],
                                        [int(a / 2 - k * a / 3 * math.tan(math.pi / m)), int(a / 2 - k * a / 3)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + (k * a / 8) * math.sin(math.pi / m)),
                                        int(a / 2 - (k * a / 8) * math.cos(math.pi / m))],
                                        [int(a / 2 + k * a / 3 * math.tan(math.pi / m)), int(a / 2 - k * a / 3)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + (k * a / 8) * math.cos(math.pi / m)),
                                        int(a / 2 - (k * a / 8) * math.sin(math.pi / m))],
                                        [int(a / 2 + k * a / 3), int(a / 2 - k * a / 3 * math.tan(math.pi / m))])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + (k * a / 8) * math.cos(math.pi / m)),
                                        int(a / 2 + (k * a / 8) * math.sin(math.pi / m))],
                                        [int(a / 2 + k * a / 3), int(a / 2 + k * a / 3 * math.tan(math.pi / m))])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - (k * a / 8) * math.cos(math.pi / m)),
                                        int(a / 2 - (k * a / 8) * math.sin(math.pi / m))],
                                        [int(a / 2 - k * a / 3), int(a / 2 - k * a / 3 * math.tan(math.pi / m))])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - (k * a / 8) * math.cos(math.pi / m)),
                                        int(a / 2 + (k * a / 8) * math.sin(math.pi / m))],
                                        [int(a / 2 - k * a / 3), int(a / 2 + k * a / 3 * math.tan(math.pi / m))])


    pygame.draw.line(surface, DIMGREY, [int(a / 2 + k * a / 4), int(a /2 + k * a /4)],
                                        [int(a /2 + k * a / 4), int(a / 2 + k * a / 3)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + k * a / 4), int(a / 2 + k * a / 4)],
                                        [int(a / 2 + k * a / 3), int(a / 2 + k * a / 4)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - k * a / 4), int(a / 2 + k * a / 4)],
                                        [int(a / 2 - k * a / 4), int(a / 2 + k * a / 3)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - k * a / 4), int(a / 2 + k * a / 4)],
                     [int(a / 2 - k * a / 3), int(a / 2 + k * a / 4)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - k * a / 4), int(a / 2 - k * a / 4)],
                     [int(a / 2 - k * a / 4), int(a / 2 - k * a / 3)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - k * a / 4), int(a / 2 - k * a / 4)],
                     [int(a / 2 - k * a / 3), int(a / 2 - k * a / 4)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + k * a / 4), int(a / 2 - k * a / 4)],
                     [int(a / 2 + k * a / 4), int(a / 2 - k * a / 3)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + k * a / 4), int(a / 2 - k * a / 4)],
                     [int(a / 2 + k * a / 3), int(a / 2 - k * a / 4)])

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

    pygame.draw.line(surface, DIMGREY, [int(a / 2), int(a / 2 + k * a /6)], [int(a / 2), int(a / 2 + k * a / 3)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2), int(a / 2 - k * a / 6)], [int(a / 2), int(a / 2 - k * a / 3)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - k * a /6), int(a / 2)], [int(a / 2 - k * a / 3), int(a / 2)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + k * a / 6), int(a / 2)], [int(a / 2 + k * a / 3), int(a / 2)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + k * a / 7), int(a / 2 - k * a / 7)],
                                        [int(a / 2 + k * a / 4), int(a / 2 - k * a / 4)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - k * a / 7), int(a / 2 - k * a / 7)],
                                        [int(a / 2 - k * a / 4), int(a / 2 - k * a / 4)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + k * a / 7), int(a / 2 + k * a / 7)],
                                        [int(a / 2 + k * a / 4), int(a / 2 + k * a / 4)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - k * a / 7), int(a / 2 + k * a / 7)],
                                        [int(a / 2 - k * a / 4), int(a / 2 + k * a / 4)])


    #рисуем узорчик в правом верхнем углу

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + k * a / 4 - k * a / 8), int(a / 2 - k * a / 4 - k * a / 8)],
                                        [int(a / 2 + k * a /4 - k * a / 8 + k * a / 8),
                                         int(a / 2 - k * a / 4 - k * a / 8 - k * a / 8)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + k * a / 4 + k * a / 8), int(a / 2 - k * a / 4 + k * a / 8)],
                                        [int(a / 2 + k * a / 4 + k * a / 8 + k * a / 8),
                                        int(a / 2 - k * a / 4 + k * a / 8 - k * a / 8)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + k * a /4 - k * a / 8 + k * a / 8),
                                        int(a / 2 - k * a / 4 - k * a / 8 - k * a / 8)],
                                        [int(a / 2 + k * a / 4 + k * a / 8 + k * a / 8),
                                        int(a / 2 - k * a / 4 + k * a / 8 - k * a / 8)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + 0.37 * k * a - k * a / 20), int(a / 2 - 0.37 * k * a - k * a / 20)],
                                        [int(a / 2 + 0.37 * k * a - k * a / 20 + k * a / 8),
                                        int(a / 2 - 0.37 * k * a - k * a / 20 - k * a / 8)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + 0.37 * k * a + k * a / 20), int(a / 2 - 0.37 * k * a + k * a / 20)],
                                        [int(a / 2 + 0.37 * k * a + k * a / 20 + k * a / 8),
                                        int(a / 2 - 0.37 * k * a + k * a / 20 - k * a / 8)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + 0.37 * k * a - k * a / 20 + k * a / 8),
                                        int(a / 2 - 0.37 * k * a - k * a / 20 - k * a / 8)],
                                        [int(a / 2 + 0.37 * k * a + k * a / 20 + k * a / 8),
                                        int(a / 2 - 0.37 * k * a + k * a / 20 - k * a / 8)])
    pygame.draw.line(surface, DIMGREY, [int(a / 2 + 0.37 * k * a), int(a / 2 - 0.37 * k * a)],
                                        [int(a / 2 + 0.43 * k * a), int(a / 2 - 0.43 * k * a)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2), int(a / 2 - math.sqrt(2) * k * a / 3)],
                                        [int(a / 2 + 0.18 * k * a),
                                         int(a / 2 - math.sqrt(2) * k * a / 3 - 0.18 * k * a)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + math.sqrt(2) * k * a / 3), int(a / 2)],
                                        [int(a / 2 + math.sqrt(2) * k * a / 3 + 0.18 * k * a),
                                         int(a / 2 - 0.18 * k * a)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + math.sqrt(2) * k * a / 3 + 0.18 * k * a),
                                        int(a / 2 - 0.18 * k * a)],
                                        [int(a / 2 + math.sqrt(2) * k * a / 3 + 0.18 * k * a - 0.19 * k * a),
                                         int(a / 2 - 0.18 * k * a - 0.19 * k * a)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + 0.18 * k * a),
                                        int(a / 2 - math.sqrt(2) * k * a / 3 - 0.18 * k * a)],
                                        [int(a / 2 + 0.18 * k * a + 0.19 * k * a),
                                         int(a / 2 - math.sqrt(2) * k * a / 3 - 0.18 * k * a + 0.19 * k * a)])

    # рисуем узорчок в левом верхнем угле
    pygame.draw.line(surface, DIMGREY, [int(a / 2 - k * a / 4 + k * a / 8), int(a / 2 - k * a / 4 - k * a / 8)],
                     [int(a / 2 - k * a / 4 + k * a / 8 - k * a / 8),
                      int(a / 2 - k * a / 4 - k * a / 8 - k * a / 8)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - k * a / 4 - k * a / 8), int(a / 2 - k * a / 4 + k * a / 8)],
                     [int(a / 2 - k * a / 4 - k * a / 8 - k * a / 8),
                      int(a / 2 - k * a / 4 + k * a / 8 - k * a / 8)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - k * a / 4 + k * a / 8 - k * a / 8),
                                        int(a / 2 - k * a / 4 - k * a / 8 - k * a / 8)],
                     [int(a / 2 - k * a / 4 - k * a / 8 - k * a / 8),
                      int(a / 2 - k * a / 4 + k * a / 8 - k * a / 8)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - 0.37 * k * a + k * a / 20),
                                        int(a / 2 - 0.37 * k * a - k * a / 20)],
                     [int(a / 2 - 0.37 * k * a + k * a / 20 - k * a / 8),
                      int(a / 2 - 0.37 * k * a - k * a / 20 - k * a / 8)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - 0.37 * k * a - k * a / 20), int(a / 2 - 0.37 * k * a + k * a / 20)],
                     [int(a / 2 - 0.37 * k * a - k * a / 20 - k * a / 8),
                      int(a / 2 - 0.37 * k * a + k * a / 20 - k * a / 8)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - 0.37 * k * a + k * a / 20 - k * a / 8),
                                        int(a / 2 - 0.37 * k * a - k * a / 20 - k * a / 8)],
                     [int(a / 2 - 0.37 * k * a - k * a / 20 - k * a / 8),
                      int(a / 2 - 0.37 * k * a + k * a / 20 - k * a / 8)])
    pygame.draw.line(surface, DIMGREY, [int(a / 2 - 0.37 * k * a), int(a / 2 - 0.37 * k * a)],
                     [int(a / 2 - 0.43 * k * a), int(a / 2 - 0.43 * k * a)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2), int(a / 2 - math.sqrt(2) * k * a / 3)],
                     [int(a / 2 - 0.18 * k * a), int(a / 2 - math.sqrt(2) * k * a / 3 - 0.18 * k * a)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - math.sqrt(2) * k * a / 3), int(a / 2)],
                     [int(a / 2 - math.sqrt(2) * k * a / 3 - 0.18 * k * a),
                      int(a / 2 - 0.18 * k * a)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - math.sqrt(2) * k * a / 3 - 0.18 * k * a),
                                        int(a / 2 - 0.18 * k * a)],
                     [int(a / 2 - math.sqrt(2) * k * a / 3 - 0.18 * k * a + 0.19 * k * a),
                      int(a / 2 - 0.18 * k * a - 0.19 * k * a)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - 0.18 * k * a),
                                        int(a / 2 - math.sqrt(2) * k * a / 3 - 0.18 * k * a)],
                     [int(a / 2 - 0.18 * k * a - 0.19 * k * a),
                      int(a / 2 - math.sqrt(2) * k * a / 3 - 0.18 * k * a + 0.19 * k * a)])

    #рисуем узорчик в левом нижнем уголке

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - k * a / 4 + k * a / 8), int(a / 2 + k * a / 4 + k * a / 8)],
                     [int(a / 2 - k * a / 4 + k * a / 8 - k * a / 8),
                      int(a / 2 + k * a / 4 + k * a / 8 + k * a / 8)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - k * a / 4 - k * a / 8), int(a / 2 + k * a / 4 - k * a / 8)],
                     [int(a / 2 - k * a / 4 - k * a / 8 - k * a / 8),
                      int(a / 2 + k * a / 4 - k * a / 8 + k * a / 8)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - k * a / 4 + k * a / 8 - k * a / 8),
                                        int(a / 2 + k * a / 4 + k * a / 8 + k * a / 8)],
                     [int(a / 2 - k * a / 4 - k * a / 8 - k * a / 8),
                      int(a / 2 + k * a / 4 - k * a / 8 + k * a / 8)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - 0.37 * k * a + k * a / 20), int(a / 2 + 0.37 * k * a + k * a / 20)],
                     [int(a / 2 - 0.37 * k * a + k * a / 20 - k * a / 8),
                      int(a / 2 + 0.37 * k * a + k * a / 20 + k * a / 8)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - 0.37 * k * a - k * a / 20), int(a / 2 + 0.37 * k * a - k * a / 20)],
                     [int(a / 2 - 0.37 * k * a - k * a / 20 - k * a / 8),
                      int(a / 2 + 0.37 * k * a - k * a / 20 + k * a / 8)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - 0.37 * k * a + k * a / 20 - k * a / 8),
                                        int(a / 2 + 0.37 * k * a + k * a / 20 + k * a / 8)],
                     [int(a / 2 - 0.37 * k * a - k * a / 20 - k * a / 8),
                      int(a / 2 + 0.37 * k * a - k * a / 20 + k * a / 8)])
    pygame.draw.line(surface, DIMGREY, [int(a / 2 - 0.37 * k * a), int(a / 2 + 0.37 * k * a)],
                     [int(a / 2 - 0.43 * k * a), int(a / 2 + 0.43 * k * a)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2), int(a / 2 + math.sqrt(2) * k * a / 3)],
                     [int(a / 2 - 0.18 * k * a), int(a / 2 + math.sqrt(2) * k * a / 3 + 0.18 * k * a)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - math.sqrt(2) * k * a / 3), int(a / 2)],
                     [int(a / 2 - math.sqrt(2) * k * a / 3 - 0.18 * k * a),
                      int(a / 2 + 0.18 * k * a)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - math.sqrt(2) * k * a / 3 - 0.18 * k * a),
                                        int(a / 2 + 0.18 * k * a)],
                     [int(a / 2 - math.sqrt(2) * k * a / 3 - 0.18 * k * a + 0.19 * k * a),
                      int(a / 2 + 0.18 * k * a + 0.19 * k * a)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - 0.18 * k * a),
                                        int(a / 2 + math.sqrt(2) * k * a / 3 + 0.18 * k * a)],
                     [int(a / 2 - 0.18 * k * a - 0.19 * k * a),
                      int(a / 2 + math.sqrt(2) * k * a / 3 + 0.18 * k * a - 0.19 * k * a)])

    #рисуем узорчик в правом нижнем уголке

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + k * a / 4 - k * a / 8), int(a / 2 + k * a / 4 + k * a / 8)],
                     [int(a / 2 + k * a / 4 - k * a / 8 + k * a / 8),
                      int(a / 2 + k * a / 4 + k * a / 8 + k * a / 8)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + k * a / 4 + k * a / 8), int(a / 2 + k * a / 4 - k * a / 8)],
                     [int(a / 2 + k * a / 4 + k * a / 8 + k * a / 8),
                      int(a / 2 + k * a / 4 - k * a / 8 + k * a / 8)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + k * a / 4 - k * a / 8 + k * a / 8),
                                        int(a / 2 + k * a / 4 + k * a / 8 + k * a / 8)],
                     [int(a / 2 + k * a / 4 + k * a / 8 + k * a / 8),
                      int(a / 2 + k * a / 4 - k * a / 8 + k * a / 8)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + 0.37 * k * a - k * a / 20), int(a / 2 + 0.37 * k * a + k * a / 20)],
                     [int(a / 2 + 0.37 * k * a - k * a / 20 + k * a / 8),
                      int(a / 2 + 0.37 * k * a + k * a / 20 + k * a / 8)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + 0.37 * k * a + k * a / 20), int(a / 2 + 0.37 * k * a - k * a / 20)],
                     [int(a / 2 + 0.37 * k * a + k * a / 20 + k * a / 8),
                      int(a / 2 + 0.37 * k * a - k * a / 20 + k * a / 8)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + 0.37 * k * a - k * a / 20 + k * a / 8),
                                        int(a / 2 + 0.37 * k * a + k * a / 20 + k * a / 8)],
                     [int(a / 2 + 0.37 * k * a + k * a / 20 + k * a / 8),
                      int(a / 2 + 0.37 * k * a - k * a / 20 + k * a / 8)])
    pygame.draw.line(surface, DIMGREY, [int(a / 2 + 0.37 * k * a), int(a / 2 + 0.37 * k * a)],
                     [int(a / 2 + 0.43 * k * a), int(a / 2 + 0.43 * k * a)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2), int(a / 2 + math.sqrt(2) * k * a / 3)],
                     [int(a / 2 + 0.18 * k * a), int(a / 2 + math.sqrt(2) * k * a / 3 + 0.18 * k * a)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + math.sqrt(2) * k * a / 3), int(a / 2)],
                     [int(a / 2 + math.sqrt(2) * k * a / 3 + 0.18 * k * a),
                      int(a / 2 + 0.18 * k * a)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + math.sqrt(2) * k * a / 3 + 0.18 * k * a),
                                        int(a / 2 + 0.18 * k * a)],
                     [int(a / 2 + math.sqrt(2) * k * a / 3 + 0.18 * k * a - 0.19 * k * a),
                      int(a / 2 + 0.18 * k * a + 0.19 * k * a)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + 0.18 * k * a),
                                        int(a / 2 + math.sqrt(2) * k * a / 3 + 0.18 * k * a)],
                     [int(a / 2 + 0.18 * k * a + 0.19 * k * a),
                      int(a / 2 + math.sqrt(2) * k * a / 3 + 0.18 * k * a - 0.19 * k * a)])

    pygame.draw.lines(surface, DIMGREY, False, [[int(a / 2 - 0.3 * k * a), int(a / 2 + 0.9 * k * a - 0.3 * k * a)],
                      [int(a / 2), int(a / 2 + 0.9 * k * a)],
                      [int(a / 2 + 0.3 * k * a), int(a / 2 + 0.9 * k * a - 0.3 * k * a)]])

    pygame.draw.lines(surface, DIMGREY, False, [[int(a / 2 - 0.3 * k * a), int(a / 2 - 0.9 * k * a + 0.3 * k * a)],
                                                [int(a / 2), int(a / 2 - 0.9 * k * a)],
                                                [int(a / 2 + 0.3 * k * a), int(a / 2 - 0.9 * k * a + 0.3 * k * a)]])

    pygame.draw.lines(surface, DIMGREY, False, [[int(a / 2 - 0.9 * k * a + 0.3 * k * a), int(a / 2 - 0.3 * k * a)],
                                                [int(a / 2 - 0.9 * k * a), int(a / 2)],
                                                [int(a / 2 - 0.9 * k * a + 0.3 * k * a), int(a / 2 + 0.3 * k * a)]])

    pygame.draw.lines(surface, DIMGREY, False, [[int(a / 2 + 0.9 * k * a - 0.3 * k * a), int(a / 2 - 0.3 * k * a)],
                                                [int(a / 2 + 0.9 * k * a), int(a / 2)],
                                                [int(a / 2 + 0.9 * k * a - 0.3 * k * a), int(a / 2 + 0.3 * k * a)]])

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
        pygame.draw.lines(surface, DIMGREY, False, [[int(a / 2 + k * a / 8 * math.sin(math.pi * i / 3)),
                                                    int(a / 2 - k * a / 8 * math.cos(math.pi * i / 3))],
                                                    [int(a / 2 + (k * a / 8 + k * a / 16) * math.sin(math.pi * i/ 3) +
                                                    k * a / 40 * math.cos(math.pi * i/ 3)),
                                                     int(a / 2 - (k * a / 8 + k * a / 16) * math.cos(math.pi * i/ 3) +
                                                    k * a / 40 * math.sin(math.pi * i/ 3))],
                                                    [int(a / 2 + k * a / 4 * math.sin(math.pi * i/ 3)),
                                                    int(a / 2 - k * a / 4 * math.cos(math.pi * i/ 3))]])

    # рисуем "палочки" в узорах
    for i in range(0,6,1):
        pygame.draw.line(surface, DIMGREY, [int(a / 2 - 0.98 * k * a * math.sin(i * math.pi / 3)),
                                            int(a / 2 + 0.98 * k * a * math.cos(i * math.pi / 3))],
                                            [int(a / 2 - 0.56 * k * a * math.sin(i * math.pi / 3)),
                                             int(a / 2 + 0.56 * k * a * math.cos(i * math.pi / 3))])
    #дуги нижний угол
    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - k * a / 3), int(a / 2 + 0.45 * k * a),
                                       int(k * a / 3), int(k * a / 3)), 0, -1.7)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2), int(a / 2 + 0.45 * k * a), int(k * a / 3), int(k * a / 3)), - math.pi + 1.7, - math.pi)


    #дуги верхний угол
    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - k * a / 3), int(a / 2 - 0.45 * k * a - k * a / 3),
                                       int(k * a / 3), int(k * a / 3)), 1.7, 0)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2), int(a / 2 - 0.45 * k * a - k * a / 3),
                                       int(k * a / 3), int(k * a / 3)), math.pi, math.pi - 1.7)

    #дуги левый нижний угол
    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.56 * k * a), int(a / 2 + 0.26 * k * a),
                                       int(k * a / 3), int(k * a / 3)), - math.pi + 0.65, 5 / 6 *math.pi)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.73 * k * a), int(a / 2  - 0.02 * k * a),
                                       int(k * a / 3), int(k * a / 3)),-1.05, 4.25)

    #дуги левый верхний угол
    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.58 * k * a), int(a / 2 - 0.59 * k * a),
                                       int(k * a / 3), int(k * a / 3)), -2.09, 2.49)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.73 * k * a), int(a / 2 - 0.31 * k * a),
                                       int(k * a / 3), int(k * a / 3)), -3.54, 1.05)
    #дуги правый верхний угол
    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.26 * k * a), int(a / 2 - 0.58 * k * a),
                                       int(k * a / 3), int(k * a / 3)), 0.65, 5.24)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.44 * k * a), int(a / 2 - 0.32 * k * a),
                                       int(k * a / 3), int(k * a / 3)), - 4.19, 0.65)
    #дуги правый нижний угол
    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.40 * k * a), int(a / 2 -0.02 * k * a),
                                       int(k * a / 3), int(k * a / 3)), -0.39, 4.19)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.26 * k * a), int(a / 2 + 0.27 * k * a),
                                       int(k * a / 3), int(k * a / 3)), 1.05, 5.89)

    pygame.draw.circle(surface, BLUE, (int(a / 2), int(a / 2)), int(math.sqrt(2) * k * a / 3), 2)
    surf.blit(surface, (x, y), special_flags=pygame.BLEND_RGBA_MIN)

def orange_chip(a, surf, color, k, x, y):
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

    pygame.draw.circle(surface, DARKORANGE, (int(a / 2), int(a / 2)), int(k * a))
    pygame.draw.circle(surface, color, (int(a / 2 + k * a * 1.65), int(a / 2)), int(k * a))
    pygame.draw.circle(surface, color, (int(a / 2 - k * a * 1.65), int(a / 2)), int(k * a))

    pygame.draw.arc(surface, ORANGERED, (int(a / 2 - k * a), int(a / 2 - k * a),
                                       int(2 * k * a ), int(2 * k * a )), 0.62, 2.52, 3)

    pygame.draw.arc(surface, ORANGERED, (int(a / 2 - k * a), int(a / 2 - k * a),
                                         int(2 * k * a), int(2 * k * a)), -2.52, -0.62, 3)

    pygame.draw.arc(surface, ORANGERED, (int(a / 2 + 0.65 * k * a), int(a / 2 - k * a),
                                         int(2 * k * a), int(2 * k * a)), -3.74, -2.54, 3)

    pygame.draw.arc(surface, ORANGERED, (int(a / 2 - 2.65 * k * a), int(a / 2 - k * a),
                                         int(2 * k * a), int(2 * k * a)), -0.6, 0.6, 3)



    #узор посередине справа
    pygame.draw.line(surface, DIMGREY, [int(a / 2 + 0.45 * k * a), int(a / 2 - 0.23 * k * a)],
                     [int(a / 2 + 0.45 * k * a), int(a / 2 + 0.23 * k * a)])

    pygame.draw.arc(surface, DIMGREY, (int(a / 2  + 0.45 * k * a), int(a / 2 - 0.23 * k * a),
                                         int(0.14 * k * a), int(0.14 * k * a)), -1.57, 1.57)
    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.45 * k * a), int(a / 2 - 0.08 * k * a),
                                       int(0.14 * k * a), int(0.14 * k * a)), -1.57, 1.57)
    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.45 * k * a), int(a / 2 + 0.07 * k * a),
                                       int(0.14 * k * a), int(0.14 * k * a)), -1.57, 1.57)



    #узор посередине слева
    pygame.draw.line(surface, DIMGREY, [int(a / 2 - 0.45 * k * a), int(a / 2 - 0.23 * k * a)],
                     [int(a / 2 - 0.45 * k * a), int(a / 2 + 0.23 * k * a)])

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.59 * k * a), int(a / 2 - 0.23 * k * a),
                                       int(0.14 * k * a), int(0.14 * k * a)), 1.57, 4.71)
    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.59 * k * a), int(a / 2 - 0.08 * k * a),
                                       int(0.14 * k * a), int(0.14 * k * a)), 1.57, 4.71)
    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.59 * k * a), int(a / 2 + 0.07 * k * a),
                                       int(0.14 * k * a), int(0.14 * k * a)), 1.57, 4.71)
    #центральный узор

    pygame.draw.circle(surface, DIMGREY, (int(a / 2), int(a / 2 + 0.2 * k * a)), int(0.1 * k * a), 1)
    pygame.draw.circle(surface, DIMGREY, (int(a / 2), int(a / 2 - 0.2 * k * a)), int(0.1 * k * a), 1)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.2 * k * a), int(a / 2 - 0.44 * k * a),
                                       int(0.4 * k * a), int(0.4 * k * a)), -3.14, 0)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.2 * k * a), int(a / 2 +0.04 * k * a),
                                       int(0.4 * k * a), int(0.4 * k * a)), 0, 3.13)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.3 * k * a), int(a / 2 - 0.1 * k * a),
                                       int(0.2 * k * a), int(0.2 * k * a)), 1.9, 4.5)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.1 * k * a), int(a / 2 - 0.1 * k * a),
                                       int(0.2 * k * a), int(0.2 * k * a)), -1.2, 1.2)

    #верхний узор
    pygame.draw.line(surface, DIMGREY, [int(a / 2), int(a / 2 - 0.55 * k * a)],
                     [int(a / 2 + 0.43 * k * a), int(a / 2 - 0.32 * k * a )])

    pygame.draw.line(surface, DIMGREY, [int(a / 2), int(a / 2 - 0.55 * k * a)],
                     [int(a / 2 - 0.43 * k * a), int(a / 2 - 0.32 * k * a)])

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.62 * k * a), int(a / 2 - 0.62 * k * a),
                                       int(0.3 * k * a), int(0.3 * k * a)), 0.5, 5.5)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.32 * k * a), int(a / 2 - 0.62 * k * a),
                                       int(0.3 * k * a), int(0.3 * k * a)), -1.65, 2.64)

    pygame.draw.lines(surface, DIMGREY, True,
                      [[int(a / 2 - 0.4 * k * a), int(a / 2 - 0.8 * k * a)],
                       [int(a / 2 - 0.25 * k * a), int(a / 2 - 0.6 * k * a)],
                       [int(a / 2 - 0.1 * k * a), int(a / 2 - 0.8 * k * a)]])
    pygame.draw.lines(surface, DIMGREY, True,
                      [[int(a / 2 + 0.4 * k * a), int(a / 2 - 0.8 * k * a)],
                       [int(a / 2 + 0.25 * k * a), int(a / 2 - 0.6 * k * a)],
                       [int(a / 2 + 0.1 * k * a), int(a / 2 - 0.8 * k * a)]])


    #нижний узор
    pygame.draw.line(surface, DIMGREY, [int(a / 2), int(a / 2 + 0.55 * k * a)],
                     [int(a / 2 + 0.43 * k * a), int(a / 2 + 0.32 * k * a)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2), int(a / 2 + 0.55 * k * a)],
                     [int(a / 2 - 0.43 * k * a), int(a / 2 + 0.32 * k * a)])

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.62 * k * a), int(a / 2 + 0.33 * k * a),
                                       int(0.3 * k * a), int(0.3 * k * a)), -5.45, -0.5)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.32 * k * a), int(a / 2 + 0.33 * k * a),
                                       int(0.3 * k * a), int(0.3 * k * a)), -2.72, 1.81)

    pygame.draw.lines(surface, DIMGREY, True,
                      [[int(a / 2 - 0.4 * k * a), int(a / 2 + 0.8 * k * a)],
                       [int(a / 2 - 0.25 * k * a), int(a / 2 + 0.6 * k * a)],
                       [int(a / 2 - 0.1 * k * a), int(a / 2 + 0.8 * k * a)]])
    pygame.draw.lines(surface, DIMGREY, True,
                      [[int(a / 2 + 0.4 * k * a), int(a / 2 + 0.8 * k * a)],
                       [int(a / 2 + 0.25 * k * a), int(a / 2 + 0.6 * k * a)],
                       [int(a / 2 + 0.1 * k * a), int(a / 2 + 0.8 * k * a)]])

    draw2(a, ORANGERED, 6, surface, k, math.pi / 6)

    surf.blit(surface, (x, y), special_flags=pygame.BLEND_RGBA_MIN)

def grey_chip(a, surf, color, k, x, y):
    '''
    функция рисует серую фишку с орнаментом
    :param a: размер ячейки
    :param color: цвет основы ячейки
    :param surf: экран, куда отображается плоскость
    :param k: масштаб изображения внутри ячейкм
    :param x: положение ячейки на экране по оси x
    :param y: положение ячейки на экране по оси y
    '''
    surface = pygame.Surface((a, a), pygame.SRCALPHA, 32)
    surface.fill(color)

    draw1(a, SILVER, GRAY, 4, surface, k, 0)

    #центральный узор
    pygame.draw.circle(surface, DIMGREY, (int(a / 2), int(a / 2)), int(0.1 * k * a), 1)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.2 * k * a), int(a / 2 - 0.2 * k * a),
                                       int(0.4 * k * a ), int(0.4 * k * a)), -1.0, 4.38)

    pygame.draw.lines(surface, DIMGREY, False, [[int(a / 2 - 0.1 * k * a), int(a / 2 + 0.18 * k * a)],
                                                [int(a / 2 - 0.15 * k * a), int(a / 2 + 0.33 * k * a)],
                                                [int(a / 2 - 0.21 * k * a), int(a / 2 + 0.33 * k * a)],
                                                [int(a / 2 - 0.16 * k * a ), int(a /2 + 0.21 * k * a)],
                                                [int(a /2 - 0.24 * k * a), int(a / 2 + 0.30 * k * a)],
                                                [int(a / 2 - 0.31 * k * a), int(a / 2 + 0.22 * k * a)],
                                                [int(a / 2 - 0.22 * k * a), int(a / 2 + 0.14 * k * a)],
                                                [int(a / 2 - 0.38 * k * a), int(a / 2 + 0.15 * k * a)],
                                                [int(a / 2 - 0.40 * k * a), int(a / 2 + 0.04 * k * a)],
                                                [int(a / 2 - 0.25 * k * a), int(a / 2 + 0.02 * k * a)],
                                                [int(a / 2 - 0.38 * k * a), int(a / 2 - 0.05 * k * a)],
                                                [int(a / 2 - 0.32 * k * a), int(a / 2 - 0.17 * k * a)],
                                                [int(a / 2 - 0.22 * k * a ), int(a / 2 - 0.12 * k * a)],
                                                [int(a / 2 - 0.29 * k * a), int(a / 2 - 0.26 * k * a)],
                                                [int(a / 2 - 0.20 * k * a), int(a / 2 - 0.32 * k * a)],
                                                [int(a / 2 - 0.13 * k * a), int(a / 2 - 0.22 * k * a)],
                                                [int(a / 2 - 0.11 * k * a), int(a / 2 - 0.38 * k * a)],
                                                [int(a / 2 - 0.01 * k * a), int(a / 2 - 0.38 * k * a)],
                                                [int(a / 2 + 0.01 * k * a), int(a / 2 - 0.23 * k * a)],
                                                [int(a / 2 + 0.08 * k * a), int(a / 2 - 0.36 * k * a)],
                                                [int(a / 2 + 0.15 * k * a), int(a / 2 - 0.34 * k * a)],
                                                [int(a / 2 + 0.13 * k * a), int(a / 2 - 0.20 * k * a)],
                                                [int(a / 2 + 0.29 * k * a), int(a / 2 - 0.23 * k * a)],
                                                [int(a / 2 + 0.31 * k * a), int(a / 2 - 0.15 * k * a)],
                                                [int(a / 2 + 0.22 * k * a), int(a / 2 - 0.10 * k * a)],
                                                [int(a / 2 + 0.34 * k * a), int(a / 2 - 0.11 * k * a)],
                                                [int(a / 2 + 0.34 * k * a), int(a / 2 - 0.01 * k * a)],
                                                [int(a / 2 + 0.25 * k * a), int(a / 2 + 0.02 * k * a)],
                                                [int(a / 2 + 0.35 * k * a), int(a / 2 + 0.08 * k * a)],
                                                [int(a / 2 + 0.31 * k * a), int(a / 2 + 0.16 * k * a)],
                                                [int(a / 2 + 0.23 * k * a), int(a / 2 + 0.14 * k * a)],
                                                [int(a / 2 + 0.3 * k* a), int(a / 2 + 0.21 * k * a)],
                                                [int(a / 2 + 0.24 * k * a), int(a / 2 + 0.28 * k * a)],
                                                [int(a / 2 + 0.18 * k * a), int(a / 2 + 0.23 * k * a)],
                                                [int(a / 2 + 0.20 * k * a), int(a / 2 + 0.31 * k * a)],
                                                [int(a / 2 + 0.16 * k * a), int(a / 2 + 0.33 * k * a)],
                                                [int(a / 2 + 0.11 * k * a), int(a /2 + 0.17 * k * a)]])

    pygame.draw.circle(surface, DIMGREY, (int(a / 2 - 0.06 * k * a), int(a / 2 + 0.31 * k * a)), int(0.04 * k * a))
    pygame.draw.circle(surface, DIMGREY, (int(a / 2 + 0.06 * k * a), int(a / 2 + 0.31 * k * a)), int(0.04 * k * a))

    # узор в левой нижней части
    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.62 * k * a), int(a / 2 + 0.31 * k * a),
                                       int(0.3 * k * a), int(0.3 * k * a)), 1.57, 4.71)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.56 * k * a), int(a / 2 + 0.31 * k * a),
                                       int(0.2 * k * a), int(0.2 * k * a)), -1.57, 1.57)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.48 * k * a), int(a / 2 + 0.40 * k * a),
                                       int(0.1 * k * a), int(0.1 * k * a)), 1.57, 4.71)

    pygame.draw.lines(surface, DIMGREY, False,
                      [[int(a / 2 - 0.49 * k * a), int(a / 2 + 0.59 * k * a)],
                       [int(a / 2 - 0.29 * k * a), int(a / 2 + 0.59 * k * a)],
                       [int(a / 2 - 0.29 * k * a), int(a / 2 + 0.49 * k * a)],
                       [int(a / 2 - 0.45 * k * a), int(a / 2 + 0.49 * k * a)]])

    pygame.draw.lines(surface, DIMGREY, True,
                      [[int(a / 2 - 0.26 * k * a), int(a / 2 + 0.49 * k * a)],
                       [int(a / 2 - 0.18 * k * a), int(a / 2 + 0.48 * k * a)],
                       [int(a / 2 - 0.17 * k * a), int(a / 2 + 0.59 * k * a)],
                       [int(a / 2 - 0.25 * k * a), int(a / 2 + 0.59 * k * a)]])

    pygame.draw.lines(surface, DIMGREY, True,
                      [[int(a / 2 - 0.14 * k * a), int(a / 2 + 0.48 * k * a)],
                       [int(a / 2 - 0.02 * k * a), int(a / 2 + 0.49 * k * a)],
                       [int(a / 2 - 0.02 * k * a), int(a / 2 + 0.60 * k * a)],
                       [int(a / 2 - 0.13 * k * a), int(a / 2 + 0.59 * k * a)]])

    pygame.draw.lines(surface, DIMGREY, True,
                      [[int(a / 2 + 0.03 * k * a), int(a / 2 + 0.49 * k * a)],
                       [int(a / 2 + 0.16 * k * a), int(a / 2 + 0.53 * k * a)],
                       [int(a / 2 + 0.16 * k * a), int(a / 2 + 0.63 * k * a)],
                       [int(a / 2 + 0.03 * k * a), int(a / 2 + 0.60 * k * a)]])
    #узор в верхней правой части

    pygame.draw.lines(surface, DIMGREY, False,
                      [[int(a / 2 + 0.49 * k * a), int(a / 2 - 0.59 * k * a)],
                       [int(a / 2 + 0.29 * k * a), int(a / 2 - 0.59 * k * a)],
                       [int(a / 2 + 0.29 * k * a), int(a / 2 - 0.49 * k * a)],
                       [int(a / 2 + 0.45 * k * a), int(a / 2 - 0.49 * k * a)]])

    pygame.draw.lines(surface, DIMGREY, True,
                      [[int(a / 2 + 0.26 * k * a), int(a / 2 - 0.49 * k * a)],
                       [int(a / 2 + 0.18 * k * a), int(a / 2 - 0.48 * k * a)],
                       [int(a / 2 + 0.17 * k * a), int(a / 2 - 0.59 * k * a)],
                       [int(a / 2 + 0.25 * k * a), int(a / 2 - 0.59 * k * a)]])

    pygame.draw.lines(surface, DIMGREY, True,
                      [[int(a / 2 + 0.14 * k * a), int(a / 2 - 0.48 * k * a)],
                       [int(a / 2 + 0.02 * k * a), int(a / 2 - 0.49 * k * a)],
                       [int(a / 2 + 0.02 * k * a), int(a / 2 - 0.60 * k * a)],
                       [int(a / 2 + 0.13 * k * a), int(a / 2 - 0.59 * k * a)]])

    pygame.draw.lines(surface, DIMGREY, True,
                      [[int(a / 2 - 0.03 * k * a), int(a / 2 - 0.49 * k * a)],
                       [int(a / 2 - 0.16 * k * a), int(a / 2 - 0.53 * k * a)],
                       [int(a / 2 - 0.16 * k * a), int(a / 2 - 0.63 * k * a)],
                       [int(a / 2 - 0.03 * k * a), int(a / 2 - 0.60 * k * a)]])

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.32 * k * a), int(a / 2 - 0.6 * k * a),
                                       int(0.3 * k * a), int(0.3 * k * a)), -1.57, 1.57)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.36 * k * a), int(a / 2 - 0.5 * k * a),
                                       int(0.2 * k * a), int(0.2 * k * a)), 1.57, 4.71)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.38 * k * a), int(a / 2 - 0.50 * k * a),
                                       int(0.1 * k * a), int(0.1 * k * a)), - 1.57, 1.57)

    #узор в левой верхней части

    pygame.draw.lines(surface, DIMGREY, False,
                      [[int(a / 2 - 0.59 * k * a), int(a / 2 - 0.49 * k * a)],
                       [int(a / 2 - 0.59 * k * a), int(a / 2 - 0.29 * k * a)],
                       [int(a / 2 - 0.49 * k * a), int(a / 2 - 0.29 * k * a)],
                       [int(a / 2 - 0.49 * k * a), int(a / 2 - 0.45 * k * a)]])

    pygame.draw.lines(surface, DIMGREY, True,
                      [[int(a / 2 - 0.49 * k * a), int(a / 2 - 0.26 * k * a)],
                       [int(a / 2 - 0.48 * k * a), int(a / 2 - 0.18 * k * a)],
                       [int(a / 2 - 0.59 * k * a), int(a / 2 - 0.17 * k * a)],
                       [int(a / 2 - 0.59 * k * a), int(a / 2 - 0.25 * k * a)]])

    pygame.draw.lines(surface, DIMGREY, True,
                      [[int(a / 2 - 0.48 * k * a), int(a / 2 - 0.14 * k * a)],
                       [int(a / 2 - 0.49 * k * a), int(a / 2 - 0.02 * k * a)],
                       [int(a / 2 - 0.60 * k * a), int(a / 2 - 0.02 * k * a)],
                       [int(a / 2 - 0.59 * k * a), int(a / 2 - 0.13 * k * a)]])

    pygame.draw.lines(surface, DIMGREY, True,
                      [[int(a / 2 - 0.49 * k * a), int(a / 2 + 0.03 * k * a)],
                       [int(a / 2 - 0.53 * k * a), int(a / 2 + 0.16 * k * a )],
                       [int(a / 2 - 0.63 * k * a), int(a / 2 + 0.16 * k * a)],
                       [int(a / 2 - 0.60 * k * a), int(a / 2 + 0.03 * k * a)]])

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.60 * k * a), int(a / 2 - 0.58 * k * a),
                                       int(0.3 * k * a), int(0.3 * k * a)), 0, 3.14)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.48 * k * a), int(a / 2 - 0.55 * k * a),
                                       int(0.2 * k * a), int(0.2 * k * a)), - 3.14, 0)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.48 * k * a), int(a / 2 - 0.49 * k * a),
                                       int(0.1 * k * a), int(0.1 * k * a)), 0, 3.14)

    #узор в правой нижней части

    pygame.draw.lines(surface, DIMGREY, False,
                      [[int(a / 2 + 0.59 * k * a), int(a / 2 + 0.49 * k * a)],
                       [int(a / 2 + 0.59 * k * a), int(a / 2 + 0.29 * k * a)],
                       [int(a / 2 + 0.49 * k * a), int(a / 2 + 0.29 * k * a)],
                       [int(a / 2 + 0.49 * k * a), int(a / 2 + 0.45 * k * a)]])

    pygame.draw.lines(surface, DIMGREY, True,
                      [[int(a / 2 + 0.49 * k * a), int(a / 2 + 0.26 * k * a)],
                       [int(a / 2 + 0.48 * k * a), int(a / 2 + 0.18 * k * a)],
                       [int(a / 2 + 0.59 * k * a), int(a / 2 + 0.17 * k * a)],
                       [int(a / 2 + 0.59 * k * a), int(a / 2 + 0.25 * k * a)]])

    pygame.draw.lines(surface, DIMGREY, True,
                      [[int(a / 2 + 0.48 * k * a), int(a / 2 + 0.14 * k * a)],
                       [int(a / 2 + 0.49 * k * a), int(a / 2 + 0.02 * k * a)],
                       [int(a / 2 + 0.60 * k * a), int(a / 2 + 0.02 * k * a)],
                       [int(a / 2 + 0.59 * k * a), int(a / 2 + 0.13 * k * a)]])

    pygame.draw.lines(surface, DIMGREY, True,
                      [[int(a / 2 + 0.49 * k * a), int(a / 2 - 0.03 * k * a)],
                       [int(a / 2 + 0.53 * k * a), int(a / 2 - 0.16 * k * a)],
                       [int(a / 2 + 0.63 * k * a), int(a / 2 - 0.16 * k * a)],
                       [int(a / 2 + 0.60 * k * a), int(a / 2 - 0.03 * k * a)]])

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.31 * k * a), int(a / 2 + 0.29 * k * a),
                                       int(0.3 * k * a), int(0.3 * k * a)), - 3.14, 0)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.31 * k * a), int(a / 2 + 0.35 * k * a),
                                       int(0.2 * k * a), int(0.2 * k * a)), 0, 3.14)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.40 * k * a), int(a / 2 + 0.39 * k * a),
                                       int(0.1 * k * a), int(0.1 * k * a)), - 3.14, 0)

    draw2(a, GRAY, 8, surface, k, 0)

    surf.blit(surface, (x, y), special_flags=pygame.BLEND_RGBA_MIN)

def green_chip(a, surf, color, k, x, y):
    '''
    функция рисует серую зелёную фишку с орнаментом
    :param a: размер ячейки
    :param color: цвет основы ячейки
    :param surf: экран, куда отображается плоскость
    :param k: масштаб изображения внутри ячейкм
    :param x: положение ячейки на экране по оси x
    :param y: положение ячейки на экране по оси y
    '''
    surface = pygame.Surface((a, a), pygame.SRCALPHA, 32)
    surface.fill(color)

    draw1(a, GREEN, DARKGREEN, 4, surface, k, math.pi / 4)

    #центральный узор
    pygame.draw.lines(surface, DIMGREY, True, [[int(a / 2), int(a / 2 - 0.1 * k * a)],
                                                [int(a / 2 + 0.1 * k * a), int(a / 2 )],
                                                [int(a / 2), int(a / 2 + 0.1 * k * a)],
                                               [int(a / 2 - 0.1 * k * a), int(a / 2)]])

    pygame.draw.circle(surface, DIMGREY, (int(a / 2 - 0.2 * k * a), int(a / 2 - 0.2 * k * a)), int(0.08 * k * a),1)

    pygame.draw.circle(surface, DIMGREY, (int(a / 2 + 0.2 * k * a), int(a / 2 - 0.2 * k * a)), int(0.08 * k * a), 1)

    pygame.draw.circle(surface, DIMGREY, (int(a / 2 - 0.2 * k * a), int(a / 2 + 0.2 * k * a)), int(0.08 * k * a), 1)

    pygame.draw.circle(surface, DIMGREY, (int(a / 2 + 0.2 * k * a), int(a / 2 + 0.2 * k * a)), int(0.08 * k * a), 1)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.06 * k * a), int(a / 2 - 0.4 * k * a),
                                       int(0.3* k * a), int(0.4 * k * a)), -1.57, 0)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.06 * k * a), int(a / 2 - 0.01 * k * a),
                                       int(0.3 * k * a), int(0.4 * k * a)), 0, 1.57)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.36 * k * a), int(a / 2 - 0.4 * k * a),
                                       int(0.3 * k * a), int(0.4 * k * a)), -3.14, -1.57)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.36 * k * a), int(a / 2 - 0.01 * k * a),
                                       int(0.3 * k * a), int(0.4 * k * a)), 1.57, 3.14)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.4 * k * a), int(a / 2 - 0.35 * k * a),
                                       int(0.4 * k * a), int(0.3 * k * a)), 0, 1.57)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.0 * k * a), int(a / 2 - 0.35 * k * a),
                                       int(0.4 * k * a), int(0.3 * k * a)), 1.57, 3.14)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.4 * k * a), int(a / 2 + 0.05 * k * a),
                                       int(0.4 * k * a), int(0.3 * k * a)), -1.57, 0)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.0 * k * a), int(a / 2 + 0.05 * k * a),
                                       int(0.4 * k * a), int(0.3 * k * a)), -3.14, -1.57)

    #верхний узор
    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.15 * k * a), int(a / 2 - 0.8 * k * a),
                                       int(0.3 * k * a), int(0.3 * k * a)), -1.57, 1.57)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.1 * k * a), int(a / 2 - 0.8 * k * a),
                                       int(0.2 * k * a), int(0.2 * k * a)), - 4.71, - 1.57)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.08 * k * a), int(a / 2 - 0.75 * k * a),
                                       int(0.16 * k * a), int(0.16 * k * a)), - 1.57, 1.57)

    pygame.draw.line(surface, DIMGREY, [int(a / 2), int(a / 2 - 0.52 * k * a)],
                     [int(a / 2 - 0.4 * k * a), int(a / 2 - 0.52 * k * a)])

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.46 * k * a), int(a / 2 - 0.52 * k * a),
                                       int(0.22 * k * a), int(0.22 * k * a)), 1.57, 4.71)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.42 * k * a), int(a / 2 - 0.44 * k * a),
                                       int(0.14 * k * a), int(0.14 * k * a)), - 1.57, 1.57)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.40 * k * a), int(a / 2 - 0.43 * k * a),
                                       int(0.08 * k * a), int(0.08 * k * a)), 1.57, 4.71)

    #нижний узор
    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.15 * k * a), int(a / 2 + 0.52 * k * a),
                                       int(0.3 * k * a), int(0.3 * k * a)), 1.57, 4.71)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.1 * k * a), int(a / 2 + 0.6 * k * a),
                                       int(0.2 * k * a), int(0.2 * k * a)), - 1.57, 1.57)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.08 * k * a), int(a / 2 + 0.61 * k * a),
                                       int(0.16 * k * a), int(0.16 * k * a)), 1.57, 4.71)

    pygame.draw.line(surface, DIMGREY, [int(a / 2), int(a / 2 + 0.52 * k * a)],
                     [int(a / 2 + 0.4 * k * a), int(a / 2 + 0.52 * k * a)])

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.29 * k * a), int(a / 2 + 0.33 * k * a),
                                       int(0.22 * k * a), int(0.22 * k * a)), - 1.57, 1.57)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.33 * k * a), int(a / 2 + 0.34 * k * a),
                                       int(0.14 * k * a), int(0.14 * k * a)), 1.57, 4.71)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.34 * k * a), int(a / 2 + 0.39 * k * a),
                                       int(0.08 * k * a), int(0.08 * k * a)), -1.57, 1.57)

    #левый узор

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.82 * k * a), int(a / 2 - 0.15 * k * a),
                                       int(0.3 * k * a), int(0.3 * k * a)), 0, 3.14)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.8 * k * a), int(a / 2 - 0.1 * k * a),
                                       int(0.2 * k * a), int(0.2 * k * a)), - 3.14, 0)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.77 * k * a), int(a / 2 - 0.08 * k * a),
                                       int(0.16 * k * a), int(0.16 * k * a)), 0, 3.14)

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - 0.52 * k * a), int(a / 2)],
                     [int(a / 2 - 0.52 * k * a), int(a / 2 + 0.4 * k * a)])

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.52 * k * a), int(a / 2 + 0.29 * k * a),
                                       int(0.22 * k * a), int(0.22 * k * a)), - 3.14, 0)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.47 * k * a), int(a / 2 + 0.33 * k * a),
                                       int(0.14 * k * a), int(0.14 * k * a)), 0, 3.14)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.47 * k * a), int(a / 2 + 0.34 * k * a),
                                       int(0.08 * k * a), int(0.08 * k * a)), - 3.14, 0)

    #правый узор

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.52 * k * a), int(a / 2 - 0.15 * k * a),
                                       int(0.3 * k * a), int(0.3 * k * a)), -3.14, 0)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.6 * k * a), int(a / 2 - 0.1 * k * a),
                                       int(0.2 * k * a), int(0.2 * k * a)), 0, 3.14)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.61 * k * a), int(a / 2 - 0.08 * k * a),
                                       int(0.16 * k * a), int(0.16 * k * a)), -3.14, 0)

    pygame.draw.line(surface, DIMGREY, [int(a / 2 +  0.52 * k * a), int(a / 2)],
                     [int(a / 2 + 0.52 * k * a), int(a / 2 - 0.4 * k * a)])

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.3 * k * a), int(a / 2 - 0.51 * k * a),
                                       int(0.22 * k * a), int(0.22 * k * a)), 0, 3.14)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.32 * k * a), int(a / 2 - 0.47 * k * a),
                                       int(0.14 * k * a), int(0.14 * k * a)), - 3.14, 0)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.37 * k * a), int(a / 2 - 0.43 * k * a),
                                       int(0.08 * k * a), int(0.08 * k * a)), 0, 3.14)

    draw2(a, DARKGREEN, 8, surface, k, 0)

    surf.blit(surface, (x, y), special_flags=pygame.BLEND_RGBA_MIN)


red_chip(100, screen, WHITE, 0.4, 500, 400)

yellow_chip(100, screen, WHITE, 0.4, 600, 100)

blue_chip(100, screen, WHITE, 0.4, 200, 100 )

orange_chip(100, screen, WHITE, 0.4, 100, 100)

purple_chip(100, screen, WHITE, 0.4, 100, 200)

grey_chip(100, screen, WHITE, 0.4, 100, 400)

green_chip(100, screen, WHITE, 0.4, 200, 300)
pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()