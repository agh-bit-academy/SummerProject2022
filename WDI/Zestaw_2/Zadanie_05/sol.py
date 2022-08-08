def decimal_to_binary(number):
    k = 0
    decimal_nr = 0
    while number > 0:
        decimal_nr += (number % 2) * (10 ** k)
        k += 1
        number //= 2
    return decimal_nr


def count_if_can_be_divided(number, bit_mask, divisor, length):
    new_number = 0
    k = 0
    for _ in range(length):
        if bit_mask % 10 == 1:
            new_number += (number % 10) * (10 ** k)
            k += 1
        bit_mask //= 10
        number //= 10
    if new_number % divisor == 0:
        return 1
    else:
        return 0


def f(number, divisor):

    if number == 0:
        print(1)
        return

    number = abs(number)
    divisor = abs(divisor)
    temp_number = number
    length = 0
    counter = 0

    while temp_number > 0:
        length += 1
        temp_number //= 10

    for i in range(1, 2**length):
        counter += count_if_can_be_divided(number, decimal_to_binary(i), divisor, length)
    print(counter)
