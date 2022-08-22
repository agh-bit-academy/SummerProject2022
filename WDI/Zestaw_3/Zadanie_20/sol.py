# Karol Sewiło
def f(t):
    n = len(t)
    if n == 0:
        return 0

    array_of_divisors = [divisors(t[i]) for i in range(n)]

    highest_absolute_number = float("-inf")
    for number in t:
        highest_absolute_number = max(highest_absolute_number, abs(number))

    result = 0
    for i in range(n):
        result = max(count_longest_subsequence(i, array_of_divisors, t, highest_absolute_number), result)

    return result


def count_longest_subsequence(i, array_of_divisors, t, highest_number):
    positive_divisors = [False for _ in range(highest_number + 1)]
    negative_divisors = [False for _ in range(highest_number + 1)]
    counter = 0

    for j in range(i, len(t)):
        if len(array_of_divisors[j]) == 0 or t[j] == 0:
            return counter

        if t[j] < 0:
            negative = True
        else:
            negative = False

        for divisor in array_of_divisors[j]:

            if divisor == 0:
                break

            if positive_divisors[divisor] is True:
                return counter
            positive_divisors[divisor] = True

            if negative:
                if negative_divisors[divisor] is True:
                    return counter
                negative_divisors[divisor] = True

        counter += 1
    return counter


def divisors(number):
    number = abs(number)
    i = 2
    array_of_divisors = [0 for _ in range(int((number ** 0.5) + 1))]
    index = 0
    while number > 1 and i ** 2 <= number:
        if number % i == 0:
            if len(array_of_divisors) != 0 and i == array_of_divisors[-1]:
                return []
            array_of_divisors[index] = i
            index += 1
            number //= i
        else:
            i += 1
    if number > 1:
        if len(array_of_divisors) != 0 and array_of_divisors[-1] == number:
            return []
        array_of_divisors[index] = number

    return array_of_divisors
