# Maciej Bartczak
from math import sqrt


def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x < 2 or x % 2 == 0 or x % 3 == 0:
        return False

    factor = 5
    while factor < int(sqrt(x)) + 1:
        if x % factor == 0 or x % (factor + 2) == 0:
            return False
        factor += 6
    return True


def f(A, B):
    a_length = len(A)
    b_length = len(B)
    common_length = min(a_length, b_length)
    max_length = max(a_length, b_length)
    longer = A
    if b_length > a_length:
        longer = B

    valid_sum_counter = 0
    for mask in range(0, 3 ** common_length):
        result = 0
        index = 0
        while index < common_length:
            digit = mask % 3
            mask //= 3
            if digit == 0:
                result += A[index]
            elif digit == 1:
                result += B[index]
            elif digit == 2:
                result += A[index] + B[index]
            index += 1
        while index < max_length:
            result += longer[index]
            index += 1
        if is_prime(result):
            valid_sum_counter += 1
    return valid_sum_counter
