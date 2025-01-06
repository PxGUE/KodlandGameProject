import math
import random

import pygame
from pygame import Surface, Vector2
from lib import *
from settings import *

class Asteroid(pygame.sprite.Sprite):
    """Clase base del asteroide"""
    def __init__(self, screen : Surface):
        super().__init__()
        self.screen = screen
        #sprites
        asteroid_image_01 = pygame.transform.rotozoom(pygame.image.load(ASTEROID_1).convert_alpha(), 0, random.uniform(MIN_ASTEROID_SIZE, MAX_ASTEROID_SIZE))
        asteroid_image_02 = pygame.transform.rotozoom(pygame.image.load(ASTEROID_2).convert_alpha(), 0, random.uniform(MIN_ASTEROID_SIZE, MAX_ASTEROID_SIZE))
        self. asteroids = [asteroid_image_01, asteroid_image_02]
        self.image :Surface= random.choice(self.asteroids) #se selecciona uno aleatorio
        self.rect = self.image.get_rect()
        self.hit_mask = pygame.mask.from_surface(self.image)
        self.velocity = random.randint(MIN_ASTEROID_SPEED,MAX_ASTEROID_SPEED)
        self.side = self.get_initial_side()
        self.direction = self.get_initial_direction(self.side)
        self.inital_location = self.get_random_location(self.side)
        self.rect.center = (int(self.inital_location.y), int(self.inital_location.x))

    def get_initial_side(self) -> str:
        """Lado inicial de la pantalla arriba, abajo o a los lados"""
        side : str = random.choice(['top', 'bottom', 'left', 'right'])
        return side

    def get_random_location(self, side):
        """
        se obtiene una posicion aleatoria del lado de la pantalla:
        ejemplo: 'top' es calquier posicion en x desde 0 hasta el ancho de la pantalla
        """
        location = Vector2(0, 0)

        offset = self.rect.width // 2

        if side == 'top':
            location.x = random.randint(offset, WIDTH-offset)
            location.y = HEIGHT + offset
        elif side == 'bottom':
            location.x = random.randint(offset, WIDTH-offset)
            location.y = -offset
        elif side == 'left':
            location.x = -offset
            location.y = random.randint(offset, HEIGHT-offset)
        elif side == 'right':
            location.x = WIDTH + offset
            location.y = random.randint(offset, HEIGHT-offset)

        return  location

    def get_initial_direction(self, side):
        """Se obtiene un angulo aleatorio al que apuntara el asteroide"""
        direction = 0

        if side == 'top':
             direction = random.uniform(math.pi, math.pi * 1.5)
        elif side == 'bottom':
             direction = random.uniform(math.pi * 0.5, math.pi)
        elif side == 'left':
            direction = random.uniform(math.pi * 0.75, math.pi * 1.25)
        elif side == 'right':
            direction = random.uniform(-math.pi * 0.25, math.pi * 0.25)

        return  direction

    def move(self):
        self.rect.centerx += math.cos(self.direction) * self.velocity
        self.rect.centery += math.sin(self.direction) * self.velocity

        #Correccion del angulo para evitar que el asteroide apunte fuera de la pantalla inicialmente.
        if self.rect.centerx < 0:
            self.rect.centerx = WIDTH
            self.direction = random.uniform(math.pi * 0.75, math.pi * 1.25)
        elif self.rect.centerx > WIDTH:
            self.rect.centerx = 0
            self.direction = random.uniform(-math.pi * 0.25, math.pi * 0.25)
        if self.rect.centery < 0:
            self.rect.centery = HEIGHT
            self.direction = random.uniform(math.pi, math.pi * 1.5)
        elif self.rect.centery > HEIGHT:
            self.rect.centery = 0
            self.direction = random.uniform(math.pi * 0.5, math.pi)

    def update(self):
        self.move()
        self.destroy()

    def destroy(self):
        if self.rect.centerx < 0 or self.rect.centerx > WIDTH or \
           self.rect.centery < 0 or self.rect.centery > HEIGHT:
            self.kill()
