# Maciej Bartczak
# Izabella Rosikoń
import math


def f(a, b):
    length_a = int(math.log10(a)) + 1
    length_b = int(math.log10(b)) + 1

    if length_a != length_b:
        return False

    digit_counter = [0 for _ in range(10)]

    for _ in range(length_a):
        digit_counter[a % 10] += 1
        a //= 10
        digit_counter[b % 10] -= 1
        b //= 10

    for count in digit_counter:
        if count != 0:
            return False
    return True
