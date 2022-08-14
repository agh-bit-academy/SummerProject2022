# Mikołaj Maślak
def f(A):
    max_asc_len = 0
    asc_len = 0
    max_desc_len = 0
    desc_len = 0
    prev = 0
    for i in range(1, len(A)):
        diff = A[i] - A[i - 1]
        if diff > 0:
            if diff == prev:
                asc_len += 1
            else:
                asc_len = 2
                desc_len = 0
        elif diff < 0:
            if diff == prev:
                desc_len += 1
            else:
                desc_len = 2
                asc_len = 0
        max_asc_len = max(max_asc_len, asc_len)
        max_desc_len = max(max_desc_len, desc_len)
        prev = diff
    return max_asc_len - max_desc_len
