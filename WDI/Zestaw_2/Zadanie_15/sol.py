# Sebastian Soczawa
def f(n):
    for i in range(10 ** (n - 1), 10 ** n):
        tmp = i
        sol = 0
        while tmp != 0:
            sol += (tmp % 10) ** n
            tmp //= 10
        if sol == i:
            print(i, end=" ")
