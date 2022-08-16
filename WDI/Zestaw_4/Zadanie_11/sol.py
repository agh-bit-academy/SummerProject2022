# Dominik Adamczyk

def f(T):
    lent = len(T)
    counter = 0
    digits = [[[False] * 10 for _ in range(lent)] for _ in range(lent)]
    for y in range(lent):
        for x in range(lent):
            num = T[y][x]
            while num != 0:
                digits[y][x][num % 10] = True
                num //= 10

    for y in range(lent):
        for x in range(lent):
            if x != 0 and digits[y][x] != digits[y][x - 1]:
                continue
            if y != 0 and digits[y][x] != digits[y - 1][x]:
                continue
            if x != lent - 1 and digits[y][x] != digits[y][x + 1]:
                continue
            if y != lent - 1 and digits[y][x] != digits[y + 1][x]:
                continue
            counter += 1
    return counter
