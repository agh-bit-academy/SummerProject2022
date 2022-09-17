# Sebastian Soczawa
def count_dist(p):
    return (p[0] ** 2 + p[1] ** 2 + p[2] ** 2)


def rec(T, r, coords=(0, 0, 0), weight=0, i=0):
    if weight >= 3:
        if r ** 2 >= count_dist(coords):
            return True
    if i == len(T):
        return False
    if weight == 0:
        new_coords = T[i]
    else:
        new_coords = ((coords[0] * weight + T[i][0]) / (weight + 1),
                      (coords[1] * weight + T[i][1]) / (weight + 1),
                      (coords[2] * weight + T[i][2]) / (weight + 1))

    return rec(T, r, new_coords, weight + 1, i + 1) or\
        rec(T, r, coords, weight, i + 1)


def f(T, r):
    return rec(T, r)
