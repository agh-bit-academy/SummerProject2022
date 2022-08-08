# Krzysztof Mach


def f(num):
    a, b = 1, 1
    while a <= num:
        tempA, tempB = a, b

        while tempB <= num:
            if a * tempB == num:
                return True
            tempA, tempB = tempB, tempA + tempB

        a, b = b, a + b
    return False
