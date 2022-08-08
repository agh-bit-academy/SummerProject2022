# Andrzej Karciński
from math import sqrt


def f():
    epsilon = 10 ** -7
    x = sqrt(0.5)
    result = 1
    resultBefore = 0.5
    while abs((2 / result) - (2 / resultBefore)) > epsilon:
        resultBefore = result
        result *= x
        x = sqrt(0.5 + (0.5 * x))
    print(2 / result)
