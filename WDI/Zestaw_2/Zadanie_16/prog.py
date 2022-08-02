# # Paweł Konopka

# def f(mx=1_000_000):
#     # Tutaj wprowadź swój kod
#     pass


# Rozwiązanie tylko do testowania prędkości testów, 
# sol.py pisze ktoś inny

from math import isqrt

APPROX_ERROR = 10 ** (-6)


def sum_cyfr(n):
    rez = 0
    while n > 0:
        rez += (n % 10)
        n //= 10
    return rez


def czynn(licz):
    n = licz
    czynn = []
    temp = 0
    while n % 2 == 0:
        temp += 1
        n //= 2
    if temp > 0:
        czynn.append((2, temp))
    
    for i in range(3, isqrt(licz) + 1, 2):
        temp = 0        
        while n % i == 0:
            temp += 1
            n //= i
        if temp > 0:
            czynn.append((i, temp))
        
        if n == 1:
            break
    if n > 1:
        czynn.append((n, 1))

    return czynn

def sum_cyf_czynn(czyn):
    rez = 0
    
    for cz, krot in czyn:
        rez += sum_cyfr(cz) * krot
    return rez

def is_composite(czyn):
    if len(czyn) >= 2 or len(czyn) == 1 and czyn[0][1] >= 2:
        return True
    return False


def f(mx=1_000_000):
    # if 500_000 < mx < 800_000:
    #     print(2)
    #     return

    for i in range(1, mx):
        czyn = czynn(i)

        if is_composite(czyn) and sum_cyfr(i) == sum_cyf_czynn(czyn):
            print(i)
