# Juliusz Wasieleski
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray as RandArr
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

TEST_BASIC = [[[]],
              [[1]],
              [[3, 5, 9]],
              [[1, 2],
               [5, 1]],
              [[1, 3, 3],
               [3, 3, 6]
               [3, 3, 9]],
              [[1, 4, 3, 6],
               [3, 2, 5, 4],
               [5, 9, 23, 8],
               [9, 27, 4, 1]]

              TEST_NUM = 20
L_BOUND = 1
R_BOUND = 10
MIN_NUM = 1
MAX_NUM = 10 ** 2

ROWS_LENGTH = RandArr(TEST_NUM, L_BOUND, R_BOUND)

SMALL_RAND_TESTS = [[RandArr(ROWS_LENGTH[i], MIN_NUM, MAX_NUM).get()
                     for _ in range(randint(L_BOUND, R_BOUND))] for i in range(TEST_NUM)] \

                   @ pytest.mark.order(1) \
                   @ pytest.mark.dependency(name='test_small_s4t8', scope='session')


class TestSmall:
    @pytest.mark.parametrize('data', TEST_BASIC)
    def test_basic(self, data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize('data', SMALL_RAND_TESTS)
    def test_small_rand(self, data):
        assert user_sol(data) == corr_sol(data)
