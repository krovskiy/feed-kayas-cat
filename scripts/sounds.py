import pygame
from scripts.constants import *

pygame.mixer.init()
pygame.mixer.music.load(kayamusic_path)
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1)

nomnom = pygame.mixer.Sound(nom_sound_path)
nomnom.set_volume(0.8)

miau = pygame.mixer.Sound(miau_sound_path)

titleSound = pygame.mixer.Sound(tbell_sound_path)

soundoff = pygame.mixer.Sound(soundoff_path)
soundoff.set_volume(0.4)

click = pygame.mixer.Sound(click_sound_path)
click.set_volume(0.8)

tryagain = pygame.mixer.Sound(tryagain_path)
tryagain.set_volume(0.8)