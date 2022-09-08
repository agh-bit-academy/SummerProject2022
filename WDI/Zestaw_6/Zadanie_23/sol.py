# Sebastian Soczawa
def rek(T, R, res, count, i):
    if count == 3:
        if res == R:
            print(i)
            return True
        return False
    if i == len(T):
        return False
    r_serial = res + T[i]
    if count == 0:
        r_parallel = T[i]
    else:
        r_parallel = (res * T[i]) / (res + T[i])
    return rek(T, R, r_serial, count + 1, i + 1) or \
        rek(T, R, r_parallel, count + 1, i + 1) or \
        rek(T, R, res, count, i + 1)


def f(T, R):
    return rek(T, R, 0, 0, 0)
