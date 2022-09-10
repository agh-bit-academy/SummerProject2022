# Juliusz Wasieleski
def field(x1, x2, y1, y2):
    return (x2 - x1) * (y2 - y1)


def field_sum(tab):
    fieldd = 0
    for square in tab:
        x1, x2, y1, y2 = square
        fieldd += field(x1, x2, y1, y2)
    return fieldd


def do_they_not_overlap(tab):
    n = len(tab)
    x_es = [[] for _ in range(n)]
    y_es = [[] for _ in range(n)]
    for i in range(n):
        x1, x2, y1, y2 = tab[i]
        x_es[i] += (x1, x2)
        y_es[i] += [y1, y2]
    x_es.sort()
    y_es.sort()

    x_tmp = x_es[0][0]
    y_tmp = y_es[0][0]
    for i in range(len(x_es)):
        x1, x2 = x_es[i]
        y1, y2 = y_es[i]
        if x_tmp > x1 or y_tmp > y1:
            return False
        x_tmp = x2
        y_tmp = y2
    return True


def f(tab, i=0, left=13, taken=[]):
    n = len(tab)
    if left == 0 and field_sum(taken) == 2012:
        return True
    if i == n:
        return False
    a = f(tab, i + 1, left, taken)
    if do_they_not_overlap([*taken, tab[i]]):
        b = f(tab, i + 1, left - 1, [*taken, tab[i]])
    else:
        b = False
    if a or b:
        return True
    else:
        return False
