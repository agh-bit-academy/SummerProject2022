from random import randint
from ....Rand_Templates.RandFixArray import RandFixArray


def gen_arith_tab(tabSize: int, initialTerm: int, difference: int) -> list:
    return [initialTerm + difference * i for i in range(tabSize)]


def gen_test_tab(lPieceSize: int, rPieceSize: int, noPieces: int,
                 l_range, r_range, min_diff, max_diff, has_rand: int = 1) -> list:
    output = []
    for _ in range(noPieces):
        is_random = 0
        if has_rand:
            is_random = randint(0, 1)
        size = randint(lPieceSize, rPieceSize)
        if is_random:
            output = output + RandFixArray(size, l_range, r_range).get()
        else:
            initial_term = randint(l_range, r_range)
            difference = randint(min_diff, max_diff)
            output = output + gen_arith_tab(size, initial_term, difference)
    return output
