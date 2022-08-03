# Krzysztof Mach
APPROX_ERROR = 10 ** (-6)


def f(num):
    a, b = 1, num
    while abs(a - b) > APPROX_ERROR:
        a, b = (a + b) / 2, num / ((a + b) / 2)
    print((a + b) / 2)
