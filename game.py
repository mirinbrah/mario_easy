import pygame

from settings import *
from player import Player

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 48)
        self.play = True

        self.all_sprites = pygame.sprite.Group()
        self.player = Player(50, GROUND_LEVEL)
        self.all_sprites.add(self.player)

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.window.fill(SKY_BLUE)
        pygame.draw.rect(self.window, GROUND_COLOR, (0, GROUND_LEVEL, WIDTH, HEIGHT - GROUND_LEVEL))
        self.all_sprites.draw(self.window)
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.play = False

    def run(self):
        while self.play:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()


