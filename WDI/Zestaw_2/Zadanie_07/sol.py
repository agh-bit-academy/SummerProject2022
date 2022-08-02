def f(x):
    i = 1
    a_n = 3
    while a_n <= x:
        if x % a_n == 0:
            print(True)
            return
        i += 1
        a_n = i * i + i + 1
    print(False)
    return
