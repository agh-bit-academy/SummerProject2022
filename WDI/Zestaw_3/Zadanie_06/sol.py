# Andrzej Karciński
from random import randint


def has_odd(number):
    while number > 0:
        last_digit = number % 10
        if last_digit % 2 == 1:
            return True
        number //= 10
    return False


def f(n):
    array = [randint(1, 1000) for _ in range(n)]
    for number in array:
        if has_odd(number) is False:
            return array, False
    return array, True
