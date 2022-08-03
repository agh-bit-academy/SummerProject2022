# Bartłomiej Kozera
from math import sqrt


def f(x):
    for factor in range(int(sqrt(x)), 0, -1):
        if x % factor == 0:
            factor2 = x // factor  # Dziele całkowicie bo ładniej to wylgądało w outpucie jak są 2 inty
            return factor, factor2
