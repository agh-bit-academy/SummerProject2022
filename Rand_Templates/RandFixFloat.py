from random import random, seed


class RandFixFloat():
    DIG_NUM = 4
    SEED_VAL = 0

    @staticmethod
    def gen_random(l_range: float, r_range: float) -> float:
        if l_range < r_range:
            output = random()
            output *= r_range - l_range
            output += l_range
            return output
        else:
            return 0

    @staticmethod
    def gen_random_fixed(l_range: float, r_range: float) -> float:
        seed(RandFixFloat.SEED_VAL)
        RandFixFloat.SEED_VAL += 1
        seed()
        return RandFixFloat.gen_random(l_range, r_range)

    @staticmethod
    def print(val: any) -> float:
        if not isinstance(val, float):
            val = float(val)
        return round(val, RandFixFloat.DIG_NUM)
