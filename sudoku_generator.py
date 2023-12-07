import math,random

class SudokuGenerator:
    # Constructor of the SudokuGenerator class

    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for i in range(self.row_length)] for j in range(self.row_length)]
        self.box_length = int(math.sqrt(self.row_length))

    # Method to return the current state of the board
    def get_board(self):

        return self.board

    # Method to print the board to the console
    def print_board(self):
        for row in self.board:
            for col in row:
                print(col, end=' ')
            print()

    # Method to check if a number is valid in a given row
    def valid_in_row(self, row, num):
        counter = 0
        for i in range(self.row_length):
            if self.board[row][i] == num:
                counter += 1
        if counter == 1:
            return False
        else:
            return True

    # Method to check if a number is valid in a given column
    def valid_in_col(self, col, num):
        counter = 0
        for i in range(self.row_length):
            if self.board[i][col] == num:
                counter += 1
        if counter == 1:
            return False
        else:
            return True
    # Method to check if a number is valid in a 3x3 box

    def valid_in_box(self, row_start, col_start, num):
        counter = 0
        for row in range(row_start, row_start + 3):
            for column in range(col_start, col_start + 3):
                if self.board[row][column] == num:
                    counter += 1
        if counter == 1:
            return False
        else:
            return True

    # Method to check if a number is valid in its row, column, and box
    def is_valid(self, row, col, num):
        return (self.valid_in_row(row,num) and self.valid_in_col(col, num) and self.valid_in_box(row // 3 * 3 if row % 3 != 0 else row, col // 3 * 3 if col % 3 != 0 else col, num))

    # Method to fill a 3x3 box with valid numbers

    def fill_box(self, row_start, col_start):
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                while True:
                    boardEntry = random.randint(1,self.row_length)
                    if self.is_valid(i,j,boardEntry) is True:
                        self.board[i][j] = boardEntry
                        break
    # Method to fill all the diagonal 3x3 boxes (which are independent of each other)

    def fill_diagonal(self):
        for i in range(self.box_length):
            self.fill_box(i * 3, i * 3)

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        counter = 0
        while counter != self.removed_cells:
            row = random.randint(0,8)
            col = random.randint(0,8)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                counter += 1

def generate_sudoku(size,removed):
     sudoku = SudokuGenerator(size, removed)
     sudoku.fill_values()
     sudoku.remove_cells()
     board = sudoku.get_board()
     return board

