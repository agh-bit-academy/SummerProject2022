# Dominik Adamczyk

def f(A):
    for el in A:
        areDigitsOdd = True
        while el != 0:
            if el % 2 == 0:
                areDigitsOdd = False
                break
            el //= 10
        if areDigitsOdd:
            return True
    return False
