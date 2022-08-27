# Andrzej Karciński
def sum_divisors(x):
    sum = 1
    i = 2
    while i ** 2 < x:
        if x % i == 0:
            sum += i
            sum += (x // i)
        i += 1
    if i ** 2 == x:
        sum += i
    return sum


def f(n, m):
    m_divisors = sum_divisors(m)
    n_divisors = sum_divisors(n)
    if m_divisors == n and n_divisors == m:
        print("True")
    else:
        print("False")
