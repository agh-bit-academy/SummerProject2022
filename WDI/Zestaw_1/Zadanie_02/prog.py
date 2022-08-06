# Kacper Słoniec
def f():
    year = 2022
    for sum in range(2, year):
        for a in range(1, sum):
            a_start = a
            b_start = sum-a
            if a_start > b_start:
                continue
            x = a_start
            y = b_start
            while x <= year:
                if x == year:
                    print(a_start, b_start)
                    return
                x, y = y, x + y
