# Andrzej Karciński
from math import sqrt


def f():
    epsilon = 10 ** -7
    x = sqrt(0.5)
    result = 1
    result_before = 0.5
    while abs((2 / result) - (2 / result_before)) > epsilon:
        result_before = result
        result *= x
        x = sqrt(0.5 + (0.5 * x))
    print(2 / result)
