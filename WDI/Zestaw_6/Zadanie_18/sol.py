# Juliusz Wasielski
def get_first_digit(num):
    while num > 9:
        num //= 10

    return num


def can_move(tab, row, col, new_row, new_col):
    n = len(tab)
    m = len(tab[0])
    if new_row < 0 or new_col < 0 or new_row >= n or new_col >= m:
        return False
    return tab[row][col] % 10 < get_first_digit(tab[new_row][new_col])


def f(tab, row=0, col=0):
    n = len(tab)
    m = len(tab[0])
    if row + 1 == n and col + 1 == m:
        return True
    if can_move(tab, row, col, row + 1, col):
        if f(tab, row + 1, col):
            return True
    if can_move(tab, row, col, row, col + 1):
        if f(tab, row, col + 1):
            return True
    if can_move(tab, row, col, row + 1, col + 1):
        if f(tab, row + 1, col + 1):
            return True
    return False
