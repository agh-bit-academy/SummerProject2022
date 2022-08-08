# Jakub Bizan
from math import log


def f():
    a = 10
    b = 1
    while a != b:
        b = a
        a = a - (a ** a - 2020) / ((a ** a) * (log(a) + 1))
    return a
