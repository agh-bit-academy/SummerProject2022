def f(a, b):
    print(a // b, end="")
    print(".", end="")
    flag = True
    flag1 = True
    secondFlag = False
    aCopy = float("inf")
    # print(a, b)
    a %= b
    a *= 10
    while True:
        if flag:
            aCopy = a
            for _ in range(b):
                aCopy %= b
                aCopy *= 10
                if aCopy == a:
                    flag = False
                    break
        if aCopy == a and not flag and flag1:
            print("(", end="")
            flag1 = False
            secondFlag = True
        print(a // b, end="")
        a %= b
        a *= 10
        if aCopy == a and secondFlag:
            print(")", end="")
            break

f(1,7)