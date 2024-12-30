import pygame

from scripts.rendering import musicNoteImage

class Soundinitz(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.music_current_image = 0
        self.image = musicNoteImage[self.music_current_image]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)