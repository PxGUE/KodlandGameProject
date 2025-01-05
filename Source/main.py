import pygame, sys

from logic import Game
from settings import *

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def main_game():
    pygame.display.set_caption("Kodland Project: Game")
    game = Game(SCREEN)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        game.run()
        pygame.display.update()
        clock.tick(60)

def main_menu():
    pygame.display.set_caption("Kodland Project: Main menu")
    SCREEN.fill((0,0,0))
    while True:
        mouse_pos = pygame.mouse.get_pos()


if __name__ == '__main__':
    pygame.init()
    main_game()

