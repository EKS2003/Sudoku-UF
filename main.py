import sys
import pygame as pg
import board as board

pg.init()
WIDTH = 750
HEIGHT = 750
screen_size = 750, 750
screen = pg.display.set_mode(screen_size)
font = pg.font.SysFont(None, 80)

def draw_gamestart(starting_screen):
    title_font = pg.font.Font(None, 100)
    selection_title_font = pg.font.Font(None, 70)
    button_font = pg.font.Font(None, 50)

    title_surface = title_font.render("Sudoku", 0, "black")
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    starting_screen.blit(title_surface, title_rectangle)

    select_title_surface = selection_title_font.render("select Game Mode:", True, (0, 0, 0))
    select_title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(select_title_surface, select_title_rectangle)

    easy_text = button_font.render("Easy", 0, "black")
    easy_surface = pg.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill("gray")
    easy_surface.blit(easy_text, (10,10))
    easy_rectangle = easy_surface.get_rect(center=(WIDTH // 2 - 100, HEIGHT // 2))
    screen.blit(easy_surface, easy_rectangle)

    medium_text = button_font.render("Medium", 0, "black")
    medium_surface = pg.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill("gray")
    medium_surface.blit(medium_text, (10, 10))
    medium_rectangle = medium_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(medium_surface, medium_rectangle)

    hard_text = button_font.render("Hard", 0, "black")
    hard_surface = pg.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill("gray")
    hard_surface.blit(hard_text, (10, 10))
    hard_rectangle = hard_surface.get_rect(center=(WIDTH // 2 + 100, HEIGHT // 2))
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if easy_rectangle.collide(event.pos):
                    return 30
                elif medium_rectangle.collide(event.pos):
                    return 40
                elif hard_rectangle.collide(event.pos):
                    return 50

        pg.display.update()


def draw_game_on(screen):
    button_font = pg.font.Font(None, 40)

    reset_text = button_font.render("Reset", 0, "black")
    restart_text = button_font.render("Restart", 0, "black")
    exit_text = button_font.render("Exit", 0, "black")

    reset_surface = pg.Surface((reset_text.get_size()[0] + 20, reset_text.get()[1] + 20))
    reset_surface.fill("gray")
    reset_surface.blit(reset_text, (10, 10))
    reset_rectangle = reset_surface.get_rect(center=(WIDTH // 2 - 200, HEIGHT // 2 - 200))
    screen.blit(reset_surface, reset_rectangle)

    restart_surface = pg.Surface((restart_text.get_size()[0] + 20, restart_text.get()[1] + 20))
    restart_surface.fill("gray")
    restart_surface.blit(restart_text, (10, 10))
    restart_rectangle = restart_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200))
    screen.blit(restart_surface, restart_rectangle)

    exit_surface = pg.Surface((exit_text.get_size()[0] + 20, exit_text.get()[1] + 20))
    exit_surface.fill("gray")
    exit_surface.blit(exit_text, (10, 10))
    exit_rectangle = exit_surface.get_rect(center=(WIDTH // 2 + 200, HEIGHT // 2 - 200))
    screen.blit(exit_surface, exit_rectangle)

    return reset_rectangle, restart_rectangle, exit_rectangle


def draw_game_over(screen):
    game_over_font = pg.font.Font(None, 100)
    restart_text = game_over_font.render("Restart", 0, "black")

    screen.fill("black")

    if board.check_board():
        text = "Game Won"

    else:
        text = "Game Over"

    restart_surface = pg.Surface((restart_text.get_size()[0] + 20, restart_text.get()[1] + 20))
    restart_surface.fill("gray")
    restart_surface.blit(restart_text, (10, 10))
    restart_rectangle = restart_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200))
    screen.blit(restart_surface, restart_rectangle)

    game_over_surface = game_over_font.render(text, True, "white")
    game_over_rectangle = game_over_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(game_over_surface, game_over_rectangle)


    pg.display.update()
    return restart_rectangle


if __name__ == '__main__':
    game_completed = False
    Done = False
    pg.init()
    pg.display.set_caption("Sudoku")
    screen = pg.display.set_mode((723, 800))
    screen.fill((255, 255, 245))
    draw_game_on(screen)

    # draw the game start screen and get the selected difficulty
    difficulty = draw_game_on(screen)
    # initialize the game board with the selected difficulty
    board = board(723, 723, screen, difficulty=difficulty)

    # main game loop
    while not Done:
        while not game_completed:
            # draw game in progress screen
            screen.fill((255, 255, 245))
            reset_rectangle, restart_rectangle, exit_rectangle = draw_game_in_progress(screen)
            board.draw()
            pg.display.update()

        # event handling for the game in progress
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:  # <-- orlando
                x, y = event.pos
                # check if the player clicks on the buttons
                if reset_rectangle.collidepoint(x, y):
                    board = board(723, 723, screen, difficulty=difficulty)
                elif restart_rectangle.collidepoint(x, y):
                    screen.fill((255, 255, 245))
                    difficulty = draw_game_on(screen)
                    board = board(723, 723, screen, difficulty=difficulty)
                elif exit_rectangle.collidepoint(x, y):
                    pg.quit()
                    sys.exit()
                # player clicked on the puzzle board, handle the click
            else:
                click_result = board.click(x, y)
                if click_result is not None:
                    row, col = click_result
                    board.cells[row][col].is_selected = True
                    board.selected_row, board.selected_col = row, col

        if event.type == pg.KEYUP:
            # handle keyboard input for number selection
            if event.key == pg.K_1:
                board.sketch(1)
            elif event.key == pg.K_2:
                board.sketch(2)
            elif event.key == pg.K_3:
                board.sketch(3)
            elif event.key == pg.K_4:
                board.sketch(4)
            elif event.key == pg.K_5:
                board.sketch(5)
            elif event.key == pg.K_6:
                board.sketch(6)
            elif event.key == pg.K_7:
                board.sketch(7)
            elif event.key == pg.K_8:
                board.sketch(8)
            elif event.key == pg.K_9:
                board.sketch(9)
            # check if game is completed
            if board.is_full():
                game_completed = True
        # game is completed, show the game over screen
        screen.fill((255, 255, 245))
        draw_game_over(screen)
        pg.display.update()

        # event handling for the game over screen
        while game_completed:
            restart_opt = draw_game_over(screen)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    Done = True
                    pg.quit()
                    sys.exit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    # check if the player clicks on the "Restart" button
                    if restart_opt.collidepoint(x, y):
                        game_completed = False
                        # restart the game by resetting the board and difficulty
                        pg.init()
                        pg.display.set_caption("Sudoku")
                        screen = pg.display.set_mode((723, 800))
                        screen.fill((255, 255, 245))
                        draw_game_on(screen)
                        difficulty = draw_game_on(screen)
                        board = board(723, 723, screen, difficulty=difficulty)
                        pg.display.update()





