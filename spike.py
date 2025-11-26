import pygame
from settings import *

class Spike(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, BLACK, [(0, 40), (20, 0), (40, 40)])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y