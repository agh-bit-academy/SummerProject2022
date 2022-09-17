# Juliusz Wasieleski
from math import sqrt
from math import inf


def center_of_gravity(t, taken):
    if len(taken) == 0:
        return inf
    x = 0
    y = 0
    for i in taken:
        x += t[i][0]
        y += t[i][1]
    x /= len(taken)
    y /= len(taken)
    return sqrt(x ** 2 + y ** 2)


def f(t, r, k, taken=[], i=0):
    if len(taken) % 3 == 0 and center_of_gravity(t, taken) < r and len(taken) > k:
        return True
    if i == len(t):
        return False
    if f(t, r, k, taken, i + 1) or f(t, r, k, [*taken, i], i + 1):
        return True
    else:
        return False
