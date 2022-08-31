# Sebastian Soczawa
def weight(T, left=0, right=0, i=0):
    if left == right:
        return True
    elif i >= len(T):
        return False
    return weight(T, left + T[i], right, i + 1) or \
        weight(T, left, right + T[i], i + 1) or \
        weight(T, left, right, i + 1)


def f(T, k):
    return weight(T, k)
