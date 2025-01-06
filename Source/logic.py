import random

import pygame

from pygame import Surface
from player import Player
from asteroid import Asteroid
from lib import *
from settings import *


class Game:
    def __init__(self, screen: Surface):
        self.background = pygame.transform.scale(pygame.image.load(background).convert(), (WIDTH, HEIGHT))
        self.screen = screen
        self.global_sprites = pygame.sprite.Group()
        self.player = Player((self.screen.get_width()/2, self.screen.get_height()/2), self.screen)
        self.global_sprites.add(self.player)

        self.spawn_cooldown = random.randint(MIN_ASTEROID_CD, MAX_ASTEROID_CD)
        self.canSpawn = True

    def run(self):

        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.player.image, self.player.rect)

        self.global_sprites.add(self.player.bullets)

        if self.canSpawn:
            mew_asteroid = Asteroid(self.screen)
            self.global_sprites.add(mew_asteroid)
            self.canSpawn = False
            self.spawn_cooldown = random.randint(MIN_ASTEROID_CD, MAX_ASTEROID_CD)

        self.global_sprites.draw(self.screen)
        self.global_sprites.update()

        self.timer_spawn_asteroids()


    def timer_spawn_asteroids(self):
        if self.spawn_cooldown > 0:
            self.spawn_cooldown -= 1
        else:
            self.canSpawn = True