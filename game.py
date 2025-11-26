import pygame
from settings import *
from player import Player
from castle import Castle
from spike import Spike
from ui import UI

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_state = "PLAYING"

        self.ui = UI()

        self.all_sprites = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.player = None
        self.castle = None

        self.start_new_game()

    def start_new_game(self):
        self.game_state = "PLAYING"
        self.all_sprites.empty()
        self.obstacles.empty()

        self.player = Player(50, GROUND_LEVEL)
        self.castle = Castle(700, GROUND_LEVEL)

        self.create_spikes([300, 450, 500])

        self.all_sprites.add(self.player)
        self.all_sprites.add(self.castle)

    def create_spikes(self, x_positions):
        for x in x_positions:
            spike = Spike(x, GROUND_LEVEL)
            self.obstacles.add(spike)
            self.all_sprites.add(spike)

    def check_collisions(self):
        if self.game_state != "PLAYING":
            return

        if pygame.sprite.spritecollide(self.player, self.obstacles, False):
            self.game_state = "GAME_OVER"

        if pygame.sprite.collide_rect(self.player, self.castle):
            self.game_state = "VICTORY"

    def update(self):
        if self.game_state == "PLAYING":
            self.all_sprites.update()
            self.check_collisions()

    def draw(self):
        self.window.fill(SKY_BLUE)
        pygame.draw.rect(self.window, GROUND_COLOR, (0, GROUND_LEVEL, WIDTH, HEIGHT - GROUND_LEVEL))

        self.all_sprites.draw(self.window)

        if self.game_state == "VICTORY":
            self.ui.draw_victory(self.window)
        elif self.game_state == "GAME_OVER":
            self.ui.draw_game_over(self.window)

        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and self.game_state != "PLAYING":
                    self.start_new_game()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()