# Krzysztof Mach
def f(a, b):
    for i in range(2, 17):
        if different_digits_in_base(a, b, i):
            return i
    return False


def different_digits_in_base(a, b, base):
    digits = [[False for j in range(base)] for i in range(2)]

    for i, num in enumerate((a, b)):
        while num:
            currDigit = num % base
            digits[i][currDigit] = True
            num //= base

    for i in range(base):
        if digits[0][i] and digits[1][i]:
            return False

    return True
