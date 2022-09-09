# Juliusz Wasieleski
from math import sqrt
from math import inf


def center_of_gravity(points):
    n = len(points)
    if n == 0:
        return inf, inf
    x, y = 0, 0
    for point in points:
        x += point[0]
        y += point[1]
    x /= n
    y /= n
    return x, y


def euklides_len(point_1, point_2):
    if point_1 == (inf, inf) or point_2 == (inf, inf):
        return inf
    return sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)


def f(tab, taken=0, points_1=[], points_2=[]):
    n = len(tab)
    if taken == n:
        return euklides_len(center_of_gravity(points_1), center_of_gravity(points_2))
    return min(f(tab, taken + 1, points_1, points_2), f(tab, taken + 1, [*points_1, tab[taken]], points_2),
               f(tab, taken + 1, points_1, [*points_2, tab[taken]]))
