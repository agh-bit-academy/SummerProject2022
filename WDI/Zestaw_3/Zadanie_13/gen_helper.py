from ....Rand_Templates.RandFixArray import RandFixArray
# from RandFixArray import RandFixArray
from random import randint, shuffle
from itertools import chain


def gen_reverse_tables(size: int, lRange: int, rRange: int) -> tuple:
    tab = RandFixArray(max(size // 2, 1), lRange, rRange)
    tab = tab.get()
    return tab, tab[::-1]


def gen_palindromic_table(size: int, lRange: int, rRange: int) -> list:
    tab, tabRev = gen_reverse_tables(max(size // 2, 2), lRange, rRange)
    if size % 2 == 1:
        middPoint = randint(lRange, rRange)
        return tab + [middPoint] + tabRev
    else:
        return tab + tabRev


def gen_test_table(minPieceLen: int, maxPieceLen: int, noPieces: int, lRange: int, rRange: int) -> list:
    output = []
    for _ in range(noPieces):
        pieceLen = randint(minPieceLen, maxPieceLen)
        option = randint(0, 2)
        if option == 0:
            output.append(RandFixArray(pieceLen, lRange, rRange).get())
        if option == 1:
            tab, tabRev = gen_reverse_tables(pieceLen, lRange, rRange)
            output.append(tab)
            output.append(tabRev)
        if option == 2:
            output.append(gen_palindromic_table(pieceLen, lRange, rRange))
        if output[-1] == []:
            print(option)
    shuffle(output)
    output = list(chain.from_iterable(output))
    return output
