# Radek Niżnik


def f(tab):
    n = len(tab)
    m = len(tab[0])
    for i in range(n):
        flag = True
        for j in range(m):
            if not odd(tab[i][j]):
                flag = False
                break
        if flag:
            return True

    return False


def odd(n):
    n = abs(n)
    while n != 0:
        if n % 10 % 2 == 0:
            return True
        n //= 10
    return False