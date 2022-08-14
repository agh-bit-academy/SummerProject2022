from random import randint
from ....Rand_Templates.RandFixArray import RandFixArray


def gen_arith_tab(tabSize: int, initialTerm: int, difference: int) -> list:
    return [initialTerm + difference * i for i in range(tabSize)]


def gen_test_tab(lPieceSize: int, rPieceSize: int, noPieces: int,
                 lRange, rRange, minDiff, maxDiff, hasRand: int = 1) -> list:
    output = []
    for _ in range(noPieces):
        isRandom = 0
        if hasRand:
            isRandom = randint(0, 1)
        size = randint(lPieceSize, rPieceSize)
        if isRandom:
            output = output + RandFixArray(size, lRange, rRange).get()
        else:
            initialTerm = randint(lRange, rRange)
            difference = randint(minDiff, maxDiff)
            output = output + gen_arith_tab(size, initialTerm, difference)
    return output
