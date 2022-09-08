# Izabella Rosikoń
def count_one(num):
    sum = 0
    while num != 0:
        sum += num % 2
        num //= 2
    return sum


def f(T, i=0, sum1=0, sum2=0, sum3=0):
    if sum1 == sum2 == sum3 != 0:
        return True
    if i == len(T):
        return False
    if f(T, i+1, sum1 + count_one(T[i]), sum2, sum3) or f(T, i+1, sum1, sum2+count_one(T[i]), sum3) or f(T, i+1, sum1, sum2, sum3 + count_one(T[i])):
        return True
    return False
