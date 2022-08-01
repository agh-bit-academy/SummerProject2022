# Szymon Rusiecki
from math import sqrt
APPROX_ERROR = 10 ** (-6)


def f(a, b):
    while (a - b) > APPROX_ERROR or (b - a) > APPROX_ERROR:
        a, b = sqrt(a * b), (a + b) / 2

    print((a + b) / 2)
