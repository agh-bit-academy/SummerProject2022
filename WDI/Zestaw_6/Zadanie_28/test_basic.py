# Izabella Rosikoń
# Juliusz Wasieleski
from .prog import f as user_sol
from .sol import f as corr_sol
from math import log10
from math import log2
from random import randint
import pytest


def split_into_3(left_ones):
    how_many_ones = []
    for i in range(3):
        ones_tmp = randint(0, left_ones)
        how_many_ones.append(ones_tmp)
        left_ones -= ones_tmp
    return how_many_ones


def gen_rand_two_power(min_range, max_range, taken):
    power = randint(int(log2(min_range)), int(log2(max_range)))
    while power in taken:
        power = randint(int(log2(max(min_range, 1))), int(log2(max_range)))
    return 2 ** power, power


def make_number(how_many_ones, min_range, max_range):
    result = 0
    taken = set()
    while how_many_ones != 0:
        numb_tmp, power = gen_rand_two_power(max(min_range, 1), max_range, taken)
        result += numb_tmp
        taken.add(power)
        min_range -= numb_tmp
        max_range -= numb_tmp
        how_many_ones -= 1
    return result


def generate_good(min_range, max_range, l_range, r_range):
    size = (randint(l_range, r_range) // 3) * 3
    how_many_ones = randint(max(int(log10(min_range)), 1), int(log10(max_range)))

    amounts_of = [[], [], []]
    for i in range(3):
        left_ones = how_many_ones
        for j in range(size // 3, 1, -1):
            amount_tmp = randint(0, left_ones)
            amounts_of[i].append(amount_tmp)
            left_ones -= amount_tmp
        amounts_of[i].append(left_ones)

    result = []
    for sett in amounts_of:
        for i in range(len(sett)):
            result.append(make_number(sett[i], min_range, max_range))
    return sorted(result)


def generate_bad(min_range, max_range, l_range, r_range):
    size = (randint(l_range, r_range) // 3) * 3 + 1
    left_ones = randint(max(int(log10(min_range)), 1), int(log10(max_range))) * 3
    how_many_ones = split_into_3(left_ones)
    sizes = split_into_3(size)

    amounts_of = [[], [], []]
    for i in range(3):
        left_ones = how_many_ones[i]
        for j in range(sizes[i], 1, -1):
            amount_tmp = randint(0, left_ones)
            amounts_of[i].append(amount_tmp)
            left_ones -= amount_tmp
        amounts_of[i].append(left_ones)

    result = []
    for sett in amounts_of:
        for i in range(len(sett)):
            result.append(make_number(sett[i], min_range, max_range))
    return sorted(result)


def generate(min_range, max_range, l_range, r_range):
    if randint(1, 2) % 2 == 0:
        return generate_good(min_range, max_range, l_range, r_range)
    else:
        return generate_bad(min_range, max_range, l_range, r_range)


MIN_RANGE = 1
MAX_RANGE = 100
TEST_NUM = 15
L_RANGE = 1
R_RANGE = 5
RANDOM_SIZE = [randint(L_RANGE, R_RANGE) for _ in range(TEST_NUM)]

TEST_BASIC = [[0, 1, 2, 3], [2, 3, 5, 7, 15], [2, 4, 8, 16, 32], [1, 17, 29, 42], [13, 17, 19]]
TEST_BASIC_RANDOM = [generate(MIN_RANGE, MAX_RANGE, L_RANGE, R_RANGE) for _ in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name='s6t28_test_basic', scope='session')
class TestBasic:
    @pytest.mark.parametrize('data', TEST_BASIC)
    def test_basic(self, data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize('data', TEST_BASIC_RANDOM)
    def test_basic_random(self, data):
        assert user_sol(data) == corr_sol(data)
