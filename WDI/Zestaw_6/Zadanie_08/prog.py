# Bartłomiej Kozera
def f(A, k):
    summ = 0
    for el in A:
        summ += el
        if summ == k:
            return True
        elif summ > k:
            if rek(A, k):
                return True
            return False
    return False


def rek(A, left, right=0, i=0):
    if left == right and i != 0:
        return True
    if i == len(A):
        return False
    return rek(A, left, right + A[i], i + 1) or rek(A, left, right, i + 1)\
         or rek(A, left + A[i], right, i + 1)
