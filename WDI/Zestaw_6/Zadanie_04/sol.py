# Karol Sewiło
def f(n):
    board = [[-1 for _ in range(n)] for _ in range(n)]
    array = [[rek(board, 0, 0, 0, i, j) for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if array[i][j] == float('inf'):
                array[i][j] = -1

    return array


def rek(board, x, y, i, stop_x, stop_y):
    if y == stop_y and x == stop_x:
        return i

    if board[x][y] == -1:
        board[x][y] = i
    else:
        return float('inf')

    moves = ((1, 2), (-1, 2), (1, -2), (-1, -2),
             (2, 1), (2, -1), (-2, 1), (-2, -1))
    minimal_number_of_moves = float('inf')

    for x_m, y_m in moves:
        if 0 <= x + x_m < len(board) and 0 <= y + y_m < len(board):
            minimal_number_of_moves = min(rek(board, x + x_m, y + y_m, i + 1, stop_x, stop_y), minimal_number_of_moves)

    board[x][y] = -1

    return minimal_number_of_moves
