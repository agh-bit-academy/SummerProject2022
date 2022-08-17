# Karol Sewiło
def f(t):
    n = len(t)
    array_of_divisors = [divisors(t[i]) for i in range(n)]

    result = 0
    for i in range(n):
        result = max(count_longest_subsequence(i, array_of_divisors, n), result)
    return result


def count_longest_subsequence(i, array_of_divisors, n):
    array = [False for _ in range(1000)]
    counter = 0
    for j in range(i, n):
        if len(array_of_divisors[j]) == 0:
            return counter
        for nr in array_of_divisors[j]:
            if array[nr] is True:
                return counter
            array[nr] = True
        counter += 1
    return counter


def divisors(number):
    i = 2
    array = []
    while number > 1 and i ** 2 <= number:
        if number % i == 0:
            if len(array) != 0 and i == array[-1]:
                return []
            array.append(i)
            number //= i
        else:
            i += 1
    if number > 1:
        if len(array) != 0 and array[-1] == number:
            return []
        array.append(number)
    return array
