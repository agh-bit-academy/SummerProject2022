# Bartłomiej Kozera
from math import sqrt


def is_prime(x):
    if x < 2:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
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
    for i in range(n):
        for j in range(n):
            flag = False
            for y in range(n):
                for x in range(n):
                    if A[y][x] == 0 or (i == y and j == x):
                        continue
                    act_num = A[i][j] + A[y][x]
                    print(act_num)
                    if is_prime(act_num):
                        flag = True
                        break
            if not flag:
                A[i][j] = 0
    return A
