# Andrzej Karciński
def f(number):
    a = 1
    b = 1
    c = 2
    while (a * b) <= number:
        if a * b == number:
            return True
        a, b = b, c
        c = a + b
    return False
