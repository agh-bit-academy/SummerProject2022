# Izabella Rosikoń
def unique_digit(num):
    lastDigit = num % 10
    num //= 10
    while num > 0:
        if num % 10 == lastDigit:
            return False
        num //= 10
    return True
