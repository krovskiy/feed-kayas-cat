import pygame
from scripts.rendering import shopButton, shopWindow, lockedImg

class Shop(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(shopWindow).convert_alpha()
        self.image = pygame.transform.smoothscale_by(self.image, (0.5,0.5))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class ShopButton(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = shopButton
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

class ShopItem:
    def __init__(self, x, y, width, height, action, scoreboard=None, unlocked=False):
        self.rect = pygame.Rect(x, y, width, height)
        self.action = action 
        self.scoreboard = scoreboard
        self.unlocked = unlocked
        global OwnedDictionary

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def trigger(self):
        if self.scoreboard:
            self.action(self.scoreboard)
        else:
            self.action()

    def unlock_item(self):
        self.unlocked = True

    def show_locked_status(self, screen):
        if not self.unlocked:
            screen.blit(lockedImg, (self.rect.x, self.rect.y))