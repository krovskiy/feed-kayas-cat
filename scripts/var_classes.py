from scripts.kayacat import *
from scripts.food import *
from scripts.shop import *
from scripts.secretsound import *
from scripts.scoreboard import *
from scripts.title import *
from scripts.rendering import screen

kayaC = kayaCat(50, 200)
food = Food(235, 135)
gametitle = Title(440, 690)
kayaShape = kayaShapeCat(50, 200)
shopClassWindow = Shop(50, 100) 
shopButtonWindow = ShopButton(50, 650)
musicNote = Soundinitz(500,0)
kayaCColors = kayaColorCat(50, 200)
scoreboard = Scoreboard(screen)

all_sprites = pygame.sprite.Group()
all_sprites.add(kayaCColors)
all_sprites.add(kayaShape)
all_sprites.add(kayaC)
all_sprites.add(gametitle)
all_sprites.add(shopButtonWindow)
all_sprites.add(food)
all_sprites.add(musicNote)