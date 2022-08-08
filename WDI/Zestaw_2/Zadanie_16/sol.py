# Dominik Adamczyk

def sum_of_digits(num):
    sum_num = 0
    while num != 0:
        sum_num += num % 10
        num //= 10
    return sum_num


def prime_factors_sum(num):
    factors_sum = 0
    num_copy = num
    for factor in range(2, int(num ** 0.5) + 1):
        while num % factor == 0:
            factors_sum += sum_of_digits(factor)
            num //= factor
    if num != 1 and num != num_copy:
        factors_sum += sum_of_digits(num)
    return factors_sum


def f(num):
    return prime_factors_sum(num) == sum_of_digits(num)
