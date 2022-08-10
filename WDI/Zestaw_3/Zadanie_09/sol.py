# Sebastian Soczawa
def f(A):
    lenA = len(A)
    if len == 0:
        return 0
    maxLen = 1
    i = 0
    while i < lenA - 1:
        currLen = 1
        while i < lenA - 1 and A[i] < A[i + 1]:
            currLen += 1
            i += 1
        maxLen = max(maxLen, currLen)
        i += 1
    return maxLen
