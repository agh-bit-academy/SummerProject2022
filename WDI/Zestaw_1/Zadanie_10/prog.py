# Szczepan Rzeszutek
# Sebastian Soczawa
def f(num):
    if num == 1:
        print("NIE")
        return
    tmp = num
    s = 1
    i = 2
    while i ** 2 < num:
        if num % i == 0:
            s += i
            s += num // i
        i += 1
    if i ** 2 == num:
        s += i

    if s == tmp:
        print("TAK")
    else:
        print("NIE")
