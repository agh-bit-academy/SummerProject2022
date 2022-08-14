# Karolina Kucia
from math import inf


def f(A):
    n = len(A)
    max_el = -inf
    min_el = inf
    max_cnt = 0
    min_cnt = 0
    for i in range(n):
        if A[i] > max_el:
            max_el = A[i]
            max_cnt = 1
        elif A[i] == max_el:
            max_cnt += 1
        if A[i] < min_el:
            min_el = A[i]
            min_cnt = 1
        elif A[i] == min_el:
            min_cnt += 1

    if min_cnt == max_cnt == 1:
        return True
    return False
