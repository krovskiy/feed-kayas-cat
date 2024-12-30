import pygame
from scripts.rendering import images, imageOpenMouth, catShape, catColor

INITIAL_PAUSE_DURATION = 9000
animation_steps = 4
animation_cooldown = 100 
last_update = pygame.time.get_ticks()
current_frame = 0
initial_pause = True
DARK_VIOLET = (255, 255, 255)
numberOfPresses = 0


class kayaCat(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = images
        self.current_image = 0
        self.image = self.images[self.current_image]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.is_fed = False

    def update(self, dragging=False):
        global last_update, initial_pause
        now = pygame.time.get_ticks()
        if dragging:
            self.image = imageOpenMouth
            return
        if initial_pause:
            self.image = self.images[0]
            if now - last_update < INITIAL_PAUSE_DURATION:
                return
            else:
                initial_pause = False
                last_update = now
        if now - last_update > animation_cooldown:
            last_update = now
            self.current_image = (self.current_image + 1) % animation_steps
            self.image = self.images[self.current_image]
            if self.current_image == 0:
                initial_pause = True

class kayaShapeCat(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = catShape
        self.current_image = 0
        self.image = catShape[self.current_image]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.dragging = False

class kayaColorCat(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = catColor
        self.current_image = 0
        self.image = catColor[self.current_image]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.dragging = False