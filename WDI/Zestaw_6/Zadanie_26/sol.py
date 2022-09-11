# Sebastian Soczawa
def composite(n):
    if n < 4:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return True
    d = 5
    while int(n**0.5) + 1 > d:
        if n % d == 0:
            return True
        d += 2
        if n % d == 0:
            return True
        d += 4
    return False


def bin_to_dec(n):
    dec = 0
    i = 0
    while n > 0:
        dec += (n % 10) * (2 ** i)
        n //= 10
        i += 1
    return dec


def rek(A, B, num):
    if A == 0 and B == 0:
        if composite(bin_to_dec(num)):
            return 1
        return 0
    elif A == 0:
        return rek(A, B - 1, num * 10)
    elif B == 0:
        return rek(A - 1, B, num * 10 + 1)
    else:
        return rek(A - 1, B, num * 10 + 1) +\
            rek(A, B - 1, num * 10)


def f(A, B):
    if A == 0:
        return 0
    return rek(A - 1, B, 1)
