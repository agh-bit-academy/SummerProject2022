# Krzysztof Wysocki
def nwd(a, b):
    while b:
        a, b = b, a % b
    return a


def nww(a, b):
    ans = a * b // nwd(a, b)
    return ans


def NWWWa(a, b, c):
    return nww(nww(a, b), c)
