# Izabella Rosikoń
def count_one(num):
    sum = 0
    while num != 0:
        sum += num % 2
        num //= 2
    return sum


def f(T, i=0, sum1=0, sum2=0, sum3=0):
    if i == len(T):
        if sum1 == sum2 == sum3 != 0:
            return True
        return False
    a = f(T, i + 1, sum1 + count_one(T[i]), sum2, sum3)
    b = f(T, i + 1, sum1, sum2 + count_one(T[i]), sum3)
    c = f(T, i + 1, sum1, sum2, sum3 + count_one(T[i]))
    if a or b or c:
        return True
    return False
