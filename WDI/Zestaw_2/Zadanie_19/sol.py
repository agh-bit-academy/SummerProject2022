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

# f(1,7)


def g(a, b):
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
        # print(a // b, end="")
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


g(1, 3000)
