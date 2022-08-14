# Dominik Adamczyk
def f(A):
    for el in A:
        are_digits_odd = True
        while el != 0:
            if el % 2 == 0:
                are_digits_odd = False
                break
            el //= 10
        if are_digits_odd:
            return True
    return False
