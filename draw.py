#прорисовка объектов
import pygame, sys
from random import randint
from pygame.draw import *
import math

DIMGREY = (105, 105, 105)

RED = (255, 0, 0)
CRIMSON = (220, 20, 60)
SALMON = (250, 128, 114)
DARKRED = (139, 0, 0)

PURPLE = (128, 0, 128)
INDIGO = (75, 0, 130)
PLUM = 	(221, 160, 221)

YELLOW = (255, 255, 0)
GOLD = (255, 215, 0)
KHAKI = (240, 230, 140)
GOLDENROD = (218, 165, 32)
LEMONCHIFFON = (255, 250, 205)

ROYALBLUE = (65, 105, 225)
BLUE = (0, 0, 255)

DARKORANGE = (255, 140, 0)
ORANGERED = (255, 69, 0)
ORANGE = (255, 165, 0)

SILVER = (192, 192, 192)
GRAY = (169, 169,169)

GREEN = (0, 255, 0)
DARKGREEN = (0, 100, 0)

CADETBLUE = (95, 158, 160)

TURQUOISE = (64, 224, 208)
AQUAMARINE = (127, 255, 212)
DARKTURQIOSE = (0, 206, 209)

LIGHTBLUE = (173, 216, 230)
DARKGOLDENROD = (184, 134, 11)

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
def red_stone(a, surf, x, y):
    '''
    рисуем камень в красной фишке
    :param a: характерный размер камня
    :param surf: поверхность отрисовки камня
    :param x: координата центра по оси x
    :param y: координата центра по оси y
    '''


    list = []  # лист для координат вершин n-угольника

    u = 2 * math.pi / 4
    for i in range(0, 5, 1):
        list.append((int(x + 0.87 * a * math.sin(u / 2 + u * i)),
                     int(y + 0.87 * a * math.cos(u / 2 + u * i))))
    pygame.draw.polygon(surf, TURQUOISE, list)

    pygame.draw.line(surf, AQUAMARINE, list[1], list[3], 3)
    pygame.draw.line(surf, AQUAMARINE, list[0], list[2], 3)
    pygame.draw.arc(surf, DARKTURQIOSE, [int(x - 1.38 * a), int(y - 0.7 * a), int(1 * a), int(1.4 * a)],
                    - 1.06, 1.06, 2)
    pygame.draw.arc(surf, DARKTURQIOSE, [int(x + 0.39 * a), int(y - 0.7 * a), int(1 * a), int(1.4 * a)],
                    2.14, 4.18, 2)
    pygame.draw.arc(surf, DARKTURQIOSE, [int(x - 0.7 * a), int(y - 1.37 * a), int(1.4 * a), int(1 * a)],
                    -2.60, - 0.49, 2)
    pygame.draw.arc(surf, DARKTURQIOSE, [int(x - 0.7 * a), int(y + 0.38 * a), int(1.4 * a), int(1 * a)],
                    0.54, 2.6, 2)
    pygame.draw.circle(surf, AQUAMARINE, (int(x), int(y)), int(0.3 * a))



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
def purple_stone(a, surf, x, y):
    '''
    рисуем камень в фиолетовой фишке
    :param a: характерный размер камня
    :param surf: поверхность отрисовки камня
    :param x: координата центра по оси x
    :param y: координата центра по оси y
    '''

    list = []  # лист для координат вершин n-угольника

    u = 2 * math.pi / 4
    for i in range(0, 5, 1):
        list.append((int(x + 0.87 * a * math.sin(u / 2 + u * i)),
                     int(y + 0.87 * a * math.cos(u / 2 + u * i))))

    pygame.draw.polygon(surf, PLUM, list)
    pygame.draw.circle(surf, LIGHTBLUE, (int(x), int(y)), int(0.3 * a))

    pygame.draw.line(surf, LIGHTBLUE, (int(x), int(y)), (int(x + 0.45 * a), int(y - 0.62 * a)))
    pygame.draw.line(surf, LIGHTBLUE, (int(x), int(y)), (int(x + 0.62 * a), int(y - 0.45 * a)))

    pygame.draw.line(surf, LIGHTBLUE, (int(x), int(y)), (int(x + 0.45 * a), int(y + 0.62 * a)))
    pygame.draw.line(surf, LIGHTBLUE, (int(x), int(y)), (int(x + 0.62 * a), int(y + 0.45 * a)))

    pygame.draw.line(surf, LIGHTBLUE, (int(x), int(y)), (int(x - 0.45 * a), int(y + 0.62 * a)))
    pygame.draw.line(surf, LIGHTBLUE, (int(x), int(y)), (int(x - 0.62 * a), int(y + 0.45 * a)))

    pygame.draw.line(surf, LIGHTBLUE, (int(x), int(y)), (int(x - 0.45 * a), int(y - 0.62 * a)))
    pygame.draw.line(surf, LIGHTBLUE, (int(x), int(y)), (int(x - 0.62 * a), int(y - 0.45 * a)))
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
def yellow_stone(a, surf, x, y):
    '''
    рисуем камень в жёлтой фишке
    :param a: характерный размер камня
    :param surf: поверхность отрисовки камня
    :param x: координата центра по оси x
    :param y: координата центра по оси y
    '''

    list = []  # лист для координат вершин n-угольника

    u = 2 * math.pi / 4
    for i in range(0, 4, 1):
        list.append((int(x + 0.87 * a * math.sin(u * i)),
                     int(y + 0.87 * a * math.cos(u * i))))

    pygame.draw.polygon(surf, BLUE, list)
    pygame.draw.polygon(surf, ROYALBLUE, [[x,y],list[0], list[1]])
    pygame.draw.polygon(surf, ROYALBLUE, [[x, y], list[2], list[3]])
    pygame.draw.polygon(surf, LIGHTBLUE, [[int(x), int(y - 0.3 * a)],
                                          [int(x + 0.3 * a), int(y)],
                                          [int(x), int(y + 0.3 * a)],
                                          [int(x - 0.3 * a), int(y)]])

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
def blue_stone(a, surf, x, y):
    '''
    рисуем камень в синей фишке
    :param a: характерный размер камня
    :param surf: поверхность отрисовки камня
    :param x: координата центра по оси x
    :param y: координата центра по оси y
    '''

    u = 2 * math.pi / 30
    for i in range(0, 30 ,1):
        if i%2 == 0:
            pygame.draw.polygon(surf, GOLD , [[int(x - 0.8 * a * math.sin(i * u)),
                                                          int(y - 0.8 * a * math.cos(i * u))],
                                                        [int(x), int(y)],
                                                        [int(x - 0.8 * a * math.sin((i + 1) * u)),
                                                        int(y - 0.8 * a * math.cos((i + 1) * u))]])
        else:
            pygame.draw.polygon(surf, ORANGE, [[int(x - 0.8 * a * math.sin(i * u)),
                                              int(y - 0.8 * a * math.cos(i * u))],
                                             [int(x), int(y)],
                                             [int(x - 0.8 * a * math.sin((i + 1) * u)),
                                              int(y - 0.8 * a * math.cos((i + 1) * u))]])

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
def orange_stone(a, surf, x, y):
    '''
    рисуем камень в оранжевой фишке
    :param a: характерный размер камня
    :param surf: поверхность отрисовки камня
    :param x: координата центра по оси x
    :param y: координата центра по оси y
    '''
    list = []  # лист для координат вершин n-угольника

    u = 2 * math.pi / 6
    for i in range(0, 6, 1):
        list.append((int(x + 0.87 * a * math.sin(u * i)),
                     int(y + 0.87 * a * math.cos(u * i))))

    pygame.draw.polygon(surf, GREEN, list)
    pygame.draw.polygon(surf, DARKGREEN, [list[0], list[5], [int(x), int(y + 0.44 * a)]])
    pygame.draw.polygon(surf, DARKGREEN, [list[2], list[3], [int(x), int(y - 0.44 * a)]])
    pygame.draw.line(surf, DARKGREEN, list[4], list[2], 2)
    pygame.draw.line(surf, DARKGREEN, list[0], list[3], 2)
    pygame.draw.line(surf, DARKGREEN, list[1], list[5], 2)

