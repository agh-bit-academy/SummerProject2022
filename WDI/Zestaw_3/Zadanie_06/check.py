# Andrzej Karciński

def has_odd(number):
    while number > 0:
        last_digit = number % 10
        if last_digit % 2 == 1:
            return True
        number //= 10
    return False


def f(array):
    for element in array:
        if has_odd(element) is False:
            return False
    return True
