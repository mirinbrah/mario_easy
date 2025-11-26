import pygame
from settings import *

class Castle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((100, 120), pygame.SRCALPHA)
        pygame.draw.rect(self.image, CASTLE_COLOR, (10, 40, 80, 80))
        pygame.draw.rect(self.image, CASTLE_COLOR, (0, 20, 20, 100))
        pygame.draw.rect(self.image, CASTLE_COLOR, (80, 20, 20, 100))
        pygame.draw.polygon(self.image, RED, [(0, 20), (10, 0), (20, 20)])
        pygame.draw.polygon(self.image, RED, [(80, 20), (90, 0), (100, 20)])
        pygame.draw.rect(self.image, (100, 50, 0), (35, 80, 30, 40))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y