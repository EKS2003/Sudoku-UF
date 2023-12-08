import pygame as pg
from cell import Cell
from sudoku_generator import *

WIDTH = 603
HEIGHT = 603


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.rows = 9
        self.cols = 9
        self.board = generate_sudoku(9, difficulty)
        self.cells = [[Cell(self.board[row][col], row, col, self.screen) for col in range(9)] for row in range(9)]
        self.unused_cells = []

    def draw(self):
        self.screen.fill((254, 240, 255))
        for i in range(0, 3 + 1):
            pg.draw.line(
                self.screen,(0, 13, 51),(0, i * 67 * 3),(WIDTH, i * 67 * 3), 5)

        for i in range(0, 3 + 1):
            pg.draw.line(self.screen,(0, 13, 51),(i * 67 * 3, 0),(i * 67 * 3, HEIGHT), 5)

        for i in range(0, 9 + 1):
            pg.draw.line(self.screen,(0, 13, 51),(0, i * 67),(WIDTH, i * 67),1)

        for i in range(1, 9):
            pg.draw.line(self.screen,(0, 13, 51),(i * 67, 0),(i * 67, WIDTH), 1)

        for list_cells in self.cells:
            for cell in list_cells:
                cell.draw()

    def select(self, row, col):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].clicked = False
        self.cells[row][col].clicked = True
        self.click(row, col)

    def click(self, x, y):
        clicked_row = x // 67
        clicked_col = y // 67
        if clicked_row in range(9) and clicked_col in range(9):
            print([clicked_row, clicked_col])
            return [clicked_row, clicked_col]
        else:
            return None

    def clear(self):
        for cell_list in range(9):
            for cell in range(9):
                if self.cells[cell_list][cell].clicked:
                    if self.cells[cell_list][cell].cell_filled == False:
                        self.cells[cell_list][cell].value = 0
                        self.cells[cell_list][cell].cell_sketched_value = 0

    def sketch(self, value):

        for cell_list in self.cells:
            for cell in cell_list:
                if cell.clicked:
                    cell.set_sketched_value(value)

    def place_number(self, value):
        self.find_empty()

        for cell_list in range(9):
            for cell in range(9):
                if self.cells[cell_list][cell].clicked:
                    if (cell_list, cell) in self.unused_cells:

                        if self.cells[cell_list][cell].cell_sketched_value == 0:
                            self.cells[cell_list][cell].set_cell_value(0)
                        else:
                            self.cells[cell_list][cell].set_cell_value(value)

    def reset_to_original(self):

        for row in range(9):
            for col in range(9):
                if (row, col) in self.unused_cells:
                    self.cells[row][col].set_cell_value(0)
                    self.cells[row][col].set_sketched_value(0)
                    self.cells[row][col].clicked = False

    def is_full(self):
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value == 0:
                    return False
        return True

    def update_board(self):

        for row in range(9):
            for col in range(9):
                self.board[row][col] = self.cells[row][col].value

    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value == 0:
                    pos_cell = (row, col)
                    self.unused_cells.append(pos_cell)

        return self.unused_cells

    def check_board(self):

        for row in range(9):
            row_list = set()
            for col in range(9):
                num = self.cells[row][col].value
                if num in row_list:
                    return False
                row_list.add(num)

        for col in range(9):
            col_list = set()
            for row in range(9):
                num = self.cells[row][col].value
                if num in col_list:
                    return False
                col_list.add(num)

        for col in range(0, 9, 3):
            for row in range(0, 9, 3):
                small_box = set()
                for i in range(3):
                    for j in range(3):
                        num = self.cells[i + col][j + row].value
                        if num in small_box:
                            return False
                        small_box.add(num)
        return True
