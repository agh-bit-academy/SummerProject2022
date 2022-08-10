# Krzysztof Wysocki
def insert(el, ans):
    n = []
    for i in range(len(ans)):
        if ans[i] < el:
            t = [el]
            n = ans[:i] + t + ans[i:]
            break

    return n


def f(T):
    ans = [0]
    for i in range(len(T)):
        ans = insert(T[i], ans)
    return ans[9]
