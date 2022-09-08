# Izabella Rosikoń
def fill_tab(tab_bigger, ind):
    tab_smaller = [[0 for _ in range(len(tab_bigger) - 1)] for _ in range(len(tab_bigger) - 1)]
    i = 0
    for j in range(len(tab_bigger)):
        if j == ind:
            continue
        for k in range(len(tab_smaller)):
            tab_smaller[i][k] = tab_bigger[j][k+1]
        i += 1
    return tab_smaller


def f(T):
    if len(T) == 2:
        return T[0][0] * T[1][1] - T[0][1] * T[1][0]
    det = 0
    for i in range(len(T)):
        det += T[i][0]*(-1)**(i)*f(fill_tab(T, i))
    return det
