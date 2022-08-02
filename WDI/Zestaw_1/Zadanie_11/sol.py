# Bartłomiej Kozera

from math import sqrt

ITERATOR = 10**6 + 1
LOWER_BOUND = 1
START_FOR_NU2_END_FOR_NUM1 = 0
NUM_DIVISIBLE_BY = 0


def f():
    for i in range(LOWER_BOUND, ITERATOR):
        num1 = i
        num2 = START_FOR_NU2_END_FOR_NUM1

        for j in range(LOWER_BOUND, int(sqrt(num1)) + LOWER_BOUND):
            if num1 % j == NUM_DIVISIBLE_BY:
                if j == LOWER_BOUND:
                    num2 += j
                else:
                    num2 += j + (num1/j)

        for j in range(LOWER_BOUND, int(sqrt(num2)) + LOWER_BOUND):
            if num2 % j == NUM_DIVISIBLE_BY:
                if j == LOWER_BOUND:
                    num1 -= j
                else:
                    num1 -= j + (num2/j)
        if num1 == START_FOR_NU2_END_FOR_NUM1 and i < num2:  # Wypisuje liczby w kolejności mniejsza, wieksza
            print(i, int(num2))
    return
