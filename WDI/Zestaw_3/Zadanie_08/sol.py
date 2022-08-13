# Maciej Sieniek
def getPrimeFactors(b, x, i, n):
    j = 2
    while j <= x:
        if x % j == 0 and i + j < n:
            b[i + j] = True
            while x % j == 0:
                x //= j
        j += 1


def f(T):
    n = len(T)
    bools = [False for _ in range(n)]
    bools[0] = True
    for i in range(n):
        if bools[i]:
            getPrimeFactors(bools, T[i], i, n)
    return bools[n - 1]
