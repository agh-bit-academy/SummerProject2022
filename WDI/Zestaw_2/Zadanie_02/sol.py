# Szczepan Rzeszutek
def f(a, b, n):
    print(a // b, "." if a % b != 0 else "", sep="", end="")
    a %= b
    while a > 0 and n > 0:
        a *= 10
        print(a // b, end="")
        a %= b
        n -= 1
