from os import path
import pygame

img_dir = path.join(path.dirname(__file__), "img")
pygame.init()
pravila_img = pygame.image.load(path.join(img_dir, "1.png")).convert()
