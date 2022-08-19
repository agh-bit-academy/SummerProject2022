#Bartłomiej Kozera
def is_odd(a):
    return True if a % 2 == 1 else False


def f(A):
    pal_len = 0
    for i in range(len(A)):
        if not is_odd(A[i]):
            continue
        tmp_len = 1
        l_id = i - 1
        r_id = i + 1
        while l_id >= 0 and A[l_id] == A[i]:
            l_id -= 1
            tmp_len += 1
        while r_id < len(A) and A[r_id] == A[i]:
            r_id += 1
            tmp_len += 1
        while l_id >= 0 and r_id < len(A) and is_odd(A[l_id]) and A[r_id] == A[l_id]:
            l_id -= 1
            r_id += 1
            tmp_len += 2
        pal_len = max(pal_len, tmp_len)
    return pal_len
