import pygame
import time
import sys
pygame.init()

from moduls.config import *
from moduls.name import get_player_name
from moduls.new_game import start_new_game
from moduls.results import show_results,bubble_sort,test_bubble_sort
from moduls.the_same import are_the_same,test_are_the_same

def main_game_loop(screen, font, gameWidht, gameHeight, running, player_name, restart_button_rect1, restart_button_rect2):
    pictures_name, pictures, pictures_rectangle, hidden = start_new_game(picture_size_Widht,picture_size_Height,margin_left,margin_top,padding,columns)
    selection1 = None
    selection2 = None
    game_completed = False
    results = {}
    waiting_for_restart = False
    start_time = time.time()

    running = True
    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for item in pictures_rectangle:
                    if item.collidepoint(
                            event.pos):
                        if hidden[pictures_rectangle.index(item)] != True:
                            if selection1 is not None:
                                selection2 = pictures_rectangle.index(item)
                                hidden[selection2] = True
                            else:
                                selection1 = pictures_rectangle.index(item)
                                hidden[selection1] = True

        for i in range(len(pictures_name)):
            if hidden[i] is True:
                screen.blit(pictures[i], pictures_rectangle[i])
            else:

                pygame.draw.rect(screen, WHITE, (
                    pictures_rectangle[i][0], pictures_rectangle[i][1], picture_size_Widht, picture_size_Height))
        pygame.display.update()


        if selection1 is not None and selection2 is not None:
            if are_the_same(pictures_name[selection1], pictures_name[selection2]):
                selection1, selection2 = None, None
                pygame.time.wait(500)
            else:
                pygame.time.wait(700)
                hidden[selection1] = False
                hidden[selection2] = False
                selection1, selection2 = None, None

            win = all(hidden)
            if win:
                end_time = time.time()
                game_completed = True

                elapsed_time = end_time - start_time
                results[player_name] = elapsed_time
                restart_button_rect1, restart_button_rect2 = show_results(screen, font, gameWidht, gameHeight, results,BACKGROUND_COLOR,DEEPPINK_COLOR,BLACK)

                waiting_for_restart = True
                while waiting_for_restart:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            waiting_for_restart = False
                        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            if restart_button_rect1.collidepoint(event.pos):
                                screen.fill(BACKGROUND_COLOR)
                                player_name = get_player_name(font, gameWidht, gameHeight, screen, DEEPPINK_COLOR, BACKGROUND_COLOR)
                                screen.fill(BACKGROUND_COLOR)
                                pictures_name, pictures, pictures_rectangle, hidden = start_new_game(picture_size_Widht,picture_size_Height,margin_left,margin_top,padding,columns)
                                start_time = time.time()
                                game_completed = False
                                waiting_for_restart = False
                                pygame.display.flip()
                            elif restart_button_rect2.collidepoint(event.pos):
                                pygame.quit()
                                sys.exit()
                    pygame.display.flip()

player_name = get_player_name(font, gameWidht, gameHeight, screen, DEEPPINK_COLOR, BACKGROUND_COLOR)

pictures_name, pictures, pictures_rectangle, hidden = start_new_game(picture_size_Widht,picture_size_Height,margin_left,margin_top,padding,columns)

main_game_loop(screen, font, gameWidht, gameHeight, running, player_name, restart_button_rect1, restart_button_rect2)

if game_completed:
    pictures_name, pictures, pictures_rectangle, hidden = start_new_game(picture_size_Widht,picture_size_Height,margin_left,margin_top,padding,columns)
