# Bartłomiej Kozera
from math import sqrt

ZERO_NUMBER = 0
ONE_NUMBER = 1
SUMMAND = 1
SMALLEST_PRIME_NUM = 2


def f(x):
    if x == ZERO_NUMBER or x == ONE_NUMBER:
        print(False)
        return
    factor = SMALLEST_PRIME_NUM

    while factor < int(sqrt(x)) + SUMMAND:
        if x % factor == ZERO_NUMBER:
            print(False)
            return
        factor += SUMMAND
    print(True)
    return