def gray_chip(a, surf, color, k, x, y):
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
def gray_stone(a, surf, x, y):
    '''
    рисуем камень в серой фишке
    :param a: характерный размер камня
    :param surf: поверхность отрисовки камня
    :param x: координата центра по оси x
    :param y: координата центра по оси y
    '''
    colors = [RED, DARKRED, ORANGERED, SALMON, YELLOW, SALMON, CRIMSON, DARKRED]

    list = []  # лист для координат вершин n-угольника

    u = 2 * math.pi / 8
    for i in range(0, 9, 1):
        list.append((int(x + 0.87 * a * math.sin(math.pi / 8 + u * i)),
                     int(y + 0.87 * a * math.cos(math.pi / 8 + u * i))))
    for i in range(0, 8, 1):
        pygame.draw.polygon(surf, colors[i], [list[i], list[i + 1], [int(x), int(y)]])

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
def green_stone(a, surf, x, y):
    '''
    рисуем камень в зелёной фишке
    :param a: характерный размер камня
    :param surf: поверхность отрисовки камня
    :param x: координата центра по оси x
    :param y: координата центра по оси y
    '''
    colors = [YELLOW, KHAKI, YELLOW, KHAKI, GOLD, GOLDENROD, YELLOW, GOLDENROD]

    list = []  # лист для координат вершин n-угольника

    u = 2 * math.pi / 8
    for i in range(0, 9, 1):
        list.append((int(x + 0.87 * a * math.sin(math.pi / 8 + u * i)),
                     int(y + 0.87 * a * math.cos(math.pi / 8 + u * i))))
    for i in range(0, 8, 1):
        pygame.draw.polygon(surf, colors[i], [list[i], list[i + 1], [int(x), int(y)]])
    pygame.draw.circle(surf, LEMONCHIFFON, (int(x), int(y)), int(0.4 * a))

