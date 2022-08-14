# Radek Niżnik

def f(n):
    surface = 0
    step = (n - 1) / 10000000
    for i in range(10000001):
        surface += step / (1 + i * step)
    return surface
