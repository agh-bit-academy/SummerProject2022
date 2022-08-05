def f(s):
    a, b, c, d = 1, 1, 1, 1
    curr = 0
    while a - c <= s:
        if curr < s:
            curr += a
            a, b = b, a + b
        elif curr > s:
            curr -= c
            c, d = d, c + d
        else:
            print(True)
            return
    print(False)

