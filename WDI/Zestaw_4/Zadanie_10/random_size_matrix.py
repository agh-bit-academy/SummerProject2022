# Andrzej Karciński
# funckja generująca macierze o randomowych wymiarach
from ....Rand_Templates.RandFixArray import RandFixArray
from random import randint


def random_size_matrix(LRANGE, RRANGE):
    n = randint(LRANGE, RRANGE)
    m = randint(LRANGE, RRANGE)
    array = [RandFixArray(n, 0, 1).get() for _ in range(m)]
    return array
