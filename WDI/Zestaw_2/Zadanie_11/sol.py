# Krzysztof Wysocki
def is_increasing_number(number):
    if len(str(number)) > 1:
        last_digit = number % 10
        number = number // 10
        while number > 0:
            if last_digit <= number % 10:
                print(False)
                return False
            last_digit = number % 10
            number = number // 10
        print(True)
        return True
    print(False)
    return False
