# Kacper Słoniec


def isPrime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    i = 3
    while i**2 <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def f(arr):
    ramainingPrime = False
    a = 1
    b = 1

    if isPrime(arr[0]):
        ramainingPrime = True

    while b < len(arr):
        if isPrime(arr[b]):
            return False
        if not ramainingPrime:
            for i in range(a + 1, b):
                if isPrime(arr[i]):
                    ramainingPrime = True
                    break
        a, b = b, a + b

    if not ramainingPrime:
        for i in range(a + 1, len(arr)):
            if isPrime(arr[i]):
                ramainingPrime = True
                break

    return ramainingPrime
