# Mikołaj Maślak
def f(n):
    two = 1
    three = 1
    five = 1
    product = 1
    res = 0

    while product <= n:
        if product * 2 <= n:
            two *= 2
            product *= 2
        else:
            two = 1
            product = three * five
            if product * 3 <= n:
                three *= 3
                product *= 3
            else:
                three = 1
                five *= 5
                product = five
        res += 1
    return res
