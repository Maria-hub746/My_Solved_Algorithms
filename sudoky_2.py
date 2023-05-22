import random


def generate_sudoku():
    grid = [[0] * 9 for _ in range(9)]

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            num = random.randint(1, 9)
            for k in range(3):
                for l in range(3):
                    while num in grid[i + k] or num in [row[j + l] for row in grid]:
                        num = random.randint(1, 9)
                    grid[i + k][j + l] = num

    solve_sudoku(grid)
    difficulty = 40
    while difficulty > 0:
        i = random.randint(0, 8)
        j = random.randint(0, 8)
        if grid[i][j] != 0:
            grid[i][j] = 0
            difficulty -= 1

    return grid


def solve_sudoku(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(grid, i, j, num):
                        grid[i][j] = num
                        if solve_sudoku(grid):
                            return True
                        else:
                            grid[i][j] = 0
                return False
    return True


def is_valid(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True


sudoku = generate_sudoku()
for row in sudoku:
    print(row)
