# Krzysztof Wysocki
def f(number):
    if len(str(number)) > 1:
        last_digit = number % 10
        number = number // 10
        while number > 0:
            if last_digit <= number % 10:
                return False
            last_digit = number % 10
            number = number // 10
        return True
    return False
