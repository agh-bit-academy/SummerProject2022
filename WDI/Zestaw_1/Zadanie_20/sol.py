# Szymon Rusiecki
from math import sqrt


def f(a, b):
    while abs(a - b) > 10 ** (-6):
        a, b = sqrt(a * b), (a + b) / 2

    print((a + b) / 2)
