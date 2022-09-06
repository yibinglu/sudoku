# logic.py
# Recursive backtracking file

import pprint

grid = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
        [6, 8, 0, 0, 7, 0, 0, 9, 0],
        [1, 9, 0, 0, 0, 4, 5, 0, 0],
        [8, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0],
        [0, 5, 0, 0, 0, 3, 0, 2, 8],
        [0, 0, 9, 3, 0, 0, 0, 7, 4],
        [0, 4, 0, 0, 5, 0, 0, 3, 6],
        [7, 0, 3, 0, 1, 8, 0, 0, 0]]


def solve_grid(row, col):
    '''Solves sudoku board using backtracking'''
    if col == 9 and row == 8:  # Reached the end of the board
        return True

    if col == 9 and row < 8:  # Move onto the next row
        row += 1
        col = 0

    if grid[row][col] == 0:  # Found empty cell, solve
        for num in range(1, 10):
            if check_num(row, col, num):
                grid[row][col] = num

                if solve_grid(row, col + 1):  # Recursive call
                    return True

        grid[row][col] = 0  # Backtrack

    else:  # Move onto next cell
        if solve_grid(row, col + 1):
            return True


def check_num(row, col, num):
    '''Check if num is a viable option in current row-col cell'''
    rowRange = 0
    colRange = 0

    if num in grid[row]:  # Check row
        return False

    for i in range(0, 9):  # Check column
        if num == grid[i][col]:
            return False

    #  Check 3x3 square
    if row <= 2:
        rowRange = 2

    elif row <= 5:
        rowRange = 5

    elif row <= 8:
        rowRange = 8

    if col <= 2:
        colRange = 2

    elif col <= 5:
        colRange = 5

    elif col <= 8:
        colRange = 8

    for i in range(rowRange - 2, rowRange + 1):
        for j in range(colRange - 2, colRange + 1):
            if num == grid[i][j]:
                return False

    return True


# solve_grid(0, 0)
# pprint.pp(grid)
