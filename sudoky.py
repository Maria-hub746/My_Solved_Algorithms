def puzzle(a):
    for i in range(9):
        for j in range(9):
            print(a[i][j],end = " ")
        print()

def solve_sudoku(board):
    """
    Функция решает судоку на доске.

    Args:
    - board (list): двумерный список размером 9х9 с цифрами от 0 до 9. 0 означает пустую клетку.

    Returns:
    - board (list): решенная доска, если судоку был решен.
    - None: если судоку не был решен.
    """

    # Рекурсивная функция, чтобы решить судоку
    def solve(row, col):
        # если достигнут конец строки, перейти на следующую строку
        if col == 9:
            return solve(row + 1, 0)

        # если достигнут конец доски, судоку решен
        if row == 9:
            return True

        # если текущая ячейка уже заполнена, перейти к следующей ячейке
        if board[row][col] != 0:
            return solve(row, col + 1)

        # попробовать вставить значения от 1 до 9 в текущую ячейку
        for num in range(1, 10):
            if is_valid(row, col, num):
                board[row][col] = num
                if solve(row, col + 1):
                    return True
                # если решение не найдено, вернуться и попробовать другие значения
                board[row][col] = 0

        # если не удалось найти решение, судоку не может быть решен
        return False

    # Проверка, допустимо ли вставить число в данную ячейку
    def is_valid(row, col, num):
        # проверка строки
        for i in range(9):
            if board[row][i] == num:
                return False

        # проверка столбца
        for i in range(9):
            if board[i][col] == num:
                return False

        # проверка блока 3х3
        block_row = (row // 3) * 3
        block_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[block_row + i][block_col + j] == num:
                    return False

        # если число может быть вставлено в ячейку
        return True

    # Запуск функции для решения судоку
    if solve(0, 0):
        return board
    else:
        return None

board = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
    [4, 0, 7, 0, 0, 0, 2, 0, 8],
    [0, 0, 5, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 8, 1, 0, 0],
    [0, 4, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 3, 6, 0, 0, 7, 2],
    [0, 7, 0, 0, 0, 0, 0, 0, 3],
    [9, 0, 3, 0, 0, 0, 6, 0, 4]]

if solve_sudoku(board):
    puzzle(board)
else:
    print('Solution does not exist:(')