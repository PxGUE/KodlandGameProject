from idlelib.autocomplete import TRY_A

import pygame, sys
from pygame.math import Vector2
from logic import Game
from settings import *
from GUI import Button
from lib import *


SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

BTN_IMAGE = pygame.image.load(BUTTON_BACKGROUND).convert_alpha()
BACKGROUND_PAUSE = pygame.transform.scale(pygame.image.load(background).convert(), (WIDTH, HEIGHT))

def game_over():
    pygame.display.set_caption("Kodland Project: Game over")

    btn_main_menu = Button(BTN_IMAGE, Vector2(WIDTH / 2, (HEIGHT / 2) - BTN_IMAGE.get_height()), 'MENU', SCREEN,
                           (255, 255, 255), (255, 255, 255), font_size=BTN_FONT_SIZE)

    btn_restart = Button(BTN_IMAGE, Vector2(WIDTH / 2, HEIGHT / 2), 'REINICAR', SCREEN,
                      (255, 255, 255), (255, 255, 255), font_size=BTN_FONT_SIZE)

    btn_quit = Button(BTN_IMAGE, Vector2(WIDTH / 2, (HEIGHT / 2) + BTN_IMAGE.get_height()), 'SALIR', SCREEN,
                      (255, 255, 255), (255, 255, 255), font_size=BTN_FONT_SIZE)
    pause = True
    while pause:

        mouse_pose = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if btn_main_menu.check_input(mouse_pose):
                    main_menu()
                    pause = False
                    return True

                if btn_restart.check_input(mouse_pose):
                    main_game()
                    pause = False
                    return True

                if btn_quit.check_input(mouse_pose):
                    pygame.quit()
                    sys.exit()

        SCREEN.blit(BACKGROUND_PAUSE, (0, 0))

        btn_main_menu.update()
        btn_restart.update()
        btn_quit.update()

        pygame.display.update()
        clock.tick(60)

    return False


def pause_menu() -> bool:
    pygame.display.set_caption("Kodland Project: Pausa")

    btn_main_menu = Button(BTN_IMAGE, Vector2(WIDTH / 2, (HEIGHT / 2) - BTN_IMAGE.get_height()), 'MENU', SCREEN,
                      (255, 255, 255), (255, 255, 255), font_size=BTN_FONT_SIZE)

    btn_back = Button(BTN_IMAGE, Vector2(WIDTH / 2, HEIGHT / 2), 'REGRESAR', SCREEN,
                      (255, 255, 255), (255, 255, 255), font_size=BTN_FONT_SIZE)

    btn_quit = Button(BTN_IMAGE, Vector2(WIDTH / 2, (HEIGHT / 2) + BTN_IMAGE.get_height()), 'SALIR', SCREEN,
                      (255, 255, 255), (255, 255, 255), font_size=BTN_FONT_SIZE)
    pause = True
    while pause:

        mouse_pose = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if btn_main_menu.check_input(mouse_pose):
                    main_menu()
                    pause = False
                    return True

                if btn_back.check_input(mouse_pose):
                    pause = False

                if btn_quit.check_input(mouse_pose):
                    pygame.quit()
                    sys.exit()

        SCREEN.blit(BACKGROUND_PAUSE, (0, 0))

        btn_main_menu.update()
        btn_back.update()
        btn_quit.update()

        pygame.display.update()
        clock.tick(60)

    return False

def main_game():
    pygame.display.set_caption("Kodland Project")
    game = Game(SCREEN)

    play = True
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if pause_menu():
                        play = False

        game.run()

        if game.check_game_over():
            if game_over():
                play = False

        pygame.display.update()
        clock.tick(60)

def main_menu():

    pygame.display.set_caption("Kodland Project: Menu Principal")
    btn_play = Button(BTN_IMAGE, Vector2(WIDTH / 2, (HEIGHT / 2) - BTN_IMAGE.get_height()), 'JUGAR', SCREEN,
                      (255,255,255), (255,255,255), font_size=BTN_FONT_SIZE)
    btn_options = Button(BTN_IMAGE, Vector2(WIDTH / 2, HEIGHT / 2), 'OPCIONES', SCREEN, (255,255,255),
                         (255,255,255), font_size=BTN_FONT_SIZE)
    btn_quit = Button(BTN_IMAGE, Vector2(WIDTH / 2, (HEIGHT / 2) + BTN_IMAGE.get_height()), 'SALIR', SCREEN,
                      (255,255,255), (255,255,255), font_size=BTN_FONT_SIZE)

    menu = True
    while menu:

        mouse_pose = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_play.check_input(mouse_pose):
                    main_game()
                    menu = False
                if btn_options.check_input(mouse_pose):
                    pass
                if btn_quit.check_input(mouse_pose):
                    pygame.quit()
                    sys.exit()

        SCREEN.fill((0, 0, 0))

        btn_play.update()
        btn_options.update()
        btn_quit.update()

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    pygame.init()
    main_menu()

