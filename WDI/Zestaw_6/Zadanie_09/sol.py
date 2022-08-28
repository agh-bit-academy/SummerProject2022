# Juliusz Wasieleski
def f(tab, k):
    summ = 0
    weights = []
    for weight in tab:
        summ += weight
        weights.append(weight)
        if summ == k:
            return weights
        elif summ > k:
            weights = []
            if rek(tab, weights, k):
                return weights
            return []
    return []


def rek(A, weights, left, right=0, i=0):
    if left == right and i != 0:
        return True
    if i == len(A):
        return False
    tmp_bool = rek(A, weights, left, right + A[i], i + 1) or rek(A, weights, left + A[i], right, i + 1)
    if tmp_bool:
        weights.append(A[i])
    return tmp_bool or rek(A, weights, left, right, i + 1)

