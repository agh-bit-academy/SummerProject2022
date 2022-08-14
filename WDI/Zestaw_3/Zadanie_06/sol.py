# Andrzej Karciński
from random import randint


def has_Odd(number):
    while number > 0:
        lastDigit = number % 10
        if lastDigit % 2 == 1:
            return True
        number //= 10
    return False


def f(n):
    array = [randint(1, 1000) for _ in range(n)]
    for number in array:
        if has_Odd(number) is False:
            return array, False
    return array, True
