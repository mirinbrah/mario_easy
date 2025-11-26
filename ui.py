import pygame

from settings import WIDTH, HEIGHT

class UI:
    def __init__(self):
        self.title_font = pygame.font.Font(None, 60)
        self.info_font = pygame.font.Font(None, 30)

    def draw_victory(self, surface):
        text = self.title_font.render("ПОБЕДА!", True, (255, 215, 0))
        rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        surface.blit(text, rect)
        self.draw_restart_hint(surface)

    def draw_game_over(self, surface):
        text = self.title_font.render("ОЙ! ШИПЫ!", True, (220, 20, 60))
        rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        surface.blit(text, rect)
        self.draw_restart_hint(surface)

    def draw_restart_hint(self, surface):
        text = self.info_font.render("Нажми R для рестарта", True, (255, 255, 255))
        rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        surface.blit(text, rect)
