# Sebastian Soczawa
def prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    d = 5
    while int(n**0.5) + 1 > d:
        if n % d == 0:
            return False
        d += 2
        if n % d == 0:
            return False
        d += 4
    return True


def rev(n):
    sol = 0
    i = 0
    while n > 0:
        sol = sol * 10 + n % 10
        n //= 10
        i += 1
    return sol


def rec(a, b, number, i):
    if a == 0 and b == 0:
        if prime(number):
            return 1
        return 0
    if a == 0:
        return rec(a, b // 10, number * 10 + b % 10, i + 1)
    if b == 0:
        return rec(a // 10, b, number * 10 + a % 10, i + 1)
    return rec(a // 10, b, number * 10 + a % 10, i + 1) +\
        rec(a, b // 10, number * 10 + b % 10, i + 1)


def f(a, b):
    a = rev(a)
    b = rev(b)
    return rec(a, b, 0, 0)
