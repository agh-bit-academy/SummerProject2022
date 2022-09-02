# Krzysztof Wysocki


def ff(num, ans, iter=1, s=""):
    if num == 0:
        ans.append(s)  # print(s)
    else:
        for i in range(iter, num + 1):
            ff(num - i, ans, i, s + str(i))


def f(num):
    ans = []
    ff(num, ans)
    return ans
