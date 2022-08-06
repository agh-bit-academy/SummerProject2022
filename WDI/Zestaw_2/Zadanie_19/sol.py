# Dominik Adamczyk
# Rozwiązanie nieoptymalne, potencjalnie O(n^2),
# gdzie n to suma liczby cyfr po przecinku w zapisie dziesiętnym okresowym.
# Rozwiązanie liniowe wymaga użycia zbiorów - zakazanych na WDI

def f(a, b):
    print(a // b, end="")
    print(".", end="")
    flag = True
    periodStartIdx = float("inf")
    periodEndIdx = float("inf")
    aCopy = a
    a %= b
    a *= 10
    idx = 0
    while flag:
        idx += 1
        aSecond = aCopy
        a %= b
        a *= 10
        for i in range(idx):
            aSecond %= b
            aSecond *= 10
            if a == aSecond:
                periodStartIdx = i
                periodEndIdx = idx
                flag = False
                break

    a = aCopy
    a %= b
    a *= 10
    for i in range(periodEndIdx):
        if i == periodStartIdx:
            print("(", end="")
        print(a // b, end="")
        a %= b
        a *= 10

    print(")", end="")
