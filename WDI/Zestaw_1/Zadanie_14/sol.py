# Bartłomiej Kozera

DOKLADNOSC = 10**6


def f(x):
    sum = 0
    factorial = 1

    for n in range(DOKLADNOSC):
        if n > 0:
            factorial *= 2*n-1
            factorial *= 2*n
        sum += ((-1)**n*x**(2*n))/factorial

    print(sum)
    return
