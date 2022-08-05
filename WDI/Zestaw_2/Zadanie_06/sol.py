# Kacper Słoniec
from math import sqrt


def f(n):
    for factor in range(int(sqrt(n)), n):
        if n % factor == 0:
            return factor, n//factor
