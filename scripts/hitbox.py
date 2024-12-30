import pygame

class hitbox:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
    def draw(self, screen, color=(255, 0, 0)):
        pygame.draw.rect(screen, color, self.rect)