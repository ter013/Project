# прорисовка объектов
import pygame, sys
from random import randint
import random
from pygame.draw import *
import math

pygame.init()
font = pygame.font.Font('freesansbold.ttf', 14)

from Colors import *


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

    u = 2 * math.pi / n  # характерный угол

    list = []  # лист для координат вершин n-угольника

    for i in range(0, n + 1, 1):
        list.append((int(a / 2 + k * a * math.sin(alpha + u / 2 + u * i)),
                     int(a / 2 + k * a * math.cos(alpha + u / 2 + u * i))))

    polygon(surface, color1, list)

    for i in range(1, n + 1, 1):
        pygame.draw.line(surface, color2, list[i], list[i - 1], 5)


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


def red_chip(a, surf, k, x, y):
    '''
    функция рисует красную фишку с орнаментом
    :param a: размер ячейки
    :param surf: экран, куда отображается плоскость
    :param k: масштаб изображения внутри ячейкм
    :param x: положение ячейки на экране по оси x
    :param y: положение ячейки на экране по оси y
    '''

    surface = pygame.Surface((a, a), pygame.SRCALPHA, 32)

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

    surf.blit(surface, (x, y))


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

    almaz_animation(surf, x, y, 0.8 * a)


def purple_chip(a, surf, k, x, y):
    '''
    функция рисует фиолетовую фишку с орнаментом
    :param a: размер ячейки
    :param surf: экран, куда отображается плоскость
    :param k: масштаб изображения внутри ячейкм
    :param x: положение ячейки на экране по оси x
    :param y: положение ячейки на экране по оси y
    '''

    surface = pygame.Surface((a, a), pygame.SRCALPHA, 32)

    draw1(a, PURPLE, INDIGO, 8, surface, k, -math.pi / 8)

    pygame.draw.line(surface, DIMGREY, [int(a / 2), int(a / 2 + 4.7 * k * a / 5)],
                     [int(a / 2), int(a / 2 + 3.2 * k * a / 5)])

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - k * a / 3), int(a / 2 + k * a / 3), int(k * a / 3),
                                       int(2 * (3.2 / 5 - 1 / 3) * k * a)), 0, math.pi / 2)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2), int(a / 2 + k * a / 3), int(k * a / 3),
                                       int(2 * (3.2 / 5 - 1 / 3) * k * a)), math.pi / 2, -math.pi)

    pygame.draw.line(surface, DIMGREY, [int(a / 2), int(a / 2 - 4.7 * k * a / 5)],
                     [int(a / 2), int(a / 2 - 3.2 * k * a / 5)])

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - k * a / 3), int(a / 2 - k * a / 3 - 2 * (3.2 / 5 - 1 / 3) * k * a),
                                       int(k * a / 3),
                                       int(2 * (3.2 / 5 - 1 / 3) * k * a)), 3 / 2 * math.pi, 0)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2), int(a / 2 - k * a / 3 - 2 * (3.2 / 5 - 1 / 3) * k * a),
                                       int(k * a / 3), int(2 * (3.2 / 5 - 1 / 3) * k * a)), math.pi, -math.pi / 2)

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + 4.7 * k * a / 5), int(a / 2)],
                     [int(a / 2 + 3.2 * k * a / 5), int(a / 2)])

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + k * a / 3), int(a / 2 - k * a / 3),
                                       int(2 * (3.2 / 5 - 1 / 3) * k * a), int(k * a / 3)), math.pi, - math.pi / 2)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + k * a / 3), int(a / 2), int(2 * (3.2 / 5 - 1 / 3) * k * a),
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
                                       int(k * a / 3)), math.pi / 2, -math.pi)

    pygame.draw.circle(surface, DIMGREY, (int(a / 2 - k * a / 1.7), int(a / 2 - k * a / 1.7)), int(k * a / 8), 1)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2), int(a / 2 - 2 * k * a / 3), int(k * a / 3),
                                       int(2 * k * a / 3)), 0, - 3 / 2 * math.pi)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2), int(a / 2 - k * a / 3), int(2 * k * a / 3),
                                       int(k * a / 3)), 0, -3 / 2 * math.pi)

    pygame.draw.circle(surface, DIMGREY, (int(a / 2 + k * a / 1.7), int(a / 2 - k * a / 1.7)), int(k * a / 8), 1)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2), int(a / 2), int(2 * k * a / 3),
                                       int(k * a / 3)), 3 / 2 * math.pi, 0)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2), int(a / 2), int(k * a / 3),
                                       int(2 * k * a / 3)), 3 / 2 * math.pi, 0)

    pygame.draw.circle(surface, DIMGREY, (int(a / 2 + k * a / 1.7), int(a / 2 + k * a / 1.7)), int(k * a / 8), 1)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - k * a / 3), int(a / 2), int(k * a / 3),
                                       int(2 * k * a / 3)), math.pi, - math.pi / 2)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 2 / 3 * k * a), int(a / 2), int(2 * k * a / 3),
                                       int(k * a / 3)), math.pi, - math.pi / 2)

    pygame.draw.circle(surface, DIMGREY, (int(a / 2 - k * a / 1.7), int(a / 2 + k * a / 1.7)), int(k * a / 8), 1)

    pygame.draw.circle(surface, DIMGREY, (int(a / 2), int(a / 2)), int(k * a / 20))

    pygame.draw.circle(surface, DIMGREY, (int(a / 2), int(a / 2)), int(k * a / 8), 1)

    m = 20  # коэффициент, регулирующий угол наклона лучиков

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

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + k * a / 4), int(a / 2 + k * a / 4)],
                     [int(a / 2 + k * a / 4), int(a / 2 + k * a / 3)])

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

    surf.blit(surface, (x, y))


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

    almaz_animation(surf, x, y, 0.8 * a)


def yellow_chip(a, surf, k, x, y):
    '''
        функция рисует жёлтую фишку с орнаментом
        :param a: размер ячейки
        :param surf: экран, куда отображается плоскость
        :param k: масштаб изображения внутри ячейкм
        :param x: положение ячейки на экране по оси x
        :param y: положение ячейки на экране по оси y
        '''

    surface = pygame.Surface((a, a), pygame.SRCALPHA, 32)

    pygame.draw.circle(surface, YELLOW, (int(a / 2), int(a / 2)), int(k * a))
    pygame.draw.circle(surface, GOLD, (int(a / 2), int(a / 2)), int(k * a), 2)

    pygame.draw.circle(surface, DIMGREY, (int(a / 2), int(a / 2)), int(k * a / 8), 1)

    pygame.draw.line(surface, DIMGREY, [int(a / 2), int(a / 2 + k * a / 6)], [int(a / 2), int(a / 2 + k * a / 3)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2), int(a / 2 - k * a / 6)], [int(a / 2), int(a / 2 - k * a / 3)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - k * a / 6), int(a / 2)], [int(a / 2 - k * a / 3), int(a / 2)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + k * a / 6), int(a / 2)], [int(a / 2 + k * a / 3), int(a / 2)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + k * a / 7), int(a / 2 - k * a / 7)],
                     [int(a / 2 + k * a / 4), int(a / 2 - k * a / 4)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - k * a / 7), int(a / 2 - k * a / 7)],
                     [int(a / 2 - k * a / 4), int(a / 2 - k * a / 4)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + k * a / 7), int(a / 2 + k * a / 7)],
                     [int(a / 2 + k * a / 4), int(a / 2 + k * a / 4)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 - k * a / 7), int(a / 2 + k * a / 7)],
                     [int(a / 2 - k * a / 4), int(a / 2 + k * a / 4)])

    # рисуем узорчик в правом верхнем углу

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + k * a / 4 - k * a / 8), int(a / 2 - k * a / 4 - k * a / 8)],
                     [int(a / 2 + k * a / 4 - k * a / 8 + k * a / 8),
                      int(a / 2 - k * a / 4 - k * a / 8 - k * a / 8)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + k * a / 4 + k * a / 8), int(a / 2 - k * a / 4 + k * a / 8)],
                     [int(a / 2 + k * a / 4 + k * a / 8 + k * a / 8),
                      int(a / 2 - k * a / 4 + k * a / 8 - k * a / 8)])

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + k * a / 4 - k * a / 8 + k * a / 8),
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

    # рисуем узорчик в левом нижнем уголке

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

    # рисуем узорчик в правом нижнем уголке

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

    surf.blit(surface, (x, y))


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
    pygame.draw.polygon(surf, ROYALBLUE, [[x, y], list[0], list[1]])
    pygame.draw.polygon(surf, ROYALBLUE, [[x, y], list[2], list[3]])
    pygame.draw.polygon(surf, LIGHTBLUE, [[int(x), int(y - 0.3 * a)],
                                          [int(x + 0.3 * a), int(y)],
                                          [int(x), int(y + 0.3 * a)],
                                          [int(x - 0.3 * a), int(y)]])

    almaz_animation(surf, x, y, 0.8 * a)


