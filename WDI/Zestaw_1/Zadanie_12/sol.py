def gdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def f(a, b, c):
    res = gdc(gdc(a, b), c)
    print(res)

