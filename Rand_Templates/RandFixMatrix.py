from RandFixArray import RandFixArray as Rfarr

from ._empty_num import Num
from random import seed, randint


class RandFixMatrix():
    rfmat_seed = 0

    def __init__(
        self, row_num: int, col_num: int, l_range: float, r_range: float,
        rand_gen: 'function(Num, Num)' = randint, fixed=False, v_seed=0
    ) -> None:
        self.__array = None
        if not fixed:
            self.__array = [Rfarr.gen_random(col_num, l_range, r_range, rand_gen) for _ in range(row_num)]
        else:
            self.__array = [Rfarr.gen_random_fixed(col_num, l_range, r_range, rand_gen, v_seed) for _ in range(row_num)]

    def __getitem__(self, index_row: int, index_col: int) -> 'Num':
        if type(index_row) == int and type(index_col) == int:
            return self.get()[index_row][index_col]
        else:
            return None

    def get(self) -> 'RandFixMatrix':
        return self.__array

    @staticmethod
    def gen_random(
        row_num: int, col_num: int, l_range: float, r_range: float,
        rand_gen: 'function(Num, Num)' = randint
    ) -> list:
        return [[rand_gen(l_range, r_range) for _ in range(col_num)] for _ in range(row_num)]

    @staticmethod
    def gen_random_fixed(
        row_num: int, col_num: int, l_range: float, r_range: float,
        rand_gen: 'function(Num, Num)' = randint, v_seed=None
    ) -> list:
        seed(v_seed) if v_seed else seed(RandFixMatrix.rfvec_seed)
        output = [[None for _ in range(col_num)] for _ in range(row_num)]
        for i in range(row_num):
            for j in range(col_num):
                output[i][j] = rand_gen(l_range, r_range)
                if v_seed:
                    v_seed += 1
                    seed(v_seed)
                else:
                    RandFixMatrix.rfvec_seed += 1
                    seed(RandFixMatrix.rfvec_seed)
        seed()
        return output
