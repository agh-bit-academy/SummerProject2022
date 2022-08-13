# Sebastian Soczawa
# Program nie działa poprawnie (niektóre wyniki są liczone podwójnie)
# jeśli cyfry w liczbach m i n powtarzają się jakieś cyfry,
# ale nie mam pojęcia jak poradzić sobie z tym bez tablic :(
# Rekurencyjne rozwiązanie w prog.pty też tego nie wyłapuje
from math import log10


def prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 6
    while i-1 <= int(n ** 0.5)+1:
        if n % (i-1) == 0:
            return False
        if n % (i + 1) == 0:
            return False
        i += 6
    return True


# korzystam z maski bitowej np 13 to 1101, 1 : biorę cyfrę z pierwszej liczby, 0 : z drugiej
# jednocześnie tworzę liczby dla maski i NOT maska, czyli 1101 i 0010, w ten sposób sprawdzam
# wszystkie możliwości utworzenia liczby z zadania
def createNumber(m, n, mask, counter):
    number1 = 0
    number2 = 0
    n1, m1 = n, m
    n2, m2 = n, m
    i = 0
    while mask > 0:
        if mask % 2:
            number1 += (n1 % 10) * (10 ** i)
            number2 += (m2 % 10) * (10 ** i)
            n1 //= 10
            m2 //= 10
        else:
            number1 += (m1 % 10) * (10 ** i)
            number2 += (n2 % 10) * (10 ** i)
            m1 //= 10
            n2 //= 10
        mask //= 2
        i += 1
    if m1 == 0 and n1 == 0 and prime(number1):
        counter += 1
    if m2 == 0 and n2 == 0 and prime(number2):
        counter += 1
    return counter


def f(n, m):
    length = int(log10(n)) + int(log10(m)) + 2
    counter = 0
    for i in range(2**(length - 1), 2**length):
        counter = createNumber(m, n, i, counter)
    return counter
