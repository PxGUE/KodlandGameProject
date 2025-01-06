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
        self.bullet_group = pygame.sprite.Group()
        self.asteroid_group = pygame.sprite.Group()
        self.player = Player((self.screen.get_width()/2, self.screen.get_height()/2), self.screen)
        self.player_group = pygame.sprite.GroupSingle()
        self.player_group.add(self.player)
        self.global_sprites.add(self.player)
        self.spawn_cooldown = random.randint(MIN_ASTEROID_CD, MAX_ASTEROID_CD)
        self.canSpawn = True
        self.score = 0
        self.font = pygame.font.SysFont(UI_FONT, 25)
        self.playerKill = False
        self.pk_sound = pygame.mixer.Sound(PLAYER_SOUND)
        self.a_sound = pygame.mixer.Sound(STEROID_SOUND)
        self.bg_sound = pygame.mixer.Sound(GAME_SOUND)
        pygame.mixer.Sound.play(self.bg_sound)

    def run(self):

        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.player.image, self.player.rect)

        self.global_sprites.add(self.player.bullets)
        self.bullet_group.add(self.player.bullets)

        if self.canSpawn:
            mew_asteroid = Asteroid(self.screen)
            self.global_sprites.add(mew_asteroid)
            self.asteroid_group.add(mew_asteroid)
            self.canSpawn = False
            self.spawn_cooldown = random.randint(MIN_ASTEROID_CD, MAX_ASTEROID_CD)

        self.global_sprites.draw(self.screen)
        self.global_sprites.update()

        player_hit = pygame.sprite.spritecollide(self.player_group.sprite, self.asteroid_group, False, pygame.sprite.collide_mask)
        for hit in player_hit:
            player_hit.remove(hit)
            hit.kill()
            pygame.mixer.Sound.play(self.pk_sound)
            self.playerKill = True
            self.bg_sound.stop()
            print("PLAYER HIT")

        for bullet in self.bullet_group:
            bullet_hit = pygame.sprite.spritecollide(bullet, self.asteroid_group, False, pygame.sprite.collide_mask)
            for hit in bullet_hit:
                pygame.mixer.Sound.play(self.a_sound)
                self.score += 1
                bullet_hit.remove(hit)
                hit.kill()
                bullet.kill()

        self.timer_spawn_asteroids()
        self.score_gui()


    def timer_spawn_asteroids(self):
        if self.spawn_cooldown > 0:
            self.spawn_cooldown -= 1
        else:
            self.canSpawn = True

    def score_gui(self):
        text = self.font.render("Puntaje: " + str(self.score), True, 'white')
        self.screen.blit(text, (0,0))


    def check_game_over(self):
        return self.playerKill