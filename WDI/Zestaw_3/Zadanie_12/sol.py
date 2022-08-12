# Mikołaj Maślak
def f(A):
    maxAscLen = 0
    ascLen = 0
    maxDescLen = 0
    descLen = 0
    prev = 0
    for i in range(1, len(A)):
        diff = A[i] - A[i - 1]
        if diff > 0:
            if diff == prev:
                ascLen += 1
            else:
                ascLen = 2
                descLen = 0
        elif diff < 0:
            if diff == prev:
                descLen += 1
            else:
                descLen = 2
                ascLen = 0
        maxAscLen = max(maxAscLen, ascLen)
        maxDescLen = max(maxDescLen, descLen)
        prev = diff
    return maxAscLen - maxDescLen
