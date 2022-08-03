# Krzysztof Mach
from math import factorial


APPROX_ERROR = 10 ** (-6)


def f(x):
    val = 0
    k = 0
    while True:
        change = (((-1) ** k) * (x ** (2 * k))) / factorial(2 * k)
        val += change
        k += 1
        if abs(change) < APPROX_ERROR:
            print(val)
            return
