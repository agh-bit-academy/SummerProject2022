# Maciej Bartczak
from math import inf


def get_factors(num):
    factors = []
    for factor in range(2, num + 1, 1):
        if num % factor == 0:
            factors.append(factor)
            while num % factor == 0:
                num //= factor
    return factors


def f(arr):
    size = len(arr)
    destination = size - 1

    def recur(i, counter):
        if i == destination:
            return counter
        if i > destination:
            return inf

        best = inf
        for factor in get_factors(arr[i]):
            best = min(best, recur(i + factor, counter + 1))
        if best == inf:
            return -1
        return best

    return recur(0, 0)
