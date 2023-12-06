import pygame
from cell import Cell
# Board class
class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = [[Cell() for _ in range(9)] for _ in range(9)]
        self.selected_cell = None
#draw board on pygame
    def draw(self):
        # Draw grid outline
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, self.width, self.height), 2)
# Draw bold lines to delineate 3x3 boxes
        for x in range(0, self.width, self.width // 3):
            pygame.draw.line(self.screen, (0, 0, 0), (x, 0), (x, self.height), 3)
        for y in range(0, self.height, self.height // 3):
            pygame.draw.line(self.screen, (0, 0, 0), (0, y), (self.width, y), 3)
# Draw each cell
        for row in range(9):
            for col in range(9):
                cell = self.cells[row][col]
                cell.draw(self.screen, row, col, self.selected_cell)
#select cell
    def select(self, row, col):
        self.selected_cell = (row, col)
#user click function
    def click(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            cell_width = self.width // 9
            cell_height = self.height // 9
            row = y // cell_height
            col = x // cell_width
            return (row, col)
        else:
            return None
#clears ell
    def clear(self):
        if self.selected_cell:
            row, col = self.selected_cell
            self.cells[row][col].clear()
#sketch input value
    def sketch(self, value):
        if self.selected_cell:
            row, col = self.selected_cell
            self.cells[row][col].set_sketched_value(value)
#set value of cell to input value
    def place_number(self, value):
        if self.selected_cell:
            row, col = self.selected_cell
            self.cells[row][col].set_value(value)
#resets board
    def reset_to_original(self):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].reset_to_original()
#checks of board is full
    def is_full(self):
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].get_value() == 0:
                    return False
        return True
#updates board code to check
    def update_board(self):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].update()
#check for empty cells
    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].get_value() == 0:
                    return (row, col)
        return None
#makes sure sudoku is achieved
    def check_board(self):
# Check rows
        for row in range(9):
            values = set()
            for col in range(9):
                value = self.cells[row][col].get_value()
                if value != 0:
                    if value in values:
                        return False
                    values.add(value)
# Check columns
        for col in range(9):
            values = set()
            for row in range(9):
                value = self.cells[row][col].get_value()
                if value != 0:
                    if value in values:
                        return False
                    values.add(value)
# Check 3x3 boxes
        for box_row in range(3):
            for box_col in range(3):
                values = set()
                for row in range(box_row * 3, (box_row + 1) * 3):
                    for col in range(box_col * 3, (box_col + 1) * 3):
                        value = self.cells[row][col].get_value()
                        if value != 0:
                            if value in values:
                                return False
                            values.add(value)
        return True
