def _f(tab, ver, col, summ):
    m = len(tab[0])
    n = len(tab)
    if col < 0 or col >= m:
        return float('inf')
    if ver == n-1:
        return summ + tab[ver][col]

    return min(_f(tab, ver + 1, col - 1, summ + tab[ver][col]),
               _f(tab, ver + 1, col, summ + tab[ver][col]),
               _f(tab, ver + 1, col + 1, summ + tab[ver][col]))


def f(tab, k):
    if len(tab[0]) == 0:
        return 0
    return _f(tab, 0, k, 0)

