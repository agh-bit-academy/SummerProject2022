# Juliusz Wasieleski
import pytest
from random import randint
from .prog import f as user_sol
from .sol import f as corr_sol


def get_cords_good(min_int, max_int):
    sizes = []
    left_field = 2012
    for i in range(13, 1, -1):
        field_tmp = randint(1, left_field - i)
        sizes.append(field_tmp)
        left_field -= field_tmp
    sizes.append(left_field)

    x1 = randint(min_int, max_int)
    y1 = randint(min_int, max_int)
    output = []
    for i in range(len(sizes)):
        output.append((x1, x1 + 1, y1, y1 + sizes[i]))
        x1 += 1
        y1 += sizes[i]
    return output


def get_cords(int_min, int_max, size_min, size_max):
    if randint(1, 5) % 2 == 1:
        output = get_cords_good(int_min, int_max)
        output += get_cords_bad(int_min, int_max, max(0, size_min - 13), max(0, size_max - 13))
    else:
        output = get_cords_bad(int_min, int_max, size_min, size_max)
    return output


def get_cords_bad(int_min, int_max, size_min, size_max):
    n = randint(size_min, size_max)
    output = []
    for _ in range(n):
        x1 = randint(int_min, int_max)
        x2 = randint(int_min, int_max)
        while x1 == x2:
            x1 = randint(int_min, int_max)
            x2 = randint(int_min, int_max)
        res = tuple()
        if x1 < x2:
            res += (x1, x2)
        else:
            res += (x2, x1)
        y1 = randint(int_min, int_max)
        y2 = randint(int_min, int_max)
        while y1 == y2:
            y1 = randint(int_min, int_max)
            y2 = randint(int_min, int_max)
        if y1 < y2:
            res += (y1, y2)
        else:
            res += (y2, y1)
        output.append(res)
    return output


BASIC_TESTS = [[(1, 11, 1, 21),
                (11, 21, 21, 41),
                (21, 31, 41, 61),
                (31, 41, 61, 81),
                (41, 51, 81, 101),
                (51, 61, 101, 121),
                (61, 71, 121, 141),
                (71, 81, 141, 161),
                (81, 91, 161, 181),
                (91, 101, 181, 201),
                (101, 103, 201, 204),
                (103, 105, 204, 206),
                (105, 106, 206, 208)],
               [(1, 11, 1, 21),
                (11, 21, 21, 41),
                (21, 31, 41, 61)]]

SIZE_MIN = 10
SIZE_MAX = 13
MIN_INT = -2000
MAX_INT = 2000
TEST_NUM = 38

BASIC_RANDOM_TESTS = [get_cords(MIN_INT, MAX_INT, SIZE_MIN, SIZE_MAX) for _ in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s6t27", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", BASIC_TESTS)
    def test_basic(self, data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
    def test_basic_random(self, data):
        assert user_sol(data) == corr_sol(data)
