# Bartłomiej Kozera

EPSILON = 10**(-6)
LOW = 1
FACTOR = 2


def f(num, eps=EPSILON):
    low, high = LOW, num

    while abs(low - high) >= eps:
        low = (low + high) / FACTOR
        high = num/low
    print((low + high) / FACTOR)
    return
