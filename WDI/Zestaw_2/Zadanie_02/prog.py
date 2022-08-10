# Sebastian Soczawa
def f(a, b, n):
    # tutaj wpisz swoje rozwiązanie
    if a % b == 0:
        print(a // b)
        return
    print(a // b, ".", sep="", end="")
    for _ in range(n):
        a %= b
        if a == 0:
            return
        a *= 10
        print(a // b, sep="", end="")
