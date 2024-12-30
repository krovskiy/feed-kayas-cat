import pygame
from scripts.rendering import fish_image

class Food(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = fish_image
        self.current_image = 0
        self.image = fish_image[self.current_image]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.dragging = False

    def update(self):
        if self.dragging:
            self.rect.center = pygame.mouse.get_pos()

    def reset_position(self, initial_pos):
        self.rect.topleft = initial_pos