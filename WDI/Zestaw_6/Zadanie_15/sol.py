# Juliusz Wasieleski
def is_it_possible(tab, x, y):
    for row in range(len(tab)):
        if tab[row] != -1 and (row == x or tab[row] == y):
            return False
        if tab[row] != -1 and (row + tab[row] == x + y):
            return False
        if tab[row] != -1 and (row - tab[row] == x - y):
            return False
    return True


def rek(left, solution):
    n = len(solution)
    if left == 0:
        return True

    for x in range(n):
        for y in range(n):
            if is_it_possible(solution, x, y):
                solution[x] = y
                if rek(left - 1, solution):
                    return True
                solution[x] = -1
    return False


def f():
    n = 8
    solution = [-1 for _ in range(n)]
    rek(n, solution)
    return solution
