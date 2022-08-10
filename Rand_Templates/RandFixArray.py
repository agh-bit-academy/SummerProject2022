from ._empty_num import Num
from random import seed, randint


class RandFixArray():
    rfvec_seed = 0

    def __init__(
        self, v_size: int, l_range: float, r_range: float,
        rand_gen: 'function(Num, Num)' = randint, fixed=False, v_seed=0
    ) -> None:
        self.__array = None
        if not fixed:
            self.__array = RandFixArray.gen_random(v_size, l_range, r_range, rand_gen)
        else:
            self.__array = RandFixArray.gen_random_fixed(v_size, l_range, r_range, rand_gen, v_seed)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index <= len(self):
            output = self.index
            self.index += 1
            return output
        else:
            raise StopIteration

    def __getitem__(self, index: int) -> 'Num':
        if type(index) == int:
            return self.get()[index]
        else:
            return None

    def get(self) -> 'RandFixArray':
        return self.__array

    def sort(self, key=None) -> 'None':
        if key:
            self.__array = sorted(self.__array, key=key)
        else:
            self.__array = sorted(self.__array)

    @staticmethod
    def gen_random(
        v_size: int, l_range: float, r_range: float,
        rand_gen: 'function(Num, Num)' = randint
    ) -> list:
        return [rand_gen(l_range, r_range) for _ in range(v_size)]

    @staticmethod
    def gen_random_fixed(
        v_size: int, l_range: float, r_range: float,
        rand_gen: 'function(Num, Num)' = randint, v_seed=None
    ) -> list:
        seed(v_seed) if v_seed else seed(RandFixArray.rfvec_seed)
        output = [None for _ in range(v_size)]
        for i in range(v_size):
            output[i] = rand_gen(l_range, r_range)
            if v_seed:
                v_seed += 1
                seed(v_seed)
            else:
                RandFixArray.rfvec_seed += 1
                seed(RandFixArray.rfvec_seed)
        seed()
        return output

    def set_as(self, array: list['Num']) -> bool:
        is_list = True
        is_list = is_list and type(array) == list
        is_num = True
        if is_list:
            for el in array:
                is_num = is_num and (type(el) == int or type(el) == float)

        output = True
        if is_list and is_num:
            self.__array = array
        else:
            output = False

        return output

    def __len__(self):
        return len(self.__array)

    def __str__(self):
        output = "["
        for el in range(len(self.__array)):
            output += f"{str(self.__array[el])}"
            if el == len(self.__array) - 1:
                output += "]"
            else:
                output += ", "
        return output

    def __neg__(self):
        pass

    def __pos__(self):
        pass

    def __invert__(self):
        pass

    # Vector and int
    def __add__(self, other):
        pass

    # Vector and int
    def __sub__(self, other):
        pass

    # Vector and int
    def __mul__(self, other):
        pass

    # Vector and int
    def __truediv__(self, other):
        pass

    # int
    def __floordiv__(self, other):
        pass

    # int
    def __mod__(self, other):
        pass

    # num
    def __pow__(self, other):
        pass

    # int
    def __rshift__(self, other):
        pass

    # int
    def __lshift__(self, other):
        pass

    # Vector and int
    def __and__(self, other):
        pass

    # Vector and int
    def __or__(self, other):
        pass

    # Vector and int
    def __xor__(self, other):
        pass

    # Vector
    def __lt__(self, other):
        pass

    # Vector
    def __gt__(self, other):
        pass

    # Vector
    def __le__(self, other):
        pass

    # Vector
    def __ge__(self, other):
        pass

    # Vector
    def __eq__(self, other):
        pass

    # Vector
    def __ne__(self, other):
        pass

    # Vector and int
    def __iadd__(self, other):
        pass

    # Vector and int
    def __isub__(self, other):
        pass

    # Vector and int
    def __imul__(self, other):
        pass

    # Vector and int
    def __idiv__(self, other):
        pass

    # Vector and int
    def __ifloordiv__(self, other):
        pass

    # int
    def __imod__(self, other):
        pass

    # num
    def __ipow__(self, other):
        pass

    # int
    def __irshift(self, other):
        pass

    # int
    def __ilshift(self, other):
        pass

    # Vector and int
    def __iand__(self, other):
        pass

    # Vector and int
    def __ior__(self, other):
        pass

    # Vector and int
    def __ixor__(self, other):
        pass
