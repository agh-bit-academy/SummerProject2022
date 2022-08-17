from math import inf


def f(A):
    n = len(A)
    m = len(A[0])
    min_row_sum = inf
    idy = 0
    for y in range(n):
        tmp_row_sum = 0
        for x in range(m):
            tmp_row_sum += A[y][x]
        if tmp_row_sum < min_row_sum:
            min_row_sum = tmp_row_sum
            idy = y

    max_col_sum = 0
    idx = 0
    for x in range(m):
        tmp_col_sum = 0
        for y in range(n):
            tmp_col_sum += A[y][x]
        if tmp_col_sum > max_col_sum:
            max_col_sum = tmp_col_sum
            idx = x
    return [idy, idx]
