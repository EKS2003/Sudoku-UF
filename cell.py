import pygame as pg


WIDTH = 603
HEIGHT = 603


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.cell_sketched_value = 0
        self.clicked = False
        self.width = WIDTH
        self.height = HEIGHT
        self.editable = False
        self.cell_filled = True
        if value == 0:
            self.cell_filled = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.cell_sketched_value = value

    def draw(self):
        # This sets the font of the numbers
        number_font = pg.font.Font(None, 70)
        small_font = pg.font.Font(None, 35)
        number_surf = number_font.render(str(self.value), 0, (0, 13, 51))
        sketched_surf = small_font.render(str(self.cell_sketched_value), 0, (0, 13, 51))
        empty_surf = number_font.render('', 0, (0, 13, 51))

        if self.value != 0:
            number_rect = number_surf.get_rect(
                center=(67 // 2 + 67 * self.row, 67 // 2 + 67 * self.col))
            self.screen.blit(number_surf, number_rect)

        else:
            if self.cell_sketched_value == 0:
                number_rect = empty_surf.get_rect(
                    center=(67 // 2 + 67 * self.row, 67 // 2 + 67 * self.col))
                self.screen.blit(empty_surf, number_rect)

            else:
                sketched_rect = sketched_surf.get_rect(
                    center=(67 * self.row + 10, 67 * self.col + 15))
                self.screen.blit(sketched_surf, sketched_rect)

        if self.clicked:
            pg.draw.rect(self.screen, "blue", pg.Rect(self.row * 67 - 1, self.col * 67 - 1, 67 + 3, 67 + 3), 3)