def draw_uzor(surf, x, y, b):
    '''
    рисует красивый узор для поля
    :param surf: поверхность, на которой рисуется узор
    :param x: положение на экране по оси x
    :param y: положение на экране по оси y
    :param b: характерный размер узора
    '''
    pygame.draw.rect(surf, DIMGREY, (int(x - 0.3 * b),int(y - 0.3 * b), int(0.6 * b), int(0.6 * b)), 1)
    pygame.draw.lines(surf, DIMGREY, True, [[int(x - 0.35 * b), int(y  -0.35 * b)],
                                            [int(x - 0.1 * b), int(y - 0.35 * b)],
                                            [int(x - 0.1 * b), int(y - 0.45 * b)],
                                            [int(x + 0.1 * b), int(y - 0.45 * b)],
                                            [int(x + 0.1 * b), int(y - 0.35 * b)],
                                            [int(x + 0.35 * b), int(y - 0.35 * b)],
                                            [int(x + 0.35 * b), int(y - 0.1 * b)],
                                            [int(x + 0.45 * b), int(y - 0.1 * b)],
                                            [int(x + 0.45 * b), int(y + 0.1 * b)],
                                            [int(x + 0.35 * b), int(y + 0.1 * b)],
                                            [int(x + 0.35 * b), int(y + 0.35 * b)],
                                            [int(x + 0.1 * b), int(y + 0.35 * b)],
                                            [int(x + 0.1 * b), int(y + 0.45 * b)],
                                            [int(x - 0.1 * b), int(y + 0.45 * b)],
                                            [int(x - 0.1 * b), int(y + 0.35 * b)],
                                            [int(x - 0.35 * b), int(y + 0.35 * b)],
                                            [int(x -0.35 * b), int(y + 0.1 * b)],
                                            [int(x - 0.45 * b), int(y + 0.1 * b)],
                                            [int(x - 0.45 * b), int(y - 0.1 * b)],
                                            [int(x - 0.35 * b), int(y - 0.1 * b)]])

    pygame.draw.lines(surf, DIMGREY, True, [[int(x - 0.45 * b), int(y - 0.45 * b)],
                                            [int(x - 0.2 * b), int(y - 0.45 * b)],
                                            [int(x - 0.2 * b), int(y - 0.55 * b)],
                                            [int(x + 0.2 * b), int(y - 0.55 * b)],
                                            [int(x + 0.2 * b), int(y - 0.45 * b)],
                                            [int(x + 0.45 * b), int(y - 0.45 * b)],
                                            [int(x + 0.45 * b), int(y - 0.2 * b)],
                                            [int(x + 0.55 * b), int(y - 0.2 * b)],
                                            [int(x + 0.55 * b), int(y + 0.2 * b)],
                                            [int(x + 0.45 * b), int(y + 0.2 * b)],
                                            [int(x + 0.45 * b), int(y + 0.45 * b)],
                                            [int(x + 0.2 * b), int(y + 0.45 * b)],
                                            [int(x + 0.2 * b), int(y + 0.55 * b)],
                                            [int(x - 0.2 * b), int(y + 0.55 * b)],
                                            [int(x - 0.2 * b), int(y + 0.45 * b)],
                                            [int(x - 0.45 * b), int(y + 0.45 * b)],
                                            [int(x - 0.45 * b), int(y + 0.2 * b)],
                                            [int(x - 0.55 * b), int(y + 0.2 * b)],
                                            [int(x - 0.55 * b), int(y - 0.2 * b)],
                                            [int(x - 0.45 * b), int(y - 0.2 * b)]])
    pygame.draw.lines(surf, DIMGREY, False, [[int(x - 0.35 * b), int(y - 0.45 * b)],
                                             [int(x - 0.35 * b), int(y - 0.65 * b)],
                                             [int(x + 0.35 * b), int(y - 0.65 * b)],
                                             [int(x + 0.35 * b), int(y - 0.45 * b)]])
    pygame.draw.lines(surf, DIMGREY, False,[[int(x + 0.45 * b), int(y - 0.35 * b)],
                                             [int(x + 0.65 * b), int(y - 0.35 * b)],
                                             [int(x + 0.65 * b), int(y + 0.35 * b)],
                                             [int(x + 0.45 * b), int(y + 0.35 * b)]])
    pygame.draw.lines(surf, DIMGREY, False, [[int(x - 0.45 * b), int(y - 0.35 * b)],
                                             [int(x - 0.65 * b), int(y - 0.35 * b)],
                                             [int(x - 0.65 * b), int(y + 0.35 * b)],
                                             [int(x - 0.45 * b), int(y + 0.35 * b)]])
    pygame.draw.lines(surf, DIMGREY, False, [[int(x - 0.35 * b), int(y + 0.45 * b)],
                                             [int(x - 0.35 * b), int(y + 0.65 * b)],
                                             [int(x + 0.35 * b), int(y + 0.65 * b)],
                                             [int(x + 0.35 * b), int(y + 0.45 * b)]])

    pygame.draw.lines(surf, DIMGREY, False, [[int(x - 0.55 * b), int(y - 0.35 * b)],
                                             [int(x - 0.55 * b), int(y - 0.55 * b)],
                                             [int(x - 0.35 * b), int(y - 0.55 * b)]])
    pygame.draw.lines(surf, DIMGREY, False, [[int(x + 0.55 * b), int(y - 0.35 * b)],
                                             [int(x + 0.55 * b), int(y - 0.55 * b)],
                                             [int(x + 0.35 * b), int(y - 0.55 * b)]])
    pygame.draw.lines(surf, DIMGREY, False, [[int(x - 0.55 * b), int(y + 0.35 * b)],
                                             [int(x - 0.55 * b), int(y + 0.55 * b)],
                                             [int(x - 0.35 * b), int(y + 0.55 * b)]])
    pygame.draw.lines(surf, DIMGREY, False, [[int(x + 0.55 * b), int(y + 0.35 * b)],
                                             [int(x + 0.55 * b), int(y + 0.55 * b)],
                                             [int(x + 0.35 * b), int(y + 0.55 * b)]])

def draw_border1(surf, x, y, background_color, spiral_color, b, n):
    '''
    функция рисует красивый узор границы поля по вертикали
    :param surf: поверхность отрисовки
    :param x: координата верхнего левого угла по оси x
    :param y: координата верхнего левого угла по оси y
    :param background_color: основной цвет поверхности узора
    :param spiral_color: цвет спирали узора
    :param b: характерный размер
    :param n: четное - узор на правой стороне, нечетное - узор а лево стороне
    '''
    pygame.draw.rect(surf, background_color, (int(x), int(y), int(b), int(2 * b)))

    pygame.draw.lines(surf, spiral_color, False, [[int(x + 0.5 * b - (-1)**n * 0.1 * b), int(y + 0.4 * b)],
                                                  [int(x + 0.5 * b + (-1)**n * 0.1 * b), int(y + 0.4 * b)],
                                                  [int(x + 0.5 * b + (-1)**n * 0.1 * b), int(y + 0.6 * b)],
                                                  [int(x + 0.5 * b - (-1)**n * 0.3 * b), int(y + 0.6 * b)],
                                                  [int(x + 0.5 * b - (-1)**n * 0.3 * b), int(y + 0.2 * b)],
                                                  [int(x + 0.5 * b + (-1)**n * 0.3 * b), int(y + 0.2 * b)],
                                                  [int(x + 0.5 * b + (-1)**n * 0.3 * b), int(y + 0.8 * b)],
                                                  [int(x + 0.5 * b - (-1)**n * 0.5 * b), int(y + 0.8 * b)],
                                                  [int(x + 0.5 * b - (-1)**n * 0.5 * b), int(y)],
                                                  [int(x + 0.5 * b + (-1)**n * 0.5 * b), int(y)],
                                                  [int(x + 0.5 * b + (-1)**n * 0.5 * b), int(y + b)],
                                                  [int(x + 0.5 * b - (-1)**n * 0.5 * b), int(y + b)],
                                                  [int(x + 0.5 * b - (-1)**n * 0.5 * b), int(y + 2 * b)],
                                                  [int(x + 0.5 * b + (-1)**n * 0.5 * b), int(y + 2 * b)],
                                                  [int(x + 0.5 * b + (-1)**n * 0.5 * b), int(y + 1.2 * b)],
                                                  [int(x + 0.5 * b - (-1)**n * 0.3 * b), int(y + 1.2 * b)],
                                                  [int(x + 0.5 * b - (-1)**n * 0.3 * b), int(y + 1.8 * b)],
                                                  [int(x + 0.5 * b + (-1)**n * 0.3 * b), int(y + 1.8 * b)],
                                                  [int(x + 0.5 * b + (-1)**n * 0.3 * b), int(y + 1.4 * b)],
                                                  [int(x + 0.5 * b - (-1)**n * 0.1 * b), int(y + 1.4 * b)],
                                                  [int(x + 0.5 * b - (-1)**n * 0.1 * b), int(y + 1.6 * b)],
                                                  [int(x + 0.5 * b + (-1)**n * 0.1 * b), int(y + 1.6 * b)]])
def draw_border2(surf, x, y, background_color, spiral_color, b, n):
    '''
    функция рисует красивый узор границы поля по горизонтали
    :param surf: поверхность отрисовки
    :param x: координата верхнего левого угла по оси x
    :param y: координата верхнего левого угла по оси y
    :param background_color: основной цвет поверхности узора
    :param spiral_color: цвет спирали узора
    :param b: характерный размер
    :param n: если четное, то узор сверху, если нечетное - узор снизу
    '''
    pygame.draw.rect(surf, background_color, (int(x), int(y), int(2 * b), int(b)))
    pygame.draw.lines(surf, spiral_color, False, [[int(x + 0.4 * b), int(y + 0.5 * b - (-1) ** n * 0.1 * b)],
                                                  [int(x + 0.4 * b), int(y + 0.5 * b + (-1) ** n * 0.1 * b)],
                                                  [int(x + 0.6 * b), int(y + 0.5 * b + (-1) ** n * 0.1 * b)],
                                                  [int(x + 0.6 * b), int(y + 0.5 * b - (-1) ** n * 0.3 * b)],
                                                  [int(x + 0.2 * b), int(y + 0.5 * b - (-1) ** n * 0.3 * b)],
                                                  [int(x + 0.2 * b), int(y + 0.5 * b + (-1) ** n * 0.3 * b)],
                                                  [int(x + 0.8 * b), int(y + 0.5 * b + (-1) ** n * 0.3 * b)],
                                                  [int(x+ 0.8 * b), int(y + 0.5 * b - (-1) ** n * 0.5 * b)],
                                                  [int(x), int(y + 0.5 * b - (-1) ** n * 0.5 * b)],
                                                  [int(x), int(y + 0.5 * b + (-1) ** n * 0.5 * b)],
                                                  [int(x + b), int(y + 0.5 * b + (-1) ** n * 0.5 * b)],
                                                  [int(x + b), int(y + 0.5 * b - (-1) ** n * 0.5 * b)],
                                                  [int(x + 2 * b), int(y + 0.5 * b - (-1) ** n * 0.5 * b)],
                                                  [int(x + 2 * b), int(y + 0.5 * b + (-1) ** n * 0.5 * b)],
                                                  [int(x + 1.2 * b), int(y + 0.5 * b + (-1) ** n * 0.5 * b)],
                                                  [int(x + 1.2 * b), int(y + 0.5 * b - (-1) ** n * 0.3 * b)],
                                                  [int(x + 1.8 * b), int(y + 0.5 * b - (-1) ** n * 0.3 * b)],
                                                  [int(x + 1.8 * b), int(y + 0.5 * b + (-1) ** n * 0.3 * b)],
                                                  [int(x + 1.4 * b), int(y + 0.5 * b + (-1) ** n * 0.3 * b)],
                                                  [int(x + 1.4 * b), int(y + 0.5 * b - (-1) ** n * 0.1 * b)],
                                                  [int(x + 1.6 * b), int(y + 0.5 * b - (-1) ** n * 0.1 * b)],
                                                  [int(x + 1.6 * b), int(y + 0.5 * b + (-1) ** n * 0.1 * b)]])

