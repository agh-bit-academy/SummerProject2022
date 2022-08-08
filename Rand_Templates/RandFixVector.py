from random import seed, randint


class RandFixVector():
    def __init__(
        self, v_size: int, l_range: float, r_range: float, rand_gen=randint, fixed=False, v_seed=0
    ) -> None:
        self.__array = None
        if not fixed:
            self.__array = RandFixVector.gen_random(v_size, l_range, r_range, rand_gen)
        else:
            self.__array = RandFixVector.gen_random_fixed(v_size, l_range, r_range, rand_gen, v_seed)

    def get(self):
        return self.__array

    @staticmethod
    def is_same_len(v, w) -> bool:
        if (type(v) == type(w) and type(v) == RandFixVector):
            return len(v) == len(w)
        else:
            return False

    @staticmethod
    def gen_random(v_size: int, l_range: float, r_range: float, rand_gen) -> list:
        return [rand_gen(l_range, r_range) for _ in range(v_size)]

    @staticmethod
    def gen_random_fixed(
        v_size: int, l_range: float, r_range: float, rand_gen, v_seed=0
    ) -> list:
        seed(v_seed)
        output = [None for _ in range(v_size)]
        for i in range(v_size):
            output[i] = rand_gen(l_range, r_range)
            v_seed += 1
            seed(v_seed)
        seed()
        return output

    def set_as(self, array: list) -> bool:
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

    def __sorted__(self):
        pass

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


class X:
    pass


V = RandFixVector(3, 2, 5, fixed=True)
Q = RandFixVector(7, 2, 5)
print(V, Q.get())
V.set_as([1, 9])
print(V)
