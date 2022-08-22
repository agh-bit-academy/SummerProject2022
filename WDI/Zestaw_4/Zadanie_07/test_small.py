# Bartłomiej Kozera
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

TEST_BASIC = [
        [[[1, 1],
        [1, 1]],
        [None, None, None, None]],

        [[[0, 1],
        [-1, 5]],
        [None, None, None, None]],

        [[[0]],
        [None]],

        [[[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]],
        [None, None, None, None, None, None, None, None, None]]
]

TEST_NUM = 30
LRANGE = -100
RRANGE = 100
MINSIZE = 1
MAXSIZE = 10

TAB_SIZE = [randint(MINSIZE, MAXSIZE) for _ in range(TEST_NUM)]

TEST_SMALL_RAND_MAT = [[sorted(RandFixArray(TAB_SIZE[i], LRANGE, RRANGE).get())
                for _ in range(TAB_SIZE[i])] for i in range(TEST_NUM)]

ANS_TABS = [[None for _ in range(TAB_SIZE[i]**2)] for i in range(TEST_NUM)]

TEST_SMALL_DATA = [[TEST_SMALL_RAND_MAT[i], ANS_TABS[i]] for i in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_small_s4t07", scope="session")
class TestSmall:
    @pytest.mark.parametrize('data', TEST_BASIC)
    def test_small(self, data):
        assert user_sol(data[0], data[1]) == corr_sol(data[0], data[1])

    @pytest.mark.parametrize('data', TEST_SMALL_DATA)
    def test_small_rand(self, data):
        assert user_sol(data[0], data[1]) == corr_sol(data[0], data[1])
