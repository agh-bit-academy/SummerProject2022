# Karolina Kucia
def composed_of_odds(num):
    if num == 0:
        return False
    elif num < 0:
        num *= -1
    while num > 0:
        if (num % 10) % 2 == 0:
            return False
        num //= 10
    return True


def odd_in_row(tab):
    for num in tab:
        if composed_of_odds(num):
            return True
    return False


def f(A):
    for i in range(len(A)):
        if not odd_in_row(A[i]):
            return False
    return True
