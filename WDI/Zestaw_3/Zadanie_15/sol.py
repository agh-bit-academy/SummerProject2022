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
            if isPrime(array[i]) == True:
                return False
        else:
            if isPrime(array[i]) == True:
                primeNumber = True
    
    if primeNumber:
        return True
    return False
#    0  1  2  3  4  5  6  7  8
A = [4, 6, 10,8, 1, 6, 6, 5, 6]
print(f(A))
