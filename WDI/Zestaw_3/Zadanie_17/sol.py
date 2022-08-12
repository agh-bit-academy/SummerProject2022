# Maciej Bartczak
def f(A, B):
    length = len(A)
    valid_sum_counter = 0
    for mask in range(0, 3 ** length):
        result = 0
        index = 0
        while index < length:
            digit = mask % 3
            mask //= 3
            if digit == 0:
                result += A[index]
            elif digit == 1:
                result += B[index]
            elif digit == 2:
                result += A[index] + B[index]
            index += 1
        is_prime = True
        for divisor in range(2, result):
            if result % divisor == 0:
                is_prime = False
                break
        if is_prime:
            valid_sum_counter += 1
    return valid_sum_counter
