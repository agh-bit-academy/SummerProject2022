# Karolina Kucia
def f(n):
    add = [0 for _ in range(n + 1)]
    add[0] = 1
    mul = [0 for _ in range(n + 1)]
    mul[0] = 1
    i = 1
    while max(mul) > 0:
        rest = 0
        tmp = 0
        for j in range(n, -1, -1):
            tmp = add[j] + mul[j] + rest
            rest = tmp // 10
            add[j] = tmp % 10
        i += 1
        r = 0
        for k in range(n + 1):
            r *= 10
            r += mul[k]
            mul[k] = r // i
            r %= i
    return add
