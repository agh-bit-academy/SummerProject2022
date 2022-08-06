# Krzysztof Mach
def f():
    ratio = 1
    a, b = 1, 1
    for i in range(10 ** 3):
        a, b = b, a + b
        ratio = (ratio + b / a) / 2
    print(ratio)
