# Juliusz Wasieleski
def min_positive(tab):
    result, index = float('inf'), None
    for i in range(len(tab)):
        if 0 < tab[i] < result:
            result, index = tab[i], i
    return result, index


def max_negative(tab):
    result, index = -float('inf'), None
    for i in range(len(tab)):
        if 0 > tab[i] > result:
            result, index = tab[i], i
    return result, index


def max_positive(tab):
    result, index = -1, None
    for i in range(len(tab)):
        if tab[i] >= 0 and tab[i] > result:
            result, index = tab[i], i
    return result, index


def min_negative(tab):
    result, index = 1, None
    for i in range(len(tab)):
        if tab[i] <= 0 and tab[i] < result:
            result, index = tab[i], i
    return result, index


def find_best_division(sum_of_rows, sum_of_cols):
    min_c, ind_min_c = min_negative(sum_of_cols)
    min_r, ind_min_r = min_positive(sum_of_rows)
    max_r, ind_max_r = max_negative(sum_of_rows)
    max_c, ind_max_c = max_positive(sum_of_cols)
    if ind_max_r is None and ind_min_r is None:
        return [0, 0]
    elif ind_max_r is None:
        return [ind_min_r, ind_max_c]
    elif ind_min_r is None:
        return [ind_max_r, ind_min_c]
    else:
        negative_division = min_c / max_r
        positive_division = max_c / min_r
        if negative_division > positive_division:
            return [ind_max_r, ind_min_c]
        else:
            return [ind_min_r, ind_max_c]


def f(tab):
    n = len(tab)
    m = len(tab[0])
    sum_of_rows = [0 for _ in range(n)]
    sum_of_cols = [0 for _ in range(m)]
    for i in range(n):
        for j in range(m):
            sum_of_rows[i] += tab[i][j]
            sum_of_cols[j] += tab[i][j]

    return find_best_division(sum_of_rows, sum_of_cols)
