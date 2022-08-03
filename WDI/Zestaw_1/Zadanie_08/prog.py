# Bartłomiej Kozera

from math import sqrt


def f(x):
    if x <= 0 or x == 1:
        print(False)
        return

    if x == 2 or x == 3:
        print(True)
        return

    if x % 2 == 0 or x % 3 == 0:
        print(False)
        return

    factor = 5

    while factor < int(sqrt(x)) + 1:
        if x % factor == 0:
            print(False)
            return
        factor += 2

        if x % factor == 0:
            print(False)
            return
        factor += 4

    print(True)
