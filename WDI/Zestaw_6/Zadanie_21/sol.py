# Juliusz Wasieleski
def rek(tab, row, curr_sum, sum, not_empty, columns):
    n = len(tab)
    m = len(tab[0])
    if row == n:
        return curr_sum == sum and not_empty
    for col in range(m):
        if not columns[col]:
            if rek(tab, row + 1, curr_sum, sum, not_empty, columns):
                return True
            columns[col] = True
            if rek(tab, row + 1, curr_sum + tab[row][col], sum, True, columns):
                return True
            columns[col] = False
    return False


def f(tab, k):
    m = len(tab[0])
    columns = [False for _ in range(m)]
    return rek(tab, 0, 0, k, False, columns)
