import pygame
from scripts.rendering import titleImage
from scripts.sounds import titleSound

class Title(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = titleImage
        self.title_curent_image = 0
        self.image = self.image[self.title_curent_image]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def trigger(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def play_sound(self):
        if titleSound.play():
            titleSound.stop()
        titleSound.play()
    
    def updatetitle(self, numberOfPresses):
        if numberOfPresses >= 5:
            self.image = titleImage[1]
            print(numberOfPresses)