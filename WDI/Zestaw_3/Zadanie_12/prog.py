# Sebastian Soczawa
def f(A):
    maxAscendingLen = 0
    maxDescendingLen = 0
    i = 1
    while i < len(A):
        ascLen = 1
        descLen = 1
        r = A[i] - A[i - 1]
        if r > 0:
            while i < len(A) and A[i] - A[i - 1] == r:
                ascLen += 1
                i += 1
            maxAscendingLen = max(ascLen, maxAscendingLen)
        elif r < 0:
            while i < len(A) and A[i] - A[i - 1] == r:
                descLen += 1
                i += 1
            maxDescendingLen = max(descLen, maxDescendingLen)
        else:
            i += 1
    return maxAscendingLen - maxDescendingLen
