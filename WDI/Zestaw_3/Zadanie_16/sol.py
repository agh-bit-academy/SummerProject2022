# Karolina Kucia
from math import inf


def f(A):
    n = len(A)
    maxEl = -inf
    minEl = inf
    maxCnt = 0
    minCnt = 0
    for i in range(n):
        if A[i] > maxEl:
            maxEl = A[i]
            maxCnt = 1
        elif A[i] == maxEl:
            maxCnt += 1
        if A[i] < minEl:
            minEl = A[i]
            minCnt = 1
        elif A[i] == minEl:
            minCnt += 1

    if minCnt == maxCnt == 1:
        return True
    return False
