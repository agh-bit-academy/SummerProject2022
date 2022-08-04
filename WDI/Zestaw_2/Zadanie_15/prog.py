#Szczeapan Rzeszutek
from math import log10


def f(num):
    def leng(num):
        return int(log10(num)) + 1

    l = leng(num)
    sum = 0
    numCp = num
    while num > 0:
        sum += (num % 10) ** l
        num //= 10
    return sum == numCp