import pygame
from scripts.constants import *
from scripts.dictionary_path import *

pygame.init()
WIDTH, HEIGHT = 600, 800
BG_COLOR = (255, 255, 255)
background = pygame.image.load(background)
background = pygame.transform.smoothscale_by(background, (1,1))
programIcon = pygame.image.load(icon_path)
pygame.display.set_icon(programIcon)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("feed kaya's cat")


images = [pygame.image.load(img_path) for img_path in eyes_animation]
images = [pygame.transform.smoothscale_by(img, (0.5,0.5)) for img in images]

imageOpenMouth = pygame.image.load(kayacatopenmouth_path).convert_alpha()
imageOpenMouth = pygame.transform.smoothscale_by(imageOpenMouth, (0.5,0.5))

catShape = [pygame.image.load(kayaShapesCatPath).convert_alpha() for kayaShapesCatPath in kayaShapesCat]
catShape = [pygame.transform.smoothscale_by(kayaShapesCatPathTransform, (0.5,0.5)) for kayaShapesCatPathTransform in catShape]

catColor = [pygame.image.load(kayaCatColorsPath).convert_alpha() for kayaCatColorsPath in kayacatColors]
catColor = [pygame.transform.smoothscale_by((kayaCatColorsTransform),(0.5,0.5)) for kayaCatColorsTransform in catColor]

titleImage = [pygame.image.load(titleImages).convert_alpha() for titleImages in title_image_list_path]
titleImage = [pygame.transform.smoothscale_by(titleImagesTransform, (0.3,0.3)) for titleImagesTransform in titleImage]

musicNoteImage = [pygame.image.load(musicNote).convert_alpha() for musicNote in musicNoteImages]
musicNoteImage = [pygame.transform.smoothscale_by(musicNoteTransform, (0.1, 0.1))for musicNoteTransform in musicNoteImage]

fish_image = [pygame.image.load(FishPaths).convert_alpha() for FishPaths in fishes]
fish_image = [pygame.transform.smoothscale_by(fishPathsTransform, (0.35,0.35)) for fishPathsTransform in fish_image]
 
meownies = pygame.image.load(meownies).convert_alpha()

meownies = pygame.transform.smoothscale_by(meownies, (0.03,0.03))

shopButtonClicked = pygame.image.load(shopButtonClicked).convert_alpha()

shopButtonClicked = pygame.transform.smoothscale_by(shopButtonClicked, (0.3,0.3))

shopButton = pygame.image.load(shopButton).convert_alpha()

shopButton = pygame.transform.smoothscale_by(shopButton, (0.3,0.3))

lockedImg = pygame.image.load(lockedImg).convert_alpha()

lockedImg = pygame.transform.smoothscale_by(lockedImg, (0.1,0.1))

font = pygame.font.SysFont('nicesugar', 30)
font2 = pygame.font.SysFont('nicesugar', 30)