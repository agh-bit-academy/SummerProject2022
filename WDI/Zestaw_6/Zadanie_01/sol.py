# Karol Sewiło
def is_prime(number):
    if number == 2 or number == 3:
        return True
    if number <= 1 or number % 2 == 0 or number % 3 == 0:
        return False
    for i in range(6, int(number ** 0.5 + 1), 6):
        if number % (i - 1) == 0 or number % (i + 1) == 0:
            return False
    return True


def find_prime_numbers(number, array, new_number=0, p=0, one_digit_deleted=False):
    if number == 0:
        if new_number > 9 and is_prime(new_number) and one_digit_deleted:
            array.append(new_number)
        return
    find_prime_numbers(number // 10, array, new_number + (number % 10) * (10 ** p), p + 1, one_digit_deleted)
    find_prime_numbers(number // 10, array, new_number, p, True)


def f(number):
    if number <= 10:
        return []

    array = []
    find_prime_numbers(number, array)

    return array
