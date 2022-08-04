def f():
    def sumOfDiv(num):
        s = 1
        i = 2
        while i ** 2 < num:
            if num % i == 0:
                s += i
                s += num // i
            i += 1
        if i ** 2 == num:
            s += i

        return s

    for num in range(4, 1000000):
        if sumOfDiv(num) == num:
            print(num)
