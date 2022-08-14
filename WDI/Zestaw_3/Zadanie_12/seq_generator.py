from random import randint


# Generates tuple of numbers containing many arithmetic sequences
def generate_test(a: int, b: int, n: int, r: int, seq_ammount: int) -> tuple:
    t = [0] * n
    for i in range(seq_ammount):
        v = randint(0, n - 1)
        t[v] = randint(-r, r)
    t[0] = 1
    for i in range(1, n):
        if t[i] == 0:
            t[i] = t[i - 1]
        if t[i] != t[i - 1]:
            t[i] += randint(a, b)
    t[0] += randint(a, b)
    for i in range(1, n):
        t[i] += t[i - 1]
    return tuple(t)
