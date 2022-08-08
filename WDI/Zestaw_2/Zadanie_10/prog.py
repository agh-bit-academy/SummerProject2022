# Krzysztof Mach
def f(num):
    a = 2
    while a <= num:
        if num % a == 0:
            return True
        a = 3 * a + 1
    return False
