import math
import pygame
from pygame import Surface, Vector2
from settings import *
from lib import BULLET_IMAGE


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, screen : Surface, angle: float):
        super().__init__()
        self.x = x
        self.y = y
        self.screen = screen
        self.angle = angle
        self.image = pygame.transform.rotozoom(pygame.image.load(BULLET_IMAGE).convert_alpha(), -self.angle, 0.5)
        self.original = self.image
        self.rect = self.image.get_rect(center=(x, y))
        self.hit_mask = pygame.mask.from_surface(self.image)
        self.speed = BULLET_SPEED
        self.velocity_x = math.cos(self.angle * (2*math.pi/360)) * self.speed
        self.velocity_y = math.sin(self.angle * (2*math.pi/360)) * self.speed

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

        self.rect.centerx = int(self.x)
        self.rect.centery = int(self.y)

    def destroy(self):
        if (self.rect.left <= 0 or
            self.rect.left >= self.screen.get_width() or
            self.rect.top >= self.screen.get_height() or
            self.rect.bottom <= 0):

            self.kill()

    def update(self):
        self.move()
        self.destroy()