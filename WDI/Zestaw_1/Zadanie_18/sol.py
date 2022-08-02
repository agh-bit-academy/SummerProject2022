# Paweł Konopka

SET_PRECISION = 10 ** (-9)


def f(k):
    a, b, c = k, k, 1 / k
    while abs(a - c) > SET_PRECISION:
        a = (a + c) / 2
        b = a
        c = k / (a * a)

    return (a + b + c) / 3
