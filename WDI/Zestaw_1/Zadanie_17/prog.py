# Krzysztof Mach
ITERATIONS = 10 ** 3


def f():
    ratio = 1
    a, b = 1, 1
    for i in range(ITERATIONS):
        a, b = b, a + b
        ratio = (ratio + b / a) / 2
    print(ratio)
