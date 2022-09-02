# Bartłomiej Kozera
def bin_2_dec(tab):
    poww = len(tab) - 1
    summ = 0
    for el in tab:
        if el == 1:
            summ += 2 ** poww
        poww -= 1
    return summ


def is_prime(x):
    if x < 2:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    d = 5
    while int(x**0.5) + 1 > d:
        if x % d == 0:
            return False
        d += 2
        if x % d == 0:
            return False
        d += 4
    return True


def f(A):
    if rec(A):
        return True
    return False


def rec(A, start=0, stop=1):
    num = bin_2_dec(A[start:stop])
    flag = is_prime(num)
    while not flag and stop != len(A) and stop - start < 30:
        stop += 1
        num = bin_2_dec(A[start:stop])
        flag = is_prime(num)
    if stop == len(A):
        if flag and start != 0:
            return True
        return False
    else:
        if flag:
            return rec(A, stop, stop + 1) or rec(A, start, stop + 1)
        else:
            return rec(A, start, stop + 1)