def blue_chip(a, surf, k, x, y):
    '''
    функция рисует синию фишку с орнаментом
    :param a: размер ячейки

    :param surf: экран, куда отображается плоскость
    :param k: масштаб изображения внутри ячейкм
    :param x: положение ячейки на экране по оси x
    :param y: положение ячейки на экране по оси y
    '''

    surface = pygame.Surface((a, a), pygame.SRCALPHA, 32)

    draw1(a, ROYALBLUE, BLUE, 6, surface, k, math.pi / 6)

    pygame.draw.circle(surface, DIMGREY, (int(a / 2), int(a / 2)), int(k * a / 8), 1)

    for i in range(0, 6, 1):
        pygame.draw.lines(surface, DIMGREY, False, [[int(a / 2 + k * a / 8 * math.sin(math.pi * i / 3)),
                                                     int(a / 2 - k * a / 8 * math.cos(math.pi * i / 3))],
                                                    [int(a / 2 + (k * a / 8 + k * a / 16) * math.sin(math.pi * i / 3) +
                                                         k * a / 40 * math.cos(math.pi * i / 3)),
                                                     int(a / 2 - (k * a / 8 + k * a / 16) * math.cos(math.pi * i / 3) +
                                                         k * a / 40 * math.sin(math.pi * i / 3))],
                                                    [int(a / 2 + k * a / 4 * math.sin(math.pi * i / 3)),
                                                     int(a / 2 - k * a / 4 * math.cos(math.pi * i / 3))]])

    # рисуем "палочки" в узорах
    for i in range(0, 6, 1):
        pygame.draw.line(surface, DIMGREY, [int(a / 2 - 0.98 * k * a * math.sin(i * math.pi / 3)),
                                            int(a / 2 + 0.98 * k * a * math.cos(i * math.pi / 3))],
                         [int(a / 2 - 0.56 * k * a * math.sin(i * math.pi / 3)),
                          int(a / 2 + 0.56 * k * a * math.cos(i * math.pi / 3))])
    # дуги нижний угол
    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - k * a / 3), int(a / 2 + 0.45 * k * a),
                                       int(k * a / 3), int(k * a / 3)), 0, -1.7)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2), int(a / 2 + 0.45 * k * a), int(k * a / 3), int(k * a / 3)),
                    - math.pi + 1.7, - math.pi)

    # дуги верхний угол
    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - k * a / 3), int(a / 2 - 0.45 * k * a - k * a / 3),
                                       int(k * a / 3), int(k * a / 3)), 1.7, 0)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2), int(a / 2 - 0.45 * k * a - k * a / 3),
                                       int(k * a / 3), int(k * a / 3)), math.pi, math.pi - 1.7)

    # дуги левый нижний угол
    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.56 * k * a), int(a / 2 + 0.26 * k * a),
                                       int(k * a / 3), int(k * a / 3)), - math.pi + 0.65, 5 / 6 * math.pi)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.73 * k * a), int(a / 2 - 0.02 * k * a),
                                       int(k * a / 3), int(k * a / 3)), -1.05, 4.25)

    # дуги левый верхний угол
    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.58 * k * a), int(a / 2 - 0.59 * k * a),
                                       int(k * a / 3), int(k * a / 3)), -2.09, 2.49)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.73 * k * a), int(a / 2 - 0.31 * k * a),
                                       int(k * a / 3), int(k * a / 3)), -3.54, 1.05)
    # дуги правый верхний угол
    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.26 * k * a), int(a / 2 - 0.58 * k * a),
                                       int(k * a / 3), int(k * a / 3)), 0.65, 5.24)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.44 * k * a), int(a / 2 - 0.32 * k * a),
                                       int(k * a / 3), int(k * a / 3)), - 4.19, 0.65)
    # дуги правый нижний угол
    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.40 * k * a), int(a / 2 - 0.02 * k * a),
                                       int(k * a / 3), int(k * a / 3)), -0.39, 4.19)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.26 * k * a), int(a / 2 + 0.27 * k * a),
                                       int(k * a / 3), int(k * a / 3)), 1.05, 5.89)

    pygame.draw.circle(surface, BLUE, (int(a / 2), int(a / 2)), int(math.sqrt(2) * k * a / 3), 2)
    surf.blit(surface, (x, y))


def blue_stone(a, surf, x, y):
    '''
    рисуем камень в синей фишке
    :param a: характерный размер камня
    :param surf: поверхность отрисовки камня
    :param x: координата центра по оси x
    :param y: координата центра по оси y
    '''

    u = 2 * math.pi / 30
    for i in range(0, 30, 1):
        if i % 2 == 0:
            pygame.draw.polygon(surf, GOLD, [[int(x - 0.8 * a * math.sin(i * u)),
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

    almaz_animation(surf, x, y, 0.8 * a)


def orange_chip(a, surf, k, x, y):
    '''
    функция рисует оранжевую фишку с орнаментом
    :param a: размер ячейки

    :param surf: экран, куда отображается плоскость
    :param k: масштаб изображения внутри ячейкм
    :param x: положение ячейки на экране по оси x
    :param y: положение ячейки на экране по оси y
     '''

    surface = pygame.Surface((a, a))
    surface.fill(WHITE)
    surface.set_colorkey(WHITE)

    pygame.draw.circle(surface, DARKORANGE, (int(a / 2), int(a / 2)), int(k * a))
    pygame.draw.circle(surface, WHITE, (int(a / 2 + k * a * 1.65), int(a / 2)), int(k * a))
    pygame.draw.circle(surface, WHITE, (int(a / 2 - k * a * 1.65), int(a / 2)), int(k * a))

    pygame.draw.arc(surface, ORANGERED, (int(a / 2 - k * a), int(a / 2 - k * a),
                                         int(2 * k * a), int(2 * k * a)), 0.62, 2.52, 3)

    pygame.draw.arc(surface, ORANGERED, (int(a / 2 - k * a), int(a / 2 - k * a),
                                         int(2 * k * a), int(2 * k * a)), -2.52, -0.62, 3)

    pygame.draw.arc(surface, ORANGERED, (int(a / 2 + 0.65 * k * a), int(a / 2 - k * a),
                                         int(2 * k * a), int(2 * k * a)), -3.74, -2.54, 3)

    pygame.draw.arc(surface, ORANGERED, (int(a / 2 - 2.65 * k * a), int(a / 2 - k * a),
                                         int(2 * k * a), int(2 * k * a)), -0.6, 0.6, 3)

    # узор посередине справа
    pygame.draw.line(surface, DIMGREY, [int(a / 2 + 0.45 * k * a), int(a / 2 - 0.23 * k * a)],
                     [int(a / 2 + 0.45 * k * a), int(a / 2 + 0.23 * k * a)])

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.45 * k * a), int(a / 2 - 0.23 * k * a),
                                       int(0.14 * k * a), int(0.14 * k * a)), -1.57, 1.57)
    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.45 * k * a), int(a / 2 - 0.08 * k * a),
                                       int(0.14 * k * a), int(0.14 * k * a)), -1.57, 1.57)
    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.45 * k * a), int(a / 2 + 0.07 * k * a),
                                       int(0.14 * k * a), int(0.14 * k * a)), -1.57, 1.57)

    # узор посередине слева
    pygame.draw.line(surface, DIMGREY, [int(a / 2 - 0.45 * k * a), int(a / 2 - 0.23 * k * a)],
                     [int(a / 2 - 0.45 * k * a), int(a / 2 + 0.23 * k * a)])

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.59 * k * a), int(a / 2 - 0.23 * k * a),
                                       int(0.14 * k * a), int(0.14 * k * a)), 1.57, 4.71)
    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.59 * k * a), int(a / 2 - 0.08 * k * a),
                                       int(0.14 * k * a), int(0.14 * k * a)), 1.57, 4.71)
    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.59 * k * a), int(a / 2 + 0.07 * k * a),
                                       int(0.14 * k * a), int(0.14 * k * a)), 1.57, 4.71)
    # центральный узор

    pygame.draw.circle(surface, DIMGREY, (int(a / 2), int(a / 2 + 0.2 * k * a)), int(0.1 * k * a), 1)
    pygame.draw.circle(surface, DIMGREY, (int(a / 2), int(a / 2 - 0.2 * k * a)), int(0.1 * k * a), 1)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.2 * k * a), int(a / 2 - 0.44 * k * a),
                                       int(0.4 * k * a), int(0.4 * k * a)), -3.14, 0)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.2 * k * a), int(a / 2 + 0.04 * k * a),
                                       int(0.4 * k * a), int(0.4 * k * a)), 0, 3.13)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.3 * k * a), int(a / 2 - 0.1 * k * a),
                                       int(0.2 * k * a), int(0.2 * k * a)), 1.9, 4.5)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.1 * k * a), int(a / 2 - 0.1 * k * a),
                                       int(0.2 * k * a), int(0.2 * k * a)), -1.2, 1.2)

    # верхний узор
    pygame.draw.line(surface, DIMGREY, [int(a / 2), int(a / 2 - 0.55 * k * a)],
                     [int(a / 2 + 0.43 * k * a), int(a / 2 - 0.32 * k * a)])

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

    # нижний узор
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
    surface.set_colorkey(WHITE)
    surf.blit(surface, (x, y))


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
    pygame.draw.polygon(surf, LIMEGREEN, [list[0], list[5], [int(x), int(y + 0.44 * a)]])
    pygame.draw.polygon(surf, LIMEGREEN, [list[2], list[3], [int(x), int(y - 0.44 * a)]])
    pygame.draw.line(surf, LIMEGREEN, list[4], list[2], 2)
    pygame.draw.line(surf, LIMEGREEN, list[0], list[3], 2)
    pygame.draw.line(surf, LIMEGREEN, list[1], list[5], 2)

    almaz_animation(surf, x, y, 0.8 * a)


