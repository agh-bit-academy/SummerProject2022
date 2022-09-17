# Sebastian Soczawa
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

TEST_BASIC = [([(0, 0, 0), (0, 0, 0), (0, 0, 0)], 0, True),
              ([(1, 1, 1), (1, 1, 1), (1, 1, 1)], 2, True),
              ([(1, 1, 1), (0, 0, 0), (2, 2, 2)], 1, False),
              ([(-1, -1, -1), (0, 0, 0), (-2, -2, -2)], 1, False),
              ([(6, 10, 12), (4, 12, 8), (2, 2, 2)], 12, True),
              ([(6, 10, 12), (4, 12, 8), (2, 2, 2)], 2, False),
              ([(6, 10, 12), (4, 4, 4), (6, 8, 11), (6, 4, 5)], 4, False),
              ([(6, 10, 12), (4, 4, 4), (6, 8, 11), (6, 4, 5)], 32, True)
              ]

TEST_NUM = 32
L_RANGE = -100
R_RANGE = 100
SIZE = 15
MAX_R = 1500

COORDS_TAB = [RandFixArray(3, L_RANGE, R_RANGE) for _ in range(SIZE)]

TEST_SMALL = [(COORDS_TAB, randint(0, R_RANGE)) for _ in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name='test_basic_s6t29', scope='session')
class TestBasic:
    @pytest.mark.parametrize('data, R, sol', TEST_BASIC)
    def test_basic(self, data, R, sol):
        assert user_sol(data, R) == sol

    @pytest.mark.parametrize('data, R', TEST_SMALL)
    def test_small_rand(self, data, R):
        assert user_sol(data, R) == corr_sol(data, R)
