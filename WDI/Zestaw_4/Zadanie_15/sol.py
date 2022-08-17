def f(T):
    prime_digits = [False, False, True, True, False, True, False, True, False, False]

    for i in range(len(T)):
        row_with_prime_digits = True
        for j in range(len(T)):
            if has_prime_digit(T[i][j], prime_digits) is False:
                row_with_prime_digits = False
                break
        if row_with_prime_digits is True:
            return True
    return False


def has_prime_digit(number, prime_digits):
    while number > 0:
        if prime_digits[number % 10] is True:
            return True
        number //= 10
    return False
