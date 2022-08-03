# Kacper Słoniec

def f():
    YEAR = 2022
    for sum in range(2, YEAR):
        for a in range (1, sum):
            a_start = a
            b_start = sum-a
            if a_start > b_start:
                continue
            x = a_start
            y = b_start
            while x <= YEAR:
                if x == YEAR:
                    print(a_start, b_start)
                    return
                x, y = y, x + y