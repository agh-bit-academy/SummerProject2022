# Bartłomiej Kozera
from math import sqrt


def is_prime(x):
    if x < 2:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 and x % 3 == 0:
        return False
    factor = 5
    while factor < sqrt(x) + 1:
        if x % factor == 0:
            return False
        factor += 2
        if x % factor == 0:
            return False
        factor += 4
    return True


def f(A):
    n = len(A)
    num_of_elems = n ** 2
    i = 0
    while i < num_of_elems:
        flag = False
        for y in range(n):
            for x in range(n):
                if i // n == y and i % n == x:
                    continue
                act_num = A[i // n][i % n] + A[y][x]
                if is_prime(act_num):
                    flag = True
                    break
        if not flag:
            A[i // n][i % n] = 0
        i += 1
    return A
