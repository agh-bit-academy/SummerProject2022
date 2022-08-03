# Bartłomiej Kozera


def f(num):
    low, high = 1, num

    while abs(low - high) >= 10**(-6):
        low = (low + high) / 2
        high = num/low
    print((low + high) / 2)
