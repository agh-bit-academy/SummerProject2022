# Izabella Rosikoń
import math


def f(a, b):
    length_a = int(math.log10(a)) + 1
    length_b = int(math.log10(b)) + 1

    list_a = [0] * length_a
    list_b = [0] * length_b

    if length_a != length_b:
        return False
    else:
        for j in range(length_b):
            list_a[j] = a % 10
            list_b[j] = b % 10
            a = a // 10
            b = b // 10
    tab = [0] * 10

    for item in list_a:
        tab[item] = tab[item] + 1
    for jtem in list_b:
        tab[jtem] = tab[jtem] - 1

    return tab == [0] * 10
