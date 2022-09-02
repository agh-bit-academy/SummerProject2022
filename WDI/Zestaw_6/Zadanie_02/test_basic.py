import pytest
from ....Rand_Templates.RandFixArray import RandFixArray as RandArr
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

TEST_BASIC = [[2, 5, 7],
            [5, 2, 2, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [4, 5, 8, 2, 6, 3, 8],
            [3, 4, 5, 6, 7, 8, 9, 10]]

TEST_NUM = 20
LRANGE = 1
RRANGE = 100
MIN_SIZE = 1
MAX_SIZE = 10
TEST_SMALL = [RandArr(randint(MIN_SIZE, MAX_SIZE), LRANGE, RRANGE).get() for _ in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name='test_s6t2_basic', scope='session')
class TestSmall:
    @pytest.mark.parametrize('data', TEST_BASIC)
    def test_basic(self, data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize('data', TEST_SMALL)
    def test_small_random(self, data):
        assert user_sol(data) == corr_sol(data)
