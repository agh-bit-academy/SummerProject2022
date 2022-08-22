# Szymon Ożóg
def check_number(number):
    number = abs(number)
    while number != 0:
        if number % 2 == 0:
            return True
        number //= 10
    return False


def check_row(row):
    for number in row:
        if not check_number(number):
            return False
    return True


def f(A):
    for row in A:
        if check_row(row):
            return True
    return False
