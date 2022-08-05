# Krzysztof Mach
def f(a, b, num=''):
    if not a and not b:
        return 1 if is_prime(int(num)) else 0

    total = 0

    if b:
        currDigit = b % 10
        total += f(a, b // 10, str(currDigit) + num)
    if a:
        currDigit = a % 10
        total += f(a // 10, b, str(currDigit) + num)

    return total


def is_prime(num):
    if num == 2:
        return True
    if num == 1 or num % 2 == 0:
        return False

    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True
