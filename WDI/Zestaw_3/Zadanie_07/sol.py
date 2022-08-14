# Juliusz Wasieleski
from random import randint


def are_all_digits_odd(a) -> bool:
    while a > 0:
        if a % 2 == 0:
            return False
        a //= 10
    return True


def f(n) -> tuple:
    output_tab = [randint(1, 1000) for _ in range(n)]
    for number in output_tab:
        if are_all_digits_odd(number):
            return output_tab, True
    return output_tab, False
