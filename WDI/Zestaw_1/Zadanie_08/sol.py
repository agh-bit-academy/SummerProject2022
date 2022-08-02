# Bartłomiej Kozera
from math import sqrt


def f(x):
    if x == 0 or x == 1:
        print(False)
        return
    factor = 2

    while factor < int(sqrt(x)) + 1:
        if x % factor == 0:
            print(False)
            return
        factor += 1
    print(True)
