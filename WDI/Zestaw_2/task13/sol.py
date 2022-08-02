N = int(input())

def unique_digit(num):
    last_digit = num % 10
    num //= 10
    while num > 0:
        if num % 10 == last_digit:
            return False
        num //= 10
    return True

print(unique_digit(N))