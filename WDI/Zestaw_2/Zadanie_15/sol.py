# Sebastian Soczawa
def f(N):
    for i in range(10 ** (N - 1), 10 ** N):
        tmp = i
        sol = 0
        while tmp != 0:
            sol += (tmp % 10) ** N
            tmp //= 10
        if sol == i:
            print(i, end=" ")
