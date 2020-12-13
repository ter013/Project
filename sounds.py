from os import path
import pygame


snd_dir = path.join(path.dirname(__file__),'snd')

pygame.init()
pygame.mixer.init()
#Звуки игровые
explosion_sound=pygame.mixer.Sound(path.join(snd_dir, 'Explosion.wav'))
move_sound = pygame.mixer.Sound(path.join(snd_dir, 'blip.wav'))
wow_sound = pygame.mixer.Sound(path.join(snd_dir, 'wow for molnia.wav'))
sound_1 = pygame.mixer.Sound(path.join(snd_dir, '50.wav'))
sound_2 = pygame.mixer.Sound(path.join(snd_dir, '100.wav'))
sound_3 = pygame.mixer.Sound(path.join(snd_dir, '500.wav'))
star_sound=pygame.mixer.Sound(path.join(snd_dir, 'star.wav'))
fall_sound=pygame.mixer.Sound(path.join(snd_dir, 'fall.wav'))
no_sound=pygame.mixer.Sound(path.join(snd_dir, 'no sound.wav'))
cross_sound=pygame.mixer.Sound(path.join(snd_dir, 'blue.wav'))

#музыка
pygame.mixer.music.load(path.join(snd_dir, 'regression_cyclone_0.ogg'))
#pygame.mixer.music.load(path.join(snd_dir, 'Music.mp3'))
#pygame.mixer.music.load(path.join(snd_dir, 'musci.mp3'))

volume = 0.8
pygame.mixer.music.set_volume(volume)
