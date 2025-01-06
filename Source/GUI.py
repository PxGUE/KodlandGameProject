import pygame
from pygame import Surface, Vector2
from lib import *

class Button:
    def __init__(self, image, pos:Vector2, text:str,
                 screen : Surface, base_color, hover_color, font=UI_FONT, font_size=18):

        self.image = image
        self.pos = pos
        self.text = text
        self.screen = screen
        self.font = pygame.font.SysFont(font, font_size)
        self.base_color, self.hover_color = base_color, hover_color
        self.btn_text = self.font.render(self.text, True, self.base_color)
        self.rect = self.image.get_rect(center=(self.pos.x, self.pos.y))
        self.rect_text = self.btn_text.get_rect(center=(self.pos.x, self.pos.y))


    def update(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.btn_text, self.rect_text)

    def check_input(self, position)->bool:
       if self.rect.collidepoint(position):
           print("Click")
           return True
       else:
           return False