def draw_pole(n, a, color1, color2, x, y, b):
    '''
    красивое оформление поля
    :param n: количество фишек на стороне
    :param a: размер  одной ячейки
    :param color1: основной цвет поля
    :param color2: цвет для узоров
    :param x: координата левого верхнего угла поля по оси x
    :param y: координата левого верхнего угла поля по оси y
    :param b: размер узора
    '''

    pygame.draw.rect(screen, color1,(int(x), int(y), int(n * a), int(n * a)))

    for i in range(0, n + 1, 1):
        for j in range(0, n, 1):
            pygame.draw.line(screen, color2, (int(x + j * a + 0.65 * b), int(y + i * a)),
                             (int(x + (j + 1) * a - 0.65 * b), int(y + i * a)),2)
            pygame.draw.line(screen, color2, (int(x + i * a), int(y + j * a + 0.65 * b)),
                             (int(x + i * a), int(y + (j + 1) * a - 0.65 * b)),2)
    for i in range(0, n + 1, 1):
        for j in range(0, n + 1, 1):
            draw_uzor(screen, x + i * a, y + j * a, b)

    for i in range(0, n + 1, 1):
        draw_border1(screen, int(x + n * a), int(y - a / 2 + a * i), DARKGOLDENROD, DIMGREY, int(a / 2), 0)
    for i in range(0, n + 1, 1):
        draw_border1(screen, int(x - a / 2), int(y - a / 2 + a * i), DARKGOLDENROD, DIMGREY, int(a / 2), 1)
    for i in range(0, n, 1):
        draw_border2(screen, int(x + i * a), int(y - a / 2), DARKGOLDENROD, DIMGREY, int(a / 2), 0)
    for i in range(0, n, 1):
        draw_border2(screen, int(x + i * a), int(y + n * a), DARKGOLDENROD, DIMGREY, int(a / 2), 1)



red_chip(100, screen, WHITE, 0.4, 500, 400)
red_stone(int(0.4 * 100 / 3 * math.sqrt(2)), screen, 550, 450)

yellow_chip(100, screen, WHITE, 0.4, 600, 100)
yellow_stone(int(0.4 * 100 / 3 * math.sqrt(2)), screen, 650, 150)

blue_chip(100, screen, WHITE, 0.4, 650, 300 )
blue_stone(int(0.4 * 100 / 3 * math.sqrt(2)), screen, 700, 350)

orange_chip(100, screen, WHITE, 0.4, 100, 100)
orange_stone(int(0.4 * 100 / 3 * math.sqrt(2)), screen, 150, 150)

purple_chip(100, screen, WHITE, 0.4, 100, 200)
purple_stone(int(0.4 * 100 / 3 * math.sqrt(2)), screen, 150, 250)

gray_chip(100, screen, WHITE, 0.4, 100, 400)
gray_stone(int(0.4 * 100 / 3 * math.sqrt(2)), screen, 150, 450)

green_chip(100, screen, WHITE, 0.4, 200, 300)
green_stone(int(0.4 * 100 / 3 * math.sqrt(2)), screen, 250, 350)

draw_pole(4, 50, CADETBLUE, DIMGREY, 250, 100, 16)

red_stone(20, screen, 400, 560)
pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()