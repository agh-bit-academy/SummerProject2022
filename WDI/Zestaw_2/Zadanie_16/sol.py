# Dominik Adamczyk

def sum_of_digits(num):
    sumNum = 0
    while num != 0:
        sumNum += num % 10
        num //= 10
    return sumNum


def prime_factors_sum(num):
    factorsSum = 0
    numCopy = num
    for factor in range(2, int(num ** 0.5) + 1):
        while num % factor == 0:
            factorsSum += sum_of_digits(factor)
            num //= factor
    # print(num, factorsSum)
    if num != 1 and num != numCopy:
        factorsSum += sum_of_digits(num)
    return factorsSum


def f(num):
    return prime_factors_sum(num) == sum_of_digits(num)
