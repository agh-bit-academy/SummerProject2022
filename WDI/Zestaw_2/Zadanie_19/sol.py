# Dominik Adamczyk
# Rozwiązanie wystarczające na WDI, o złożoności O(n^2),
# gdzie n to liczba cyfr po przecinku w zapisie dziesiętnym okresowym.
# Rozwiązanie liniowe wymaga użycia zbiorów - zakazanych na WDI

def f(a, b):
    print(a // b, end="")
    print(".", end="")
    flag = True
    period_start_idx = float("inf")
    period_end_idx = float("inf")
    a_cp = a
    a %= b
    a *= 10
    idx = 0
    while flag:
        idx += 1
        a_second = a_cp
        a %= b
        a *= 10
        for i in range(idx):
            a_second %= b
            a_second *= 10
            if a == a_second:
                period_start_idx = i
                period_end_idx = idx
                flag = False
                break

    a = a_cp
    a %= b
    a *= 10
    for i in range(period_end_idx):
        if i == period_start_idx:
            print("(", end="")
        print(a // b, end="")
        a %= b
        a *= 10

    print(")", end="")
