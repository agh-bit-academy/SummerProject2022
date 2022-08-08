# Krzysztof Mach
from math import factorial


def f(x):
    val = 0
    k = 0
    while True:
        change = (((-1) ** k) * (x ** (2 * k))) / factorial(2 * k)
        val += change
        k += 1
        if abs(change) < 10 ** (-6):
            print(val)
            return
