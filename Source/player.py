import pygame
from pygame import Surface, Vector2, Rect
from bullet import Bullet
from lib import *
from settings import *

import math

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, screen : Surface):
        super().__init__()
        self.image = pygame.transform.rotozoom((pygame.image.load(playerShipBase).convert_alpha()),-90, PLAYER_SCALE)
        self.pos = Vector2(pos[0], pos[1])
        self.velocity = Vector2(0, 0)
        self.base_image = self.image
        self.hit_box = self.image.get_rect(center = pos)
        self.hit_mask = pygame.mask.from_surface(self.image)
        self.rect = self.hit_box.copy()
        self.speed = PLAYER_SPEED
        self.angle = 0
        self.screen = screen
        self.canShoot = True
        self.shootTime = 0
        self.shoot_cooldown = SHOOT_COOLDOWN
        self.weapon_offset = Vector2(0,0)
        self.bullets = pygame.sprite.Group()

    def player_rotation(self):
        mouse_pos = pygame.mouse.get_pos()
        pos_x = mouse_pos[0] - self.hit_box.centerx
        pos_y = mouse_pos[1] - self.hit_box.centery
        self.angle = math.degrees(math.atan2(pos_y, pos_x))
        self.image = pygame.transform.rotate(self.base_image, -self.angle)
        self.rect = self.image.get_rect(center=self.hit_box.center)

    def get_input(self):
        # movement
        keys = pygame.key.get_pressed()

        self.velocity = Vector2(0, 0)

        if keys[pygame.K_w]:
            self.velocity.y -= 1
        if keys[pygame.K_s]:
            self.velocity.y += 1
        if keys[pygame.K_a]:
            self.velocity.x -= 1
        if keys[pygame.K_d]:
            self.velocity.x += 1

        if  self.velocity.length() > 0:
            self.velocity = self.velocity.normalize() * self.speed

        mouse_keys = pygame.mouse.get_pressed()

        if mouse_keys[0] == True and self.canShoot:
            self.canShoot = False
            self.shoot()
            self.shootTime = pygame.time.get_ticks()

    def player_movement(self):
        self.hit_box.move_ip(self.velocity)

        if self.hit_box.left < 0:
            self.hit_box.left = 0

        if self.hit_box.right > self.screen.get_width():
            self.hit_box.right = self.screen.get_width()

        if self.hit_box.top < 0:
            self.hit_box.top = 0

        if self.hit_box.bottom > self.screen.get_height():
            self.hit_box.bottom = self.screen.get_height()

        self.rect.center = self.hit_box.center

    def timer_shoot(self):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        else:
            self.canShoot = True

    def shoot(self):
        bullet_pos = self.rect.center + self.weapon_offset.rotate(self.angle)
        bullet = Bullet(bullet_pos[0], bullet_pos[1], self.screen, self.angle)
        self.bullets.add(bullet)
        self.shoot_cooldown = SHOOT_COOLDOWN

    def update(self):
        self.get_input()
        self.player_movement()
        self.player_rotation()
        self.timer_shoot()
        self.bullets.update()