def gray_chip(a, surf, k, x, y):
    '''
    функция рисует серую фишку с орнаментом
    :param a: размер ячейки
    :param surf: экран, куда отображается плоскость
    :param k: масштаб изображения внутри ячейкм
    :param x: положение ячейки на экране по оси x
    :param y: положение ячейки на экране по оси y
    '''
    surface = pygame.Surface((a, a), pygame.SRCALPHA, 32)

    draw1(a, SILVER, GRAY, 4, surface, k, 0)

    # центральный узор
    pygame.draw.circle(surface, DIMGREY, (int(a / 2), int(a / 2)), int(0.1 * k * a), 1)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.2 * k * a), int(a / 2 - 0.2 * k * a),
                                       int(0.4 * k * a), int(0.4 * k * a)), -1.0, 4.38)

    pygame.draw.lines(surface, DIMGREY, False, [[int(a / 2 - 0.1 * k * a), int(a / 2 + 0.18 * k * a)],
                                                [int(a / 2 - 0.15 * k * a), int(a / 2 + 0.33 * k * a)],
                                                [int(a / 2 - 0.21 * k * a), int(a / 2 + 0.33 * k * a)],
                                                [int(a / 2 - 0.16 * k * a), int(a / 2 + 0.21 * k * a)],
                                                [int(a / 2 - 0.24 * k * a), int(a / 2 + 0.30 * k * a)],
                                                [int(a / 2 - 0.31 * k * a), int(a / 2 + 0.22 * k * a)],
                                                [int(a / 2 - 0.22 * k * a), int(a / 2 + 0.14 * k * a)],
                                                [int(a / 2 - 0.38 * k * a), int(a / 2 + 0.15 * k * a)],
                                                [int(a / 2 - 0.40 * k * a), int(a / 2 + 0.04 * k * a)],
                                                [int(a / 2 - 0.25 * k * a), int(a / 2 + 0.02 * k * a)],
                                                [int(a / 2 - 0.38 * k * a), int(a / 2 - 0.05 * k * a)],
                                                [int(a / 2 - 0.32 * k * a), int(a / 2 - 0.17 * k * a)],
                                                [int(a / 2 - 0.22 * k * a), int(a / 2 - 0.12 * k * a)],
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
                                                [int(a / 2 + 0.3 * k * a), int(a / 2 + 0.21 * k * a)],
                                                [int(a / 2 + 0.24 * k * a), int(a / 2 + 0.28 * k * a)],
                                                [int(a / 2 + 0.18 * k * a), int(a / 2 + 0.23 * k * a)],
                                                [int(a / 2 + 0.20 * k * a), int(a / 2 + 0.31 * k * a)],
                                                [int(a / 2 + 0.16 * k * a), int(a / 2 + 0.33 * k * a)],
                                                [int(a / 2 + 0.11 * k * a), int(a / 2 + 0.17 * k * a)]])

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
    # узор в верхней правой части

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

    # узор в левой верхней части

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
                       [int(a / 2 - 0.53 * k * a), int(a / 2 + 0.16 * k * a)],
                       [int(a / 2 - 0.63 * k * a), int(a / 2 + 0.16 * k * a)],
                       [int(a / 2 - 0.60 * k * a), int(a / 2 + 0.03 * k * a)]])

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.60 * k * a), int(a / 2 - 0.58 * k * a),
                                       int(0.3 * k * a), int(0.3 * k * a)), 0, 3.14)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.48 * k * a), int(a / 2 - 0.55 * k * a),
                                       int(0.2 * k * a), int(0.2 * k * a)), - 3.14, 0)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 - 0.48 * k * a), int(a / 2 - 0.49 * k * a),
                                       int(0.1 * k * a), int(0.1 * k * a)), 0, 3.14)

    # узор в правой нижней части

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

    surf.blit(surface, (x, y))


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

    almaz_animation(surf, x, y, 0.8 * a)


def green_chip(a, surf, k, x, y):
    '''
    функция рисует серую зелёную фишку с орнаментом
    :param a: размер ячейки
    :param surf: экран, куда отображается плоскость
    :param k: масштаб изображения внутри ячейкм
    :param x: положение ячейки на экране по оси x
    :param y: положение ячейки на экране по оси y
    '''
    surface = pygame.Surface((a, a), pygame.SRCALPHA, 32)

    draw1(a, GREEN, DARKGREEN, 4, surface, k, math.pi / 4)

    # центральный узор
    pygame.draw.lines(surface, DIMGREY, True, [[int(a / 2), int(a / 2 - 0.1 * k * a)],
                                               [int(a / 2 + 0.1 * k * a), int(a / 2)],
                                               [int(a / 2), int(a / 2 + 0.1 * k * a)],
                                               [int(a / 2 - 0.1 * k * a), int(a / 2)]])

    pygame.draw.circle(surface, DIMGREY, (int(a / 2 - 0.2 * k * a), int(a / 2 - 0.2 * k * a)), int(0.08 * k * a), 1)

    pygame.draw.circle(surface, DIMGREY, (int(a / 2 + 0.2 * k * a), int(a / 2 - 0.2 * k * a)), int(0.08 * k * a), 1)

    pygame.draw.circle(surface, DIMGREY, (int(a / 2 - 0.2 * k * a), int(a / 2 + 0.2 * k * a)), int(0.08 * k * a), 1)

    pygame.draw.circle(surface, DIMGREY, (int(a / 2 + 0.2 * k * a), int(a / 2 + 0.2 * k * a)), int(0.08 * k * a), 1)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.06 * k * a), int(a / 2 - 0.4 * k * a),
                                       int(0.3 * k * a), int(0.4 * k * a)), -1.57, 0)

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

    # верхний узор
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

    # нижний узор
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

    # левый узор

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

    # правый узор

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.52 * k * a), int(a / 2 - 0.15 * k * a),
                                       int(0.3 * k * a), int(0.3 * k * a)), -3.14, 0)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.6 * k * a), int(a / 2 - 0.1 * k * a),
                                       int(0.2 * k * a), int(0.2 * k * a)), 0, 3.14)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.61 * k * a), int(a / 2 - 0.08 * k * a),
                                       int(0.16 * k * a), int(0.16 * k * a)), -3.14, 0)

    pygame.draw.line(surface, DIMGREY, [int(a / 2 + 0.52 * k * a), int(a / 2)],
                     [int(a / 2 + 0.52 * k * a), int(a / 2 - 0.4 * k * a)])

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.3 * k * a), int(a / 2 - 0.51 * k * a),
                                       int(0.22 * k * a), int(0.22 * k * a)), 0, 3.14)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.32 * k * a), int(a / 2 - 0.47 * k * a),
                                       int(0.14 * k * a), int(0.14 * k * a)), - 3.14, 0)

    pygame.draw.arc(surface, DIMGREY, (int(a / 2 + 0.37 * k * a), int(a / 2 - 0.43 * k * a),
                                       int(0.08 * k * a), int(0.08 * k * a)), 0, 3.14)

    draw2(a, DARKGREEN, 8, surface, k, 0)
    surf.blit(surface, (x, y))


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

    almaz_animation(surf, x, y, 0.8 * a)


def multi_chip(a, surf, k, x, y, p, alpha):
    '''
    функция рисует бонусную фишку, которая имеет любой цвет и может реагировать с любым рядом
    :param a: размер ячейки
    :param surf: экран, куда отображается плоскость
    :param k: масштаб изображения внутри ячейкм
    :param x: положение ячейки на экране по оси x
    :param y: положение ячейки на экране по оси y
    :param p: отвечает за цвет фишки
    :param alpha: угол поворота фишки, если понадобится
    '''
    surface = pygame.Surface((a, a), pygame.SRCALPHA, 32)
    color_list1 = [GREEN, SILVER, ROYALBLUE, YELLOW, PURPLE, DARKORANGE, RED]
    color_list2 = [DARKGREEN, GRAY, BLUE, GOLD, INDIGO, ORANGERED, CRIMSON]

    polygon(surface, color_list1[p], [(int(a / 2 + k * a * math.sin(alpha / 180 * math.pi)),
                                       int(a / 2 - k * a * math.cos(alpha / 180 * math.pi))),
                                      (int(a / 2 + k * a * math.sin((36 - alpha) / 180 * math.pi)),
                                       int(a / 2 + k * a * math.cos((36 - alpha) / 180 * math.pi))),
                                      (int(a / 2 - k * a / (4 * math.cos(18 / 180 * math.pi) * math.cos(
                                          18 / 180 * math.pi) - 1) * math.sin(
                                          alpha / 180 * math.pi)),
                                       int(a / 2 + k * a / (4 * math.cos(18 / 180 * math.pi) * math.cos(
                                           18 / 180 * math.pi) - 1) * math.cos(
                                           alpha / 180 * math.pi))),
                                      (int(a / 2 - k * a * math.sin((36 + alpha) / 180 * math.pi)),
                                       int(a / 2 + k * a * math.cos((36 + alpha) / 180 * math.pi))),
                                      (int(a / 2 + k * a * math.sin(alpha / 180 * math.pi)),
                                       int(a / 2 - k * a * math.cos(alpha / 180 * math.pi)))])

    polygon(surface, color_list1[p], [(int(a / 2 - k * a * math.sin((72 - alpha) / 180 * math.pi)),
                                       int(a / 2 - k * a * math.cos((72 - alpha) / 180 * math.pi))),
                                      (int(a / 2 + k * a * math.sin((72 + alpha) / 180 * math.pi)),
                                       int(a / 2 - k * a * math.cos((72 + alpha) / 180 * math.pi))),
                                      (int(a / 2 - k * a * math.sin((36 + alpha) / 180 * math.pi)),
                                       int(a / 2 + k * a * math.cos((36 + alpha) / 180 * math.pi))),
                                      (int(a / 2 - k * a / (4 * math.cos(18 / 180 * math.pi) * math.cos(
                                          18 / 180 * math.pi) - 1) * math.sin(
                                          (72 + alpha) / 180 * math.pi)),
                                       int(a / 2 + k * a / (4 * math.cos(18 / 180 * math.pi) * math.cos(
                                           18 / 180 * math.pi) - 1) * math.cos(
                                           (72 + alpha) / 180 * math.pi))),
                                      (int(a / 2 - k * a * math.sin((72 - alpha) / 180 * math.pi)),
                                       int(a / 2 - k * a * math.cos((72 - alpha) / 180 * math.pi)))])
    # украшающие линии
    pygame.draw.lines(surface, color_list2[p], True,
                      [[int(a / 2 + k * a * math.sin(alpha / 180 * math.pi)),
                        int(a / 2 - k * a * math.cos(alpha / 180 * math.pi))],
                       [int(a / 2 + 0.38 * k * a * math.sin((alpha + 36) / 180 * math.pi)),
                        int(a / 2 - 0.38 * k * a * math.cos((alpha + 36) / 180 * math.pi))],
                       [int(a / 2 + k * a * math.sin((72 + alpha) / 180 * math.pi)),
                        int(a / 2 - k * a * math.cos((72 + alpha) / 180 * math.pi))],
                       [int(a / 2 + 0.38 * k * a * math.sin((alpha + 108) / 180 * math.pi)),
                        int(a / 2 - 0.38 * k * a * math.cos((alpha + 108) / 180 * math.pi))],
                       [int(a / 2 + k * a * math.sin((36 - alpha) / 180 * math.pi)),
                        int(a / 2 + k * a * math.cos((36 - alpha) / 180 * math.pi))],
                       [int(a / 2 - 0.38 * k * a * math.sin(alpha / 180 * math.pi)),
                        int(a / 2 + 0.38 * k * a * math.cos(alpha / 180 * math.pi))],
                       [int(a / 2 - k * a * math.sin((36 + alpha) / 180 * math.pi)),
                        int(a / 2 + k * a * math.cos((36 + alpha) / 180 * math.pi))],
                       [int(a / 2 - 0.38 * k * a * math.sin((- alpha + 108) / 180 * math.pi)),
                        int(a / 2 - 0.38 * k * a * math.cos((- alpha + 108) / 180 * math.pi))],
                       [int(a / 2 - k * a * math.sin((72 - alpha) / 180 * math.pi)),
                        int(a / 2 - k * a * math.cos((72 - alpha) / 180 * math.pi))],
                       [int(a / 2 - 0.38 * k * a * math.sin((- alpha + 36) / 180 * math.pi)),
                        int(a / 2 - 0.38 * k * a * math.cos((- alpha + 36) / 180 * math.pi))]], 3)
    for i in range(0, 5, 1):
        pygame.draw.line(surface, color_list2[p], (int(a / 2), int(a / 2)),
                         (int(a / 2 + k * a * math.sin((alpha + i * 72) / 180 * math.pi)),
                          int(a / 2 - k * a * math.cos(((alpha + i * 72) / 180 * math.pi)))), 3)
    surf.blit(surface, (x, y))


