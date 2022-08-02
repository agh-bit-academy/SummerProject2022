# Paweł Konopka


def f(k):
    eps = 10 ** (-6)

    a, b, c = k, k, 1 / k
    while abs(a - c) > eps:
        a = (a + c) / 2
        b = a
        c = k / (a * a)

    return (a + b + c) / 3
