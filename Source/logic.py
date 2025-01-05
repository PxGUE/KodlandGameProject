import pygame

from pygame import Surface
from player import Player
from lib import *
from settings import *

class Game:
    def __init__(self, screen: Surface):
        self.background = pygame.transform.scale(pygame.image.load(background).convert(), (WIDTH, HEIGHT))
        self.screen = screen
        self.global_sprites = pygame.sprite.Group()
        self.player = Player((self.screen.get_width()/2, self.screen.get_height()/2), self.screen)
        self.global_sprites.add(self.player)

    def run(self):
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.player.image, self.player.rect)
        self.global_sprites.add(self.player.bullets)

        self.global_sprites.draw(self.screen)
        self.global_sprites.update()



