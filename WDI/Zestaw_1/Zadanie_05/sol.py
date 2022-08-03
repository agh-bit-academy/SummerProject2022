# Krzysztof Mach


def f(num):
    a, b = 1, num
    while abs(a - b) > 10 ** (-6):
        a, b = (a + b) / 2, num / ((a + b) / 2)
    print((a + b) / 2)
