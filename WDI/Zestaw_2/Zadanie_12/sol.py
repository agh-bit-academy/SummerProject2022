# Dominik Adamczyk
import math


def f(num):
    length = int(math.log10(num) + 1)
    if length > 9:
        return False
    while num != 0:
        if num % 10 == length:
            return True
        num //= 10
    return False
