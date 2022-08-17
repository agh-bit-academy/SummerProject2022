# Dominik Adamczyk

def f(T):
    lencol = len(T)
    lenrow = len(T[0])
    counter = 0
    digits = [[[False] * 10 for _ in range(lenrow)] for _ in range(lencol)]
    for y in range(lencol):
        for x in range(lenrow):
            num = T[y][x]
            while num != 0:
                digits[y][x][num % 10] = True
                num //= 10

    for y in range(lencol):
        for x in range(lenrow):
            if x != 0 and digits[y][x] != digits[y][x - 1]:
                continue
            if y != 0 and digits[y][x] != digits[y - 1][x]:
                continue
            if x != lenrow - 1 and digits[y][x] != digits[y][x + 1]:
                continue
            if y != lencol - 1 and digits[y][x] != digits[y + 1][x]:
                continue
            counter += 1
    return counter
