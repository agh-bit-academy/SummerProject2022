# Szymon Rusiecki
def f():
    a, b = 0, 1
    print(a)
    print(b)
    while b < 10 ** 6:
        a, b = b, a + b
        print(b)
    return
