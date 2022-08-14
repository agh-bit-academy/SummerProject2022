from ....Rand_Templates.RandFixArray import RandFixArray
# from RandFixArray import RandFixArray
from random import randint, shuffle
from itertools import chain


def gen_reverse_tables(size: int, l_range: int, r_range: int) -> tuple:
    tab = RandFixArray(max(size // 2, 1), l_range, r_range)
    tab = tab.get()
    return tab, tab[::-1]


def gen_palindromic_table(size: int, l_range: int, r_range: int) -> list:
    tab, tab_rev = gen_reverse_tables(max(size // 2, 2), l_range, r_range)
    if size % 2 == 1:
        midd_point = randint(l_range, r_range)
        return tab + [midd_point] + tab_rev
    else:
        return tab + tab_rev


def gen_test_table(min_piece_len: int, max_piece_len: int, no_pieces: int, l_range: int, r_range: int) -> list:
    output = []
    for _ in range(no_pieces):
        piece_len = randint(min_piece_len, max_piece_len)
        option = randint(0, 2)
        if option == 0:
            output.append(RandFixArray(piece_len, l_range, r_range).get())
        if option == 1:
            tab, tab_rev = gen_reverse_tables(piece_len, l_range, r_range)
            output.append(tab)
            output.append(tab_rev)
        if option == 2:
            output.append(gen_palindromic_table(piece_len, l_range, r_range))
    shuffle(output)
    output = list(chain.from_iterable(output))
    return output
