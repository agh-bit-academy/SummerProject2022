# Bartłomiej Kozera

from math import sqrt


def f():
    for i in range(1, 10**6 + 1):
        num1 = i
        num2 = 0

        for j in range(1, int(sqrt(num1)) + 1):
            if num1 % j == 0:
                if j == 1:
                    num2 += j
                else:
                    num2 += j + (num1/j)

        for j in range(1, int(sqrt(num2)) + 1):
            if num2 % j == 0:
                if j == 1:
                    num1 -= j
                else:
                    num1 -= j + (num2/j)
        if num1 == 0 and i < num2:  # Wypisuje liczby w kolejności mniejsza, wieksza
            print(i, int(num2))
