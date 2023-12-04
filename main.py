import sys
import pygame as pg

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
    easy_rectangle = easy_surface.get_rect(center=(WIDTH // 2 + 100, HEIGHT // 2))
    screen.blit(easy_surface, easy_rectangle)

    medium_text = button_font.render("Medium", 0, "black")
    medium_surface = pg.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill("gray")
    medium_surface.blit(medium_text, (10, 10))
    medium_rectangle = medium_surface.get_rect(center=(WIDTH // 2 + 100, HEIGHT // 2))
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
