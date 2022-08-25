# Krzysztof Wysocki
def insert(el, ans):
    n = [0] * 10
    for i in range(len(ans)):
        if ans[i] < el:
            for j in range(i):
                n[j] = ans[j]
            n[i] = el
            for k in range(i + 1, len(ans)):
                n[k] = ans[k - 1]
            return n

    return ans


def f(T):
    ans = [0] * 10
    for i in range(len(T)):
        ans = insert(T[i], ans)
    return ans[9]