def draw_uzor(surf, x, y, b):
    '''
    рисует красивый узор для поля
    :param surf: поверхность, на которой рисуется узор
    :param x: положение на экране по оси x
    :param y: положение на экране по оси y
    :param b: характерный размер узора
    '''
    pygame.draw.rect(surf, DIMGREY, (int(x - 0.3 * b), int(y - 0.3 * b), int(0.6 * b), int(0.6 * b)), 1)
    pygame.draw.lines(surf, DIMGREY, True, [[int(x - 0.35 * b), int(y - 0.35 * b)],
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
                                            [int(x - 0.35 * b), int(y + 0.1 * b)],
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
    pygame.draw.lines(surf, DIMGREY, False, [[int(x + 0.45 * b), int(y - 0.35 * b)],
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

    pygame.draw.lines(surf, spiral_color, False, [[int(x + 0.5 * b - (-1) ** n * 0.1 * b), int(y + 0.4 * b)],
                                                  [int(x + 0.5 * b + (-1) ** n * 0.1 * b), int(y + 0.4 * b)],
                                                  [int(x + 0.5 * b + (-1) ** n * 0.1 * b), int(y + 0.6 * b)],
                                                  [int(x + 0.5 * b - (-1) ** n * 0.3 * b), int(y + 0.6 * b)],
                                                  [int(x + 0.5 * b - (-1) ** n * 0.3 * b), int(y + 0.2 * b)],
                                                  [int(x + 0.5 * b + (-1) ** n * 0.3 * b), int(y + 0.2 * b)],
                                                  [int(x + 0.5 * b + (-1) ** n * 0.3 * b), int(y + 0.8 * b)],
                                                  [int(x + 0.5 * b - (-1) ** n * 0.5 * b), int(y + 0.8 * b)],
                                                  [int(x + 0.5 * b - (-1) ** n * 0.5 * b), int(y)],
                                                  [int(x + 0.5 * b + (-1) ** n * 0.5 * b), int(y)],
                                                  [int(x + 0.5 * b + (-1) ** n * 0.5 * b), int(y + b)],
                                                  [int(x + 0.5 * b - (-1) ** n * 0.5 * b), int(y + b)],
                                                  [int(x + 0.5 * b - (-1) ** n * 0.5 * b), int(y + 2 * b)],
                                                  [int(x + 0.5 * b + (-1) ** n * 0.5 * b), int(y + 2 * b)],
                                                  [int(x + 0.5 * b + (-1) ** n * 0.5 * b), int(y + 1.2 * b)],
                                                  [int(x + 0.5 * b - (-1) ** n * 0.3 * b), int(y + 1.2 * b)],
                                                  [int(x + 0.5 * b - (-1) ** n * 0.3 * b), int(y + 1.8 * b)],
                                                  [int(x + 0.5 * b + (-1) ** n * 0.3 * b), int(y + 1.8 * b)],
                                                  [int(x + 0.5 * b + (-1) ** n * 0.3 * b), int(y + 1.4 * b)],
                                                  [int(x + 0.5 * b - (-1) ** n * 0.1 * b), int(y + 1.4 * b)],
                                                  [int(x + 0.5 * b - (-1) ** n * 0.1 * b), int(y + 1.6 * b)],
                                                  [int(x + 0.5 * b + (-1) ** n * 0.1 * b), int(y + 1.6 * b)]])


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
                                                  [int(x + 0.8 * b), int(y + 0.5 * b - (-1) ** n * 0.5 * b)],
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


def draw_pole_without_border(surf, n, a, color1, color2, x, y, b):
    pygame.draw.rect(surf, color1, (int(x), int(y), int(n * a), int(n * a)))
    for i in range(0, n + 1, 1):
        for j in range(0, n, 1):
            pygame.draw.line(surf, color2, (int(x + j * a + 0.65 * b), int(y + i * a)),
                             (int(x + (j + 1) * a - 0.65 * b), int(y + i * a)), 2)
            pygame.draw.line(surf, color2, (int(x + i * a), int(y + j * a + 0.65 * b)),
                             (int(x + i * a), int(y + (j + 1) * a - 0.65 * b)), 2)
    for i in range(0, n + 1, 1):
        for j in range(0, n + 1, 1):
            draw_uzor(surf, x + i * a, y + j * a, b)


def draw_pole(surf, n, a, color1, color2, x, y, b):
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
    pygame.draw.rect(surf, color1, (int(x), int(y), int(n * a), int(n * a)))
    for i in range(0, n + 1, 1):
        for j in range(0, n, 1):
            pygame.draw.line(surf, color2, (int(x + j * a + 0.65 * b), int(y + i * a)),
                             (int(x + (j + 1) * a - 0.65 * b), int(y + i * a)), 2)
            pygame.draw.line(surf, color2, (int(x + i * a), int(y + j * a + 0.65 * b)),
                             (int(x + i * a), int(y + (j + 1) * a - 0.65 * b)), 2)
    for i in range(0, n + 1, 1):
        for j in range(0, n + 1, 1):
            draw_uzor(surf, x + i * a, y + j * a, b)

    for i in range(0, n + 1, 1):
        draw_border1(surf, int(x + n * a), int(y - a / 2 + a * i), DARKGOLDENROD, DIMGREY, int(a / 2), 0)
    for i in range(0, n + 1, 1):
        draw_border1(surf, int(x - a / 2), int(y - a / 2 + a * i), DARKGOLDENROD, DIMGREY, int(a / 2), 1)
    for i in range(0, n, 1):
        draw_border2(surf, int(x + i * a), int(y - a / 2), DARKGOLDENROD, DIMGREY, int(a / 2), 0)
    for i in range(0, n, 1):
        draw_border2(surf, int(x + i * a), int(y + n * a), DARKGOLDENROD, DIMGREY, int(a / 2), 1)


def draw_bonus_cross(surf, x, y, a):
    '''
    рисует бонус, который "срезает" фишки крест накрест
    :param surf: поверхность отрисовки
    :param x: положение центра бонуса по оси x
    :param y: положение центра бонуса по оси y
    :param a: характерный размер бонуса
    '''

    pygame.draw.circle(surf, DARKGREY, (int(x), int(y)), int(a), 2)
    pygame.draw.circle(surf, STEELBLUE, (x, y), a - 2, 2)

    pygame.draw.ellipse(surf, STEELBLUE, (int(x - 0.2 * a), int(y - 1.15 * a), int(0.4 * a), int(0.2 * a)))
    pygame.draw.ellipse(surf, BLACK, (int(x - 0.1 * a), int(y - 1.1 * a), int(0.2 * a), int(0.1 * a)))

    pygame.draw.ellipse(surf, STEELBLUE, (int(x - 0.2 * a), int(y + 0.96 * a), int(0.4 * a), int(0.2 * a)))
    pygame.draw.ellipse(surf, BLACK, (int(x - 0.1 * a), int(y + 1.02 * a), int(0.2 * a), int(0.1 * a)))

    pygame.draw.ellipse(surf, STEELBLUE, (int(x - 1.15 * a), int(y - 0.2 * a), int(0.2 * a), int(0.4 * a)))
    pygame.draw.ellipse(surf, BLACK, (int(x - 1.1 * a), int(y - 0.1 * a), int(0.1 * a), int(0.2 * a)))

    pygame.draw.ellipse(surf, STEELBLUE, (int(x + 0.98 * a), int(y - 0.2 * a), int(0.2 * a), int(0.4 * a)))
    pygame.draw.ellipse(surf, BLACK, (int(x + 1.04 * a), int(y - 0.1 * a), int(0.1 * a), int(0.2 * a)))

    cross_animation(surf, x, y, a)


def cross_animation(surf, x, y, a):
    '''
    функция рисует анимацию фишки, при наложении бонуса на неё
    :param surf: поверхность отрисовки
    :param x: координата центра по оси x
    :param y: координата центра по оси y
    :param a: характерный размер
    '''
    pygame.draw.circle(surf, LIGHTYELLOW, (int(x), int(y)), int(0.15 * a))
    q = randint(0, 2)
    alpha = []  # лист для углов поворота молний внутри бонуса
    for i in range(0, q, 1):
        alpha.append(randint(0, 360))
    for i in range(0, q, 1):
        pygame.draw.line(surf, LIGHTYELLOW, (int(x), int(y)),
                         (int(x + 0.5 * a * math.sin(math.pi * alpha[i] / 180)),
                          int(y + 0.5 * a * math.cos(math.pi * alpha[i] / 180))))
        pygame.draw.line(surf, VIOLET,
                         (int(x + 0.5 * a * math.sin(math.pi * alpha[i] / 180)),
                          int(y + 0.5 * a * math.cos(math.pi * alpha[i] / 180))),
                         (int(x + 0.6 * a * math.sin(math.pi * alpha[i] / 180 + 0.26)),
                          int(y + 0.6 * a * math.cos(math.pi * alpha[i] / 180 + 0.26))))
        pygame.draw.line(surf, LIGHTYELLOW,
                         (int(x + 0.6 * a * math.sin(math.pi * alpha[i] / 180 + 0.26)),
                          int(y + 0.6 * a * math.cos(math.pi * alpha[i] / 180 + 0.26))),
                         (int(x + 0.8 * a * math.sin(math.pi * alpha[i] / 180 + 0.26)),
                          int(y + 0.8 * a * math.cos(math.pi * alpha[i] / 180 + 0.26))))
        pygame.draw.line(surf, VIOLET,
                         (int(x + 0.8 * a * math.sin(math.pi * alpha[i] / 180 + 0.26)),
                          int(y + 0.8 * a * math.cos(math.pi * alpha[i] / 180 + 0.26))),
                         (int(x + 1.0 * a * math.sin(math.pi * alpha[i] / 180 + 0.52)),
                          int(y + 1.0 * a * math.cos(math.pi * alpha[i] / 180 + 0.52))))
        pygame.draw.line(surf, VIOLET,
                         (int(x + 0.5 * a * math.sin(math.pi * alpha[i] / 180)),
                          int(y + 0.5 * a * math.cos(math.pi * alpha[i] / 180))),
                         (int(x + 0.7 * a * math.sin(math.pi * alpha[i] / 180 + 0.14)),
                          int(y + 0.7 * a * math.cos(math.pi * alpha[i] / 180 + 0.14))))
        pygame.draw.line(surf, LIGHTYELLOW,
                         (int(x + 0.7 * a * math.sin(math.pi * alpha[i] / 180 + 0.14)),
                          int(y + 0.7 * a * math.cos(math.pi * alpha[i] / 180 + 0.14))),
                         (int(x + 1.0 * a * math.sin(math.pi * alpha[i] / 180 - 0.02)),
                          int(y + 1.0 * a * math.cos(math.pi * alpha[i] / 180 - 0.02))))


def draw_bonus_dynamite(surf, x, y, a):
    '''
    функция рисует бонус динамит
    :param surf: поверхность отрисовки изображения
    :param x: кооржината центра по оси x
    :param y: координата центра по оси y
    :param a: характерный размер
    '''
    # тело динамита
    pygame.draw.circle(surf, TOMATO, (int(x - 0.2 * a), int(y + 0.4 * a)), int(0.1 * a))
    pygame.draw.polygon(surf, TOMATO, [[int(x - 0.25 * a), int(y + 0.3 * a)],
                                       [int(x + 0.4 * a), int(y + 0.06 * a)],
                                       [int(x + 0.44 * a), int(y + 0.25 * a)],
                                       [int(x - 0.19 * a), int(y + 0.50 * a)]])

    pygame.draw.polygon(surf, DARKRED, [[int(x + 0.44 * a), int(y + 0.25 * a)],
                                        [int(x - 0.19 * a), int(y + 0.50 * a)],
                                        [int(x - 0.23 * a), int(y + 0.48 * a)],
                                        [int(x + 0.44 * a), int(y + 0.21 * a)]])
    pygame.draw.polygon(surf, ORANGE, [[int(x - 0.25 * a), int(y + 0.3 * a)],
                                       [int(x + 0.4 * a), int(y + 0.06 * a)],
                                       [int(x + 0.42 * a), int(y + 0.09 * a)],
                                       [int(x - 0.29 * a), int(y + 0.36 * a)]])
    pygame.draw.circle(surf, FIREBRICK, (int(x + 0.43 * a), int(y + 0.16 * a)), int(0.1 * a))
    pygame.draw.circle(surf, TOMATO, (int(x + 0.43 * a), int(y + 0.16 * a)), int(0.1 * a), 2)
    # обвивающая веревка(почти вертикальная)
    pygame.draw.arc(surf, SIENNA, (int(x - 0.8 * a), int(y - 0.8 * a), int(0.8 * a), int(1.8 * a)), -0.42, 0.63, 5)
    # координты штрихов на веревке по оси x
    list_x1 = [int(x - 0.07 * a), int(x - 0.02 * a),
               int(x - 0.06 * a), int(x - 0.02 * a), int(x - 0.05 * a), int(x - 0.02 * a),
               int(x - 0.05 * a), int(x - 0.01 * a), int(x - 0.05 * a), int(x - 0.01 * a),
               int(x - 0.05 * a), int(x - 0.01 * a), int(x - 0.05 * a), int(x - 0.01 * a),
               int(x - 0.06 * a), int(x - 0.02 * a), int(x - 0.06 * a), int(x - 0.02 * a),
               int(x - 0.07 * a), int(x - 0.04 * a), int(x - 0.08 * a), int(x - 0.07 * a)]
    # координаты штрихов на веревке по оси y
    list_y1 = [int(y + 0.45 * a), int(y + 0.35 * a),
               int(y + 0.36 * a), int(y + 0.28 * a), int(y + 0.29 * a), int(y + 0.21 * a),
               int(y + 0.22 * a), int(y + 0.14 * a), int(y + 0.15 * a), int(y + 0.07 * a),
               int(y + 0.08 * a), int(y + 0.00 * a), int(y + 0.01 * a), int(y - 0.07 * a),
               int(y - 0.06 * a), int(y - 0.16 * a), int(y - 0.15 * a), int(y - 0.24 * a),
               int(y - 0.23 * a), int(y - 0.34 * a), int(y - 0.33 * a), int(y - 0.41 * a)]
    for i in range(int(0.5 * len(list_x1))):
        pygame.draw.line(surf, TAN, (list_x1[2 * i], list_y1[2 * i]),
                         (list_x1[2 * i + 1], list_y1[2 * i + 1]), 1)
    # вторая обвивающая веревка
    pygame.draw.arc(surf, SIENNA, (int(x - 1.2 * a), int(y - 0.02 * a), int(1.4 * a), int(0.8 * a)), 0.1, 1.4, 5)
    # координаты штрихов для этой верёвке по оси  x
    list_x2 = [int(x + 0.16 * a), int(x + 0.17 * a), int(x + 0.13 * a), int(x + 0.14 * a),
               int(x + 0.10 * a), int(x + 0.1 * a), int(x + 0.07 * a), int(x + 0.06 * a),
               int(x + 0.03 * a), int(x + 0.02 * a), int(x + 0.00 * a), int(x - 0.01 * a),
               int(x - 0.03 * a), int(x - 0.05 * a), int(x - 0.07 * a), int(x - 0.09 * a),
               int(x - 0.10 * a), int(x - 0.13 * a), int(x - 0.14 * a), int(x - 0.19 * a),
               int(x - 0.22 * a), int(x - 0.25 * a), int(x - 0.27 * a), int(x - 0.32 * a),
               int(x - 0.29 * a), int(x - 0.34 * a)]
    # координаты штрихов для этой верёвки по оси y
    list_y2 = [int(y + 0.35 * a), int(y + 0.28 * a), int(y + 0.30 * a), int(y + 0.23 * a),
               int(y + 0.25 * a), int(y + 0.18 * a), int(y + 0.21 * a), int(y + 0.14 * a),
               int(y + 0.18 * a), int(y + 0.12 * a), int(y + 0.16 * a), int(y + 0.10 * a),
               int(y + 0.13 * a), int(y + 0.07 * a), int(y + 0.11 * a), int(y + 0.04 * a),
               int(y + 0.09 * a), int(y + 0.04 * a), int(y + 0.07 * a), int(y + 0.02 * a),
               int(y + 0.05 * a), int(y + 0.00 * a), int(y + 0.03 * a), int(y - 0.02 * a),
               int(y + 0.01 * a), int(y - 0.03 * a)]
    for i in range(int(0.5 * len(list_x2))):
        pygame.draw.line(surf, TAN, (list_x2[2 * i], list_y2[2 * i]),
                         (list_x2[2 * i + 1], list_y2[2 * i + 1]), 1)

    # веревка от динамита
    pygame.draw.arc(surf, SIENNA, (int(x + 0.07 * a), int(y - 0.2 * a), int(0.4 * a), int(0.6 * a)), -0.2, 1.4, 5)
    # координтаты штрихов динамитной веревки по оси x
    list_x3 = [int(x + 0.42 * a), int(x + 0.46 * a), int(x + 0.42 * a), int(x + 0.46 * a),
               int(x + 0.42 * a), int(x + 0.45 * a), int(x + 0.41 * a), int(x + 0.43 * a),
               int(x + 0.38 * a), int(x + 0.37 * a), int(x + 0.35 * a), int(x + 0.34 * a)]
    # координаты штрихов динамитно веревки по оси y
    list_y3 = [int(y + 0.15 * a), int(y + 0.10 * a), int(y + 0.09 * a), int(y + 0.03 * a),
               int(y + 0.04 * a), int(y - 0.02 * a), int(y - 0.03 * a), int(y - 0.09 * a),
               int(y - 0.1 * a), int(y - 0.16 * a), int(y - 0.13 * a), int(y - 0.17 * a)]
    for i in range(int(0.5 * len(list_x3))):
        pygame.draw.line(surf, TAN, (list_x3[2 * i], list_y3[2 * i]),
                         (list_x3[2 * i + 1], list_y3[2 * i + 1]), 1)

    dynamite_animation(surf, x + 0.3 * a, y - 0.2 * a, 0.1 * a)


def dynamite_animation(surf, x, y, a):
    '''
    функция рисует анимацию огонька у динамита
    :param surf: поверхность отрисовки
    :param x: координата анимации по оси x
    :param y: координата анимации по оси y
    :param a: характерный размер анимации
    '''

    list_r = []  # радиус вершины n - угольника
    list_angle = []  # угол оносительно вертикали
    for i in range(0, 20, 1):
        list_r.append(a * random.uniform(0.4, 0.8))
        list_angle.append(random.uniform(0, 6.18))
    list_x = []
    list_y = []
    for i in range(0, 20, 1):
        list_x.append(int(x + list_r[i] * math.sin(list_angle[i])))
        list_y.append(int(y - list_r[i] * math.cos(list_angle[i])))
    list_coords = []
    for i in range(0, 20, 1):
        list_coords.append([list_x[i], list_y[i]])
    polygon(surf, LIGHTYELLOW, list_coords)


def almaz_animation(surf, x, y, a):
    """
    рисует анимацию бликов на драгоценном камне
    :param surf: плоскость отрисовки
    :param x: координата центра анимации по оси x
    :param y: координата центра анимации по оси y
    :param a: характерный размер
    """
    # return
    p = randint(1, 3)
    list_x = []
    list_y = []
    for i in range(0, p, 1):
        list_x.append(randint(int(- a + x), int(a + x)))
        list_y.append(randint(int(- a + y), int(a + y)))
    for i in range(0, p, 1):
        pygame.draw.circle(surf, WHITE, (list_x[i], list_y[i]), 2)


def draw_watch(surf, x, y, a, time, time_0):
    '''
    функция отвечает за работу часов
    :param surf: поверхность, на которой отображаются часы
    :param x: координата центра часов по оси x
    :param y: координата центра часов по оси y
    :param a: характерный размер часов
    :param time: время, оставшееся для игры
    :param time_0: начальное время игры
    '''
    pygame.draw.circle(surf, SILVER, (int(x), int(y)), int(0.95 * a))
    pygame.draw.circle(surf, GOLD, (int(x), int(y)), int(a), int(0.1 * a))
    pygame.draw.circle(surf, GOLDENROD, (int(x), int(y)), int(0.9 * a), 2)
    phi = - 6 * (time / 60)
    alpha = - 30 * (time / 3600)
    # рисуем подсветку времени на часах
    if 0.8 * time_0 <= time <= time_0:
        for i in range(0, 100, 1):
            pygame.draw.polygon(surf, GREEN, [[int(x + 0.84 * a * math.sin((i * phi / 100 / 180 * math.pi))),
                                               int(y - 0.84 * a * math.cos((i * phi / 100 / 180 * math.pi)))],
                                              [int(x + 0.84 * a * math.sin((i + 1) * phi / 100 / 180 * math.pi)),
                                               int(y - 0.84 * a * math.cos((i + 1) * phi / 100 / 180 * math.pi))],
                                              [int(x), int(y)]])
    if 0.6 * time_0 <= time < 0.8 * time_0:
        for i in range(0, 100, 1):
            pygame.draw.polygon(surf, OLIVEDRAB, [[int(x + 0.84 * a * math.sin((i * phi / 100 / 180 * math.pi))),
                                                   int(y - 0.84 * a * math.cos((i * phi / 100 / 180 * math.pi)))],
                                                  [int(x + 0.84 * a * math.sin((i + 1) * phi / 100 / 180 * math.pi)),
                                                   int(y - 0.84 * a * math.cos((i + 1) * phi / 100 / 180 * math.pi))],
                                                  [int(x), int(y)]])
    if 0.4 * time_0 <= time < 0.6 * time_0:
        for i in range(0, 100, 1):
            pygame.draw.polygon(surf, YELLOW, [[int(x + 0.84 * a * math.sin((i * phi / 100 / 180 * math.pi))),
                                                int(y - 0.84 * a * math.cos((i * phi / 100 / 180 * math.pi)))],
                                               [int(x + 0.84 * a * math.sin((i + 1) * phi / 100 / 180 * math.pi)),
                                                int(y - 0.84 * a * math.cos((i + 1) * phi / 100 / 180 * math.pi))],
                                               [int(x), int(y)]])
    if 0.2 * time_0 <= time < 0.4 * time_0:
        for i in range(0, 100, 1):
            pygame.draw.polygon(surf, CRIMSON, [[int(x + 0.84 * a * math.sin((i * phi / 100 / 180 * math.pi))),
                                                 int(y - 0.84 * a * math.cos((i * phi / 100 / 180 * math.pi)))],
                                                [int(x + 0.84 * a * math.sin((i + 1) * phi / 100 / 180 * math.pi)),
                                                 int(y - 0.84 * a * math.cos((i + 1) * phi / 100 / 180 * math.pi))],
                                                [int(x), int(y)]])
    if 0.0 * time_0 <= time < 0.2 * time_0:
        for i in range(0, 100, 1):
            pygame.draw.polygon(surf, DARKRED, [[int(x + 0.84 * a * math.sin((i * phi / 100 / 180 * math.pi))),
                                                 int(y - 0.84 * a * math.cos((i * phi / 100 / 180 * math.pi)))],
                                                [int(x + 0.84 * a * math.sin((i + 1) * phi / 100 / 180 * math.pi)),
                                                 int(y - 0.84 * a * math.cos((i + 1) * phi / 100 / 180 * math.pi))],
                                                [int(x), int(y)]])
    # рисуем часовую стрелку

    pygame.draw.circle(surf, BLACK, (int(x), int(y)), int(0.1 * a), 1)
    pygame.draw.polygon(surf, BLACK, [[int(x + 0.07 * a * math.sin((alpha + 20) / 180 * math.pi)),
                                       int(y - 0.07 * a * math.cos((alpha + 20) / 180 * math.pi))],
                                      [int(x + 0.15 * a * math.sin((alpha + 30) / 180 * math.pi)),
                                       int(y - 0.15 * a * math.cos((alpha + 30) / 180 * math.pi))],
                                      [int(x + 0.2 * a * math.sin((alpha + 10) / 180 * math.pi)),
                                       int(y - 0.2 * a * math.cos((alpha + 10) / 180 * math.pi))],
                                      [int(x + 0.2 * a * math.sin((alpha - 10) / 180 * math.pi)),
                                       int(y - 0.2 * a * math.cos((alpha - 10) / 180 * math.pi))],
                                      [int(x + 0.15 * a * math.sin((alpha - 30) / 180 * math.pi)),
                                       int(y - 0.15 * a * math.cos((alpha - 30) / 180 * math.pi))],
                                      [int(x + 0.07 * a * math.sin((alpha - 20) / 180 * math.pi)),
                                       int(y - 0.07 * a * math.cos((alpha - 20) / 180 * math.pi))]])
    pygame.draw.polygon(surf, BLACK, [[int(x + 0.18 * a * math.sin((alpha) / 180 * math.pi)),
                                       int(y - 0.18 * a * math.cos((alpha) / 180 * math.pi))],
                                      [int(x + 0.3 * a * math.sin((alpha + 5) / 180 * math.pi)),
                                       int(y - 0.3 * a * math.cos((alpha + 5) / 180 * math.pi))],
                                      [int(x + 0.4 * a * math.sin(alpha / 180 * math.pi)),
                                       int(y - 0.4 * a * math.cos(alpha / 180 * math.pi))],
                                      [int(x + 0.3 * a * math.sin((alpha - 5) / 180 * math.pi)),
                                       int(y - 0.3 * a * math.cos((alpha - 5) / 180 * math.pi))]])
    pygame.draw.polygon(surf, BLACK, [[int(x + 0.36 * a * math.sin((alpha + 7) / 180 * math.pi)),
                                       int(y - 0.36 * a * math.cos((alpha + 7) / 180 * math.pi))],
                                      [int(x + 0.42 * a * math.sin((alpha + 9) / 180 * math.pi)),
                                       int(y - 0.42 * a * math.cos((alpha + 9) / 180 * math.pi))],
                                      [int(x + 0.46 * a * math.sin((alpha + 4) / 180 * math.pi)),
                                       int(y - 0.46 * a * math.cos((alpha + 4) / 180 * math.pi))],
                                      [int(x + 0.46 * a * math.sin((alpha - 4) / 180 * math.pi)),
                                       int(y - 0.46 * a * math.cos((alpha - 4) / 180 * math.pi))],
                                      [int(x + 0.42 * a * math.sin((alpha - 9) / 180 * math.pi)),
                                       int(y - 0.42 * a * math.cos((alpha - 9) / 180 * math.pi))],
                                      [int(x + 0.36 * a * math.sin((alpha - 7) / 180 * math.pi)),
                                       int(y - 0.36 * a * math.cos((alpha - 7) / 180 * math.pi))]])
    pygame.draw.lines(surf, BLACK, True, [[int(x + 0.45 * a * math.sin(alpha / 180 * math.pi)),
                                           int(y - 0.45 * a * math.cos(alpha / 180 * math.pi))],
                                          [int(x + 0.53 * a * math.sin((alpha + 5) / 180 * math.pi)),
                                           int(y - 0.53 * a * math.cos((alpha + 5) / 180 * math.pi))],
                                          [int(x + 0.62 * a * math.sin(alpha / 180 * math.pi)),
                                           int(y - 0.62 * a * math.cos(alpha / 180 * math.pi))],
                                          [int(x + 0.53 * a * math.sin((alpha - 5) / 180 * math.pi)),
                                           int(y - 0.53 * a * math.cos((alpha - 5) / 180 * math.pi))]], 2)

    # рисуем минутную стрелку

    pygame.draw.circle(surf, BLACK, (int(x), int(y)), int(0.1 * a), 1)
    pygame.draw.polygon(surf, BLACK, [[int(x + 0.07 * a * math.sin((phi + 20) / 180 * math.pi)),
                                       int(y - 0.07 * a * math.cos((phi + 20) / 180 * math.pi))],
                                      [int(x + 0.10 * a * math.sin((phi + 30) / 180 * math.pi)),
                                       int(y - 0.10 * a * math.cos((phi + 30) / 180 * math.pi))],
                                      [int(x + 0.13 * a * math.sin((phi + 10) / 180 * math.pi)),
                                       int(y - 0.13 * a * math.cos((phi + 10) / 180 * math.pi))],
                                      [int(x + 0.13 * a * math.sin((phi - 10) / 180 * math.pi)),
                                       int(y - 0.13 * a * math.cos((phi - 10) / 180 * math.pi))],
                                      [int(x + 0.10 * a * math.sin((phi - 30) / 180 * math.pi)),
                                       int(y - 0.10 * a * math.cos((phi - 30) / 180 * math.pi))],
                                      [int(x + 0.07 * a * math.sin((phi - 20) / 180 * math.pi)),
                                       int(y - 0.07 * a * math.cos((phi - 20) / 180 * math.pi))]])
    pygame.draw.polygon(surf, BLACK, [[int(x + 0.12 * a * math.sin((phi) / 180 * math.pi)),
                                       int(y - 0.12 * a * math.cos((phi) / 180 * math.pi))],
                                      [int(x + 0.26 * a * math.sin((phi + 11) / 180 * math.pi)),
                                       int(y - 0.26 * a * math.cos((phi + 11) / 180 * math.pi))],
                                      [int(x + 0.40 * a * math.sin(phi / 180 * math.pi)),
                                       int(y - 0.40 * a * math.cos(phi / 180 * math.pi))],
                                      [int(x + 0.26 * a * math.sin((phi - 11) / 180 * math.pi)),
                                       int(y - 0.26 * a * math.cos((phi - 11) / 180 * math.pi))]])
    pygame.draw.polygon(surf, BLACK, [[int(x + 0.35 * a * math.sin((phi + 7) / 180 * math.pi)),
                                       int(y - 0.35 * a * math.cos((phi + 7) / 180 * math.pi))],
                                      [int(x + 0.37 * a * math.sin((phi + 9) / 180 * math.pi)),
                                       int(y - 0.37 * a * math.cos((phi + 9) / 180 * math.pi))],
                                      [int(x + 0.41 * a * math.sin((phi + 4) / 180 * math.pi)),
                                       int(y - 0.41 * a * math.cos((phi + 4) / 180 * math.pi))],
                                      [int(x + 0.41 * a * math.sin((phi - 4) / 180 * math.pi)),
                                       int(y - 0.41 * a * math.cos((phi - 4) / 180 * math.pi))],
                                      [int(x + 0.37 * a * math.sin((phi - 9) / 180 * math.pi)),
                                       int(y - 0.37 * a * math.cos((phi - 9) / 180 * math.pi))],
                                      [int(x + 0.35 * a * math.sin((phi - 7) / 180 * math.pi)),
                                       int(y - 0.35 * a * math.cos((phi - 7) / 180 * math.pi))]])
    pygame.draw.lines(surf, BLACK, True, [[int(x + 0.40 * a * math.sin(phi / 180 * math.pi)),
                                           int(y - 0.40 * a * math.cos(phi / 180 * math.pi))],
                                          [int(x + 0.53 * a * math.sin((phi + 4) / 180 * math.pi)),
                                           int(y - 0.53 * a * math.cos((phi + 4) / 180 * math.pi))],
                                          [int(x + 0.68 * a * math.sin(phi / 180 * math.pi)),
                                           int(y - 0.68 * a * math.cos(phi / 180 * math.pi))],
                                          [int(x + 0.53 * a * math.sin((phi - 4) / 180 * math.pi)),
                                           int(y - 0.53 * a * math.cos((phi - 4) / 180 * math.pi))]], 2)

    # рисуем цифры
    for i in range(0, 12, 1):
        text = font.render(str(i), True, BLACK, SILVER)
        textRect = text.get_rect()
        place = text.get_rect(center=(int(x - 0.75 * a * math.sin(2 * math.pi / 12 * i)),
                                      int(y - 0.75 * a * math.cos(2 * math.pi / 12 * i))))
        surf.blit(text, place)


def beautiful_draw(surf, x, y, a, color, cristall=False, rainbow=0, bonus=0):
    k = 0.4
    a_cristall = int(k * a / 3 * math.sqrt(2))
    x_cristall = x + a // 2
    y_cristall = y + a // 2
    if rainbow:
        multi_chip(a, surf, k * 1.25, x, y, random.randint(0, 5), 0)
    else:
        if color == RED:
            red_chip(a, surf, k, x, y)
            if cristall:
                red_stone(a_cristall, surf, x_cristall, y_cristall)
        if color == ORANGE:
            orange_chip(a, surf, k, x, y)
            if cristall:
                orange_stone(a_cristall, surf, x_cristall, y_cristall)
        if color == YELLOW:
            yellow_chip(a, surf, k, x, y)
            if cristall:
                yellow_stone(a_cristall, surf, x_cristall, y_cristall)
        if color == GREEN:
            green_chip(a, surf, k, x, y)
            if cristall:
                green_stone(a_cristall, surf, x_cristall, y_cristall)
        if color == BLUE:
            blue_chip(a, surf, k, x, y)
            if cristall:
                blue_stone(a_cristall, surf, x_cristall, y_cristall)
        if color == PURPLE:
            purple_chip(a, surf, k, x, y)
            if cristall:
                purple_stone(a_cristall, surf, x_cristall, y_cristall)
        if color == DIMGREY:
            gray_chip(a, surf, k, x, y)
            if cristall:
                gray_stone(a_cristall, surf, x_cristall, y_cristall)

    if bonus == 1:
        draw_bonus_dynamite(surf, x_cristall, y_cristall, a)
    if bonus == 2:
        draw_bonus_cross(surf, x_cristall, y_cristall, a // 2)

def stone_heap(surf, x, y, a):
    k=0.7
    a=int(k * a / 3 * math.sqrt(2))
    red_stone(a,surf,int(x*1.0),int(y*1.0))
    orange_stone(a,surf,int(x*0.8),int(y*1.3))
    yellow_stone(a, surf, int(x * 1.2), int(y * 1.3))
    green_stone(a, surf, int(x * 0.6), int(y * 1.6))
    blue_stone(a, surf, int(x * 1.0), int(y * 1.6))
    purple_stone(a, surf, int(x * 1.4), int(y * 1.6))
    gray_stone(a, surf, int(x * 1.6), int(y * 1.6))


if __name__=='__main__':
    FPS = 30
    screen = pygame.display.set_mode((800, 600))
    screen.fill(WHITE)
    clock = pygame.time.Clock()
    finished = False

    t = 0
    n = 0
    time = 4000
    time_0 = 4000
    while not finished:

        clock.tick(FPS)
        draw_pole(screen, 4, 50, CADETBLUE, DIMGREY, 250, 100, 16)

        gray_chip(100, screen, 0.4, 290, 270)
        gray_stone(int(0.4 * 100 / 3 * math.sqrt(2)), screen, 340, 320)

        orange_chip(100, screen, 0.4, 100, 100)
        orange_stone(int(0.4 * 100 / 3 * math.sqrt(2)), screen, 150, 150)
        draw_bonus_dynamite(screen, 150, 150, 100)

        draw_bonus_cross(screen, 300, 240, 50)

        blue_chip(100, screen, 0.4, 650, 300)
        blue_stone(int(0.4 * 100 / 3 * math.sqrt(2)), screen, 700, 350)
        draw_bonus_dynamite(screen, 700, 350, 100)

        green_chip(100, screen, 0.4, 200, 300)
        green_stone(int(0.4 * 100 / 3 * math.sqrt(2)), screen, 250, 350)

        yellow_chip(100, screen, 0.4, 600, 100)
        yellow_stone(int(0.4 * 100 / 3 * math.sqrt(2)), screen, 650, 150)

        purple_chip(100, screen, 0.4, 100, 200)
        purple_stone(int(0.4 * 100 / 3 * math.sqrt(2)), screen, 150, 250)

        t += 1
        time -= 5
        draw_watch(screen, 100, 400, 100, time, time_0)
        if t%15 == 0:
            n = randint(0, 6)
        multi_chip(100, screen, 0.4, 500, 500, n, 0)

        red_chip(100, screen, 0.4, 500, 400)
        red_stone(int(0.4 * 100 / 3 * math.sqrt(2)), screen, 550, 450)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
        pygame.display.update()
    pygame.quit()
