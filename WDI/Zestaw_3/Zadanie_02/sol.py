# Izabella Rosikoń
import math


def f(a, b):
    lengthA = int(math.log10(a)) + 1
    lengthB = int(math.log10(b)) + 1

    listA = [0] * lengthA
    listB = [0] * lengthB

    if lengthA != lengthB:
        return False
    else:
        for j in range(lengthB):
            listA[j] = a % 10
            listB[j] = b % 10
            a = a // 10
            b = b // 10
    tab = [0] * 10

    for item in listA:
        tab[item] = tab[item] + 1
    for jtem in listB:
        tab[jtem] = tab[jtem] - 1

    return tab == [0] * 10
