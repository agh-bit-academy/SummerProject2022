# Andrzej Karciński 

def isPrime(x):
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
    primeNumber = False

    if isPrime(array[0]):
        return False

    for i in range(len(array)):
        if i == a:
            a, b = b, c
            c = a + b
            if isPrime(array[i]) is True:
                return False
        else:
            if isPrime(array[i]) is True:
                primeNumber = True

    if primeNumber:
        return True
    return False
