# Bartłomiej Kozera
# Sebastian Soczawa
def f(x):
    a = 2
    while a <= x:
        if x % a == 0:
            # b = x // a
            # return a, b
            return True
        a = 3 * a + 1
    return False
