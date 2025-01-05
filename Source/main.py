import pygame, sys
from logic import Game
from settings import *

if __name__ == '__main__':
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    game = Game(SCREEN)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        game.run()

        pygame.display.update()
        clock.tick(60)