# Szymon Rusiecki
from math import sqrt
SET_PRECISION = 10 ** (-6)


def f(a, b):
    while abs(a - b) > SET_PRECISION:
        a, b = sqrt(a * b), (a + b) / 2

    print((a + b) / 2)
