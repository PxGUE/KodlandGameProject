import math

import pygame
from pygame.math import Vector2
from pygame import Surface
from settings import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, screen : Surface, angle: float):
        super().__init__()
        self.image = pygame.Surface((10,10))
        self.image.fill('white')
        self.rect = self.image.get_rect(center = (x, y))
        self.speed = BULLET_SPEED
        self.x = x
        self.y = y
        self.screen = screen
        self.angle = angle
        self.velocity_x = math.cos(self.angle * (2*math.pi/360)) * self.speed
        self.velocity_y = math.sin(self.angle * (2*math.pi/360)) * self.speed

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def destroy(self):
        if self.rect.y <= -50 or self.rect.y >= self.screen.get_height() + 50:
            self.kill()

    def update(self):
        self.move()
        self.destroy()