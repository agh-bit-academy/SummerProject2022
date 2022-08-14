# Andrzej Karciński

def has_Odd(number):
    while number > 0:
        lastDigit = number % 10
        if lastDigit % 2 == 1:
            return True
        number //= 10
    return False


def f(array):
    for element in array:
        if has_Odd(element) is False:
            return False
    return True
