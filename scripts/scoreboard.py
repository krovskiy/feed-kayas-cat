import pygame

class Scoreboard:
    def __init__(self, screen, x=40, y=20, font_size=30, color=(0, 0, 0)):
        self.screen = screen
        self.x = x
        self.y = y
        self.font_size = font_size
        self.color = color
        self.score = 0
        self.font = pygame.font.SysFont('nicesugar', self.font_size)
        self.render_score()

    def render_score(self):
        self.score_image = self.font.render(f'meowny: {self.score}', True, self.color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.topleft = (self.x, self.y)

    def update_score(self, points):
        self.score += points
        self.render_score()

    def draw(self):
        self.screen.blit(self.score_image, self.score_rect)
