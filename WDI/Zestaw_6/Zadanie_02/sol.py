# Bartłomiej Kozera
def weight_count(x):
    if x == 1:
        return 0
    weight = 0
    divisor = 2
    while x > 1 and divisor < x // 2:
        if x % divisor == 0:
            weight += 1
            while x % divisor == 0:
                x //= divisor
        divisor += 1
    return weight


def f(A):
    n = len(A)
    weight_tab = [0 for _ in range(n)]
    sum = 0
    for i in range(n):
        weight_tab[i] = weight_count(A[i])
        sum += weight_tab[i]
    if sum % 3 != 0:
        return False
    if rec(weight_tab):
        return True
    return False


def rec(tab, i=0, s1=0, s2=0, s3=0):
    if i == len(tab):
        return s1 == s2 and s2 == s3
    return rec(tab, i + 1, s1 + tab[i], s2, s3) or rec(tab, i + 1, s1, s2 + tab[i], s3)\
         or rec(tab, i + 1, s1, s2, s3 + tab[i])
