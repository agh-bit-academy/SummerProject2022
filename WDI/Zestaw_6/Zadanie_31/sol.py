# Sebastian Soczawa
def erastotenes(n):
    sieve = [True for _ in range(n + 1)]
    sieve[0] = False
    if len(sieve) > 1:
        sieve[1] = False
    for i in range(2, int(n ** (0.5)) + 1):
        k = 2 * i
        while k <= n:
            sieve[k] = False
            k += i
    return sieve


def rek(dividers, product, i, no_div):
    if i == no_div:
        if product == 1:
            return 0
        return product
    return rek(dividers, product * dividers[i], i + 1, no_div) +\
        rek(dividers, product, i + 1, no_div)


def f(n):
    primes = erastotenes(n)
    prime_dividers = [None for _ in range(20)]
    j = 0
    for i in range(len(primes)):
        if primes[i] and n % i == 0:
            prime_dividers[j] = i
            j += 1
    return rek(prime_dividers, 1, 0, j)
