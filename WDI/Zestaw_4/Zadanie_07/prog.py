# Bartłomiej Kozera
from math import inf


def f(A, B):
    n = len(A)
    tab_of_ids = [0 for _ in range(n)]
    id_b = 0
    while id_b < n ** 2:
        minn = inf
        minn_id = 0
        for i in range(n):
            if tab_of_ids[i] != n:
                if minn > A[i][tab_of_ids[i]]:
                    minn = A[i][tab_of_ids[i]]
                    minn_id = i
        B[id_b] = minn
        tab_of_ids[minn_id] += 1
        id_b += 1
    return B
