import pygame as pg
import sys
from board import Board


pg.init()

WIDTH = 603
HEIGHT = 603


def start_screen(screen):
    screen.fill((254, 240, 255))

    welcome_font = pg.font.Font(None, 80)
    game_mode_font = pg.font.Font(None, 65)
    difficulty_font = pg.font.Font(None, 50)
    rules_font = pg.font.Font(None, 30)

    easy_message = difficulty_font.render('EASY', True, (254, 240, 255))
    medium_message = difficulty_font.render('MEDIUM', True, (254, 240, 255))
    hard_message = difficulty_font.render('HARD', True, (254, 240, 255))

    welcome_message = welcome_font.render('Welcome to Sudoku', True, (0, 13, 51))
    welcome_message_rect = welcome_message.get_rect(center=(WIDTH // 2, 50))
    screen.blit(welcome_message, welcome_message_rect)

    rules_message = difficulty_font.render('Rules:', True, (0, 13, 51))
    rules_message_rect = rules_message.get_rect(center=(WIDTH // 2, 150))
    screen.blit(rules_message, rules_message_rect)

    rules_text_message1 = rules_font.render('In Sudoku, a 9x9 grid is divided into nine 3x3 sub-grids.', True, (0, 13, 51))
    rules_text_message1_rect = rules_text_message1.get_rect(center=(WIDTH // 2, 195))
    screen.blit(rules_text_message1, rules_text_message1_rect)

    rules_text_message2 = rules_font.render('The objective is to fill in each row, column, and subgrid', True,(0, 13, 51))
    rules_text_message2_rect = rules_text_message2.get_rect(center=(WIDTH // 2, 225))
    screen.blit(rules_text_message2, rules_text_message2_rect)

    rules_text_message3 = rules_font.render('with the numbers 1 through 9, ensuring that no repetition', True,(0, 13, 51))
    rules_text_message3_rect = rules_text_message3.get_rect(center=(WIDTH // 2, 255))
    screen.blit(rules_text_message3, rules_text_message3_rect)

    rules_text_message4 = rules_font.render('occurs in any row, column, or subgrid.A valid solution', True,(0, 13, 51))
    rules_text_message4_rect = rules_text_message4.get_rect(center=(WIDTH // 2, 285))
    screen.blit(rules_text_message4, rules_text_message4_rect)

    rules_text_message5 = rules_font.render('must meet these conditions for every row, column,', True,(0, 13, 51))
    rules_text_message5_rect = rules_text_message5.get_rect(center=(WIDTH // 2, 315))
    screen.blit(rules_text_message5, rules_text_message5_rect)

    rules_text_message6 = rules_font.render('and 3x3 subgrid.', True,(0, 13, 51))
    rules_text_message6_rect = rules_text_message6.get_rect(center=(WIDTH // 2, 345))
    screen.blit(rules_text_message6, rules_text_message6_rect)

    game_mode_message = game_mode_font.render('Difficulty:', True, (0, 13, 51))
    game_mode_rect = game_mode_message.get_rect(center=(WIDTH // 2, HEIGHT - 100))
    screen.blit(game_mode_message, game_mode_rect)

    easy_button_surface = pg.Surface((easy_message.get_size()[0] + 20, easy_message.get_size()[1] + 20))
    easy_button_surface.fill((0, 13, 51))
    easy_button_surface.blit(easy_message, (10, 10))

    medium_button_surface = pg.Surface((medium_message.get_size()[0] + 20, medium_message.get_size()[1] + 20))
    medium_button_surface.fill((0, 13, 51))
    medium_button_surface.blit(medium_message, (10, 10))

    hard_button_surface = pg.Surface((hard_message.get_size()[0] + 20, hard_message.get_size()[1] + 20))
    hard_button_surface.fill((0, 13, 51))
    hard_button_surface.blit(hard_message, (10, 10))

    easy_mode_rect = easy_message.get_rect(center=(WIDTH // 4, HEIGHT - 50))
    screen.blit(easy_button_surface, easy_mode_rect)

    medium_mode_rect = medium_message.get_rect(center=(WIDTH // 2, HEIGHT - 50))
    screen.blit(medium_button_surface, medium_mode_rect)

    hard_mode_rect = hard_message.get_rect(center=(WIDTH * (3 / 4), HEIGHT - 50))
    screen.blit(hard_button_surface, hard_mode_rect)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if easy_mode_rect.collidepoint(event.pos):
                    return 30

                elif medium_mode_rect.collidepoint(event.pos):
                    return 40

                elif hard_mode_rect.collidepoint(event.pos):
                    return 50

        pg.display.update()


def game_won_screen(screen):

    screen = pg.display.set_mode((603, 703))
    screen.fill((254, 240, 255))

    game_won_font = pg.font.Font(None, 100)
    exit_button_font = pg.font.Font(None, 65)

    game_won_message = game_won_font.render('Game Won!', True, (0, 13, 51))
    game_won_rect = game_won_message.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 125))
    screen.blit(game_won_message, game_won_rect)

    exit_button_message = exit_button_font.render('EXIT', True, (254, 240, 255))
    exit_button_rect = exit_button_message.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
    screen.blit(exit_button_message, exit_button_rect)

    exit_button_surface = pg.Surface((exit_button_message.get_size()[0] + 20, exit_button_message.get_size()[1] + 20))
    exit_button_surface.fill((0, 13, 51))
    exit_button_surface.blit(exit_button_message, (10, 10))

    exit_button_rect = exit_button_message.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
    screen.blit(exit_button_surface, exit_button_rect)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if exit_button_rect.collidepoint(event.pos):
                    sys.exit()

        pg.display.update()


def game_over_screen(screen):
    screen.fill((254, 240, 255))

    game_over_font = pg.font.Font(None, 100)
    restart_button_font = pg.font.Font(None, 65)

    game_over_message = game_over_font.render('Game Over :(', True, (0, 13, 51))
    game_over_rect = game_over_message.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 125))
    screen.blit(game_over_message, game_over_rect)

    restart_button_message = restart_button_font.render('RESTART', True, (254, 240, 255))
    restart_button_rect = restart_button_message.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(restart_button_message, restart_button_rect)

    restart_button_surface = pg.Surface((restart_button_message.get_size()[0] + 20, restart_button_message.get_size()[1] + 20))
    restart_button_surface.fill((0, 13, 51))
    restart_button_surface.blit(restart_button_message, (10, 10))

    restart_button_rect = restart_button_message.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(restart_button_surface, restart_button_rect)

    while True:
        for event in pg.event.get():

            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:

                if restart_button_rect.collidepoint(event.pos):
                    main()

        pg.display.update()


def main():
    global x_y_pos, number_to_place
    pg.init()
    pg.display.set_caption("Sudoku")
    screen = pg.display.set_mode((603, 703))
    sudoku_screen = Board(WIDTH, HEIGHT, screen,
                          start_screen(screen))

    game_on = True
    game_won = False
    game_over = False

    while True:

        while game_on and not game_won and not game_over:
            sudoku_screen.draw()

            bottom_game_font = pg.font.Font(None,50)
            reset_message = bottom_game_font.render('RESET', True, (254, 240, 255))
            restart_message = bottom_game_font.render('RESTART', True, (254, 240, 255))
            exit_message = bottom_game_font.render('EXIT', True, (254, 240, 255))

            reset_button_surface = pg.Surface((reset_message.get_size()[0] + 20, reset_message.get_size()[1] + 20))
            reset_button_surface.fill((0, 13, 51))
            reset_button_surface.blit(reset_message, (10, 10))

            restart_button_surface = pg.Surface(
                (restart_message.get_size()[0] + 20, restart_message.get_size()[1] + 20))
            restart_button_surface.fill((0, 13, 51))
            restart_button_surface.blit(restart_message, (10, 10))

            exit_button_surface = pg.Surface((exit_message.get_size()[0] + 20, exit_message.get_size()[1] + 20))
            exit_button_surface.fill((0, 13, 51))
            exit_button_surface.blit(exit_message, (10, 10))

            reset_button_rect = reset_message.get_rect(center=(((WIDTH / 9) * 1.5) - 10, HEIGHT + 40))
            screen.blit(reset_button_surface, reset_button_rect)

            restart_button_rect = restart_message.get_rect(center=((WIDTH / 2) - 10, HEIGHT + 40))
            screen.blit(restart_button_surface, restart_button_rect)

            exit_button_rect = exit_message.get_rect(center=(((WIDTH / 9) * 7) + 10, HEIGHT + 40))
            screen.blit(exit_button_surface, exit_button_rect)

            for event in pg.event.get():

                if event.type == pg.QUIT:
                    game_on = False
                    pg.quit()
                    sys.exit()

                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    row_pos, col_pos = pos[0], pos[1]
                    x_y_pos = sudoku_screen.click(row_pos, col_pos)
                    if row_pos >= 0 and row_pos <= WIDTH and col_pos >= 0 and col_pos <= 600:
                        sudoku_screen.select(x_y_pos[0], x_y_pos[1])

                    if exit_button_rect.collidepoint(event.pos):
                        sys.exit()

                    if reset_button_rect.collidepoint(event.pos):
                        sudoku_screen.reset_to_original()

                    if restart_button_rect.collidepoint(event.pos):
                        main()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_1 or event.key == pg.K_KP1:
                        number_to_place = 1
                        sudoku_screen.sketch(1)

                    if event.key == pg.K_2 or event.key == pg.K_KP2:
                        number_to_place = 2
                        sudoku_screen.sketch(2)

                    if event.key == pg.K_3 or event.key == pg.K_KP3:
                        number_to_place = 3
                        sudoku_screen.sketch(3)

                    if event.key == pg.K_4 or event.key == pg.K_KP4:
                        number_to_place = 4
                        sudoku_screen.sketch(4)

                    if event.key == pg.K_5 or event.key == pg.K_KP5:
                        number_to_place = 5
                        sudoku_screen.sketch(5)

                    if event.key == pg.K_6 or event.key == pg.K_KP6:
                        number_to_place = 6
                        sudoku_screen.sketch(6)

                    if event.key == pg.K_7 or event.key == pg.K_KP7:
                        number_to_place = 7
                        sudoku_screen.sketch(7)

                    if event.key == pg.K_8 or event.key == pg.K_KP8:
                        number_to_place = 8
                        sudoku_screen.sketch(8)

                    if event.key == pg.K_9 or event.key == pg.K_KP9:
                        number_to_place = 9
                        sudoku_screen.sketch(9)

                    if event.key == pg.K_UP:
                        if x_y_pos[1] == 0:
                            x_y_pos[1] = 8
                        else:
                            x_y_pos[1] -= 1
                        sudoku_screen.select(x_y_pos[0], x_y_pos[1])

                    if event.key == pg.K_DOWN:
                        if x_y_pos[1] == 8:
                            x_y_pos[1] = 0
                        else:
                            x_y_pos[1] += 1

                        sudoku_screen.select(x_y_pos[0], x_y_pos[1])

                    if event.key == pg.K_LEFT:
                        if x_y_pos[0] == 0:
                            x_y_pos[0] = 8
                        else:
                            x_y_pos[0] -= 1
                        sudoku_screen.select(x_y_pos[0], x_y_pos[1])

                    if event.key == pg.K_RIGHT:
                        if x_y_pos[0] == 8:
                            x_y_pos[0] = 0
                        else:
                            x_y_pos[0] += 1
                        sudoku_screen.select(x_y_pos[0], x_y_pos[1])

                    if event.key == pg.K_DELETE or event.key == pg.K_BACKSPACE:
                        sudoku_screen.clear()

                    if event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER:
                        sudoku_screen.place_number(number_to_place)

                        if sudoku_screen.is_full():

                            if sudoku_screen.check_board():
                                game_on = False
                                game_won = True
                                return game_won_screen(screen)

                            else:
                                game_on = False
                                game_over = True
                                return game_over_screen(screen)

            pg.display.update()


if __name__ == '__main__':
    main()
