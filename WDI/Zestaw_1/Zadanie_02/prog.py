# Kacper Słoniec

def f():
    YEAR = 2022
    for sum in range(2, YEAR):
        for a in range (1, sum):
            a_start = a
            b_start = sum-a
            a = a_start
            b = b_start
            while a <= YEAR:
                if a == YEAR:
                    print(a_start, b_start)
                    exit()
                a, b = a + b, a