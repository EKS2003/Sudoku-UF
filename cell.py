import pygame


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        cell_size = 50

        x = self.col * cell_size
        y = self.row * cell_size

        # Draw cell outline
        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), (x, y, cell_size, cell_size), 2)
        else:
            pygame.draw.rect(self.screen, (0, 0, 0), (x, y, cell_size, cell_size), 2)

        # Draw value or sketched value
        if self.value != 0:
            font = pygame.font.SysFont("comicsansms", 30)
            text = font.render(str(self.value), True, (0, 0, 0))
            self.screen.blit(text,
                             (x + cell_size // 2 - text.get_width() // 2, y + cell_size // 2 - text.get_height() // 2))
        elif self.sketched_value != 0:
            font = pygame.font.SysFont("comicsansms", 15)
            text = font.render(str(self.sketched_value), True, (0, 0, 0))
            self.screen.blit(text,
                             (x + cell_size // 2 - text.get_width() // 2, y + cell_size // 2 - text.get_height() // 2))
