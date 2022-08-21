# Krzysztof Wysocki


def merge_a(t1, t2):
    n1, n2 = len(t1), len(t2)
    t3 = []
    i, j = 0, 0

    while i < n1 and j < n2:
        if t1[i] < t2[j]:
            t3.append(t1[i])
            i += 1
        else:
            t3.append(t2[j])
            j += 1

    while i < n1:
        t3.append(t1[i])
        i += 1
    while j < n2:
        t3.append(t2[j])
        j += 1
    return t3


def merge(tab):
    t = tab[0]
    for i in range(1, len(tab)):
        t = merge_a(t, tab[i])
    return t


def f(tab):
    ans = []
    tab = merge(tab)
    n = len(tab)
    i = 0
    flag = True

    while i < n - 1:

        if tab[i + 1] == tab[i]:
            flag = False
            while i < n - 1 and tab[i + 1] == tab[i]:
                i += 1
        elif tab[i + 1] != tab[i]:
            if flag:
                ans.append(tab[i])
            flag = True
            i += 1

    if tab[n - 1] != tab[n - 2]:
        ans.append(tab[n - 1])

    return ans
