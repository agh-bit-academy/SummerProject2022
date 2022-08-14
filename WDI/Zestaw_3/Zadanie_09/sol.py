# Sebastian Soczawa
def f(A):
    len_a = len(A)
    if len_a == 0:
        return 0
    max_len = 1
    i = 0
    while i < len_a - 1:
        curr_len = 1
        while i < len_a - 1 and A[i] < A[i + 1]:
            curr_len += 1
            i += 1
        max_len = max(max_len, curr_len)
        i += 1
    return max_len
