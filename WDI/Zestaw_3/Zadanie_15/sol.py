# Andrzej Karciński
def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


def f(array):
    a = 1
    b = 2
    c = 3
    prime_number = False

    if is_prime(array[0]):
        return False

    for i in range(len(array)):
        if i == a:
            a, b = b, c
            c = a + b
            if is_prime(array[i]) is True:
                return False
        else:
            if is_prime(array[i]) is True:
                prime_number = True

    if prime_number:
        return True
    return False
