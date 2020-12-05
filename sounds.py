from os import path
import pygame


snd_dir = path.join(path.dirname(__file__),'snd')

pygame.init()
pygame.mixer.init()

explosion_sound=pygame.mixer.Sound(path.join(snd_dir, 'Explosion.wav'))
move_sound = pygame.mixer.Sound(path.join(snd_dir, 'blip.wav'))
#pygame.mixer.music.load(path.join(snd_dir, 'regression_cyclone_0.ogg'))
pygame.mixer.music.load(path.join(snd_dir, 'Music.mp3'))

pygame.mixer.music.set_volume(0.4)