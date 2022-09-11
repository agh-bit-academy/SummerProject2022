# Juliusz Wasieleski
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

TEST_BASIC = [([[]], 0),
              ([[3]], 0),
              ([[2, 5],
                [3, 2]], 1),
              ([[1, 4, 5],
                [3, 5, 4],
                [1, 2, 7]], 2),
              ([[1, 1, 1, 1],
                [3, 12, 4, 1],
                [32, 5, 21, 1],
                [43, 2, 3, 1]], 0)]

TEST_NUM = 40
L_BOUND = 1
R_BOUND = 7
MIN_NUM = 0
MAX_NUM = 10 ** 2
MIN_SIZE = 1
MAX_SIZE = 7

ROWS_LENGTH = RandFixArray(TEST_NUM, L_BOUND, R_BOUND)

BOARDS = [[RandFixArray(ROWS_LENGTH[i], MIN_NUM, MAX_NUM).get()
           for _ in range(ROWS_LENGTH[i])] for i in range(TEST_NUM)]

TEST_SMALL = [(BOARDS[i], randint(0, MAX_NUM)) for i in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name='test_basic_s6t21', scope='session')
class TestBasic:
    @pytest.mark.parametrize('data', TEST_BASIC)
    def test_basic(self, data):
        assert user_sol(data[0], data[1]) == corr_sol(data[0], data[1])

    @pytest.mark.parametrize('data', TEST_SMALL)
    def test_small_rand(self, data):
        assert user_sol(data[0], data[1]) == corr_sol(data[0], data[1])
