import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(RED)
        pygame.draw.circle(self.image, WHITE, (10, 10), 5)
        pygame.draw.circle(self.image, WHITE, (30, 10), 5)
        pygame.draw.circle(self.image, BLACK, (10, 10), 2)
        pygame.draw.circle(self.image, BLACK, (30, 10), 2)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y

        self.vel_y = 0
        self.on_ground = False
        self.start_pos = (x, y)

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= MOVE_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += MOVE_SPEED

        if keys[pygame.K_SPACE] and self.on_ground:
            self.jump()

    def jump(self):
        self.vel_y = JUMP_FORCE
        self.on_ground = False

    def apply_gravity(self):
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

    def check_collisions(self):
        if self.rect.bottom >= GROUND_LEVEL:
            self.rect.bottom = GROUND_LEVEL
            self.vel_y = 0
            self.on_ground = True

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def update(self):
        self.get_input()
        self.apply_gravity()
        self.check_collisions()