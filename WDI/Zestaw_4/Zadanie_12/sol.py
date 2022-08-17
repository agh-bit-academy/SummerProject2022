# Maciej Sieniek
def is_complex(x):
    if x == 1:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return True
        i += 1
    return False


def f(T):
    n = len(T)
    last_level = 0
    for i in range(n):
        curr_level = 0
        for j in range(1, n - 1):
            for k in range(1, n - 1):
                curr_el = 0
                for a in range(-1, 2):
                    for b in range(-1, 2):
                        if a == b == 0:
                            continue
                        if is_complex(T[i][j + a][k + b]):
                            curr_el += 1
                if curr_el > 5:
                    curr_level += 1
        if i > 0 and last_level != curr_level:
            return False
        last_level = curr_level
    return True
