# Bartłomiej Kozera
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray as RandArr
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

TEST_BASIC = [([2, 3, 5], 6),
            ([1, 1, 1, 1, 1], 1),
            ([1, 2, 3, 4, 5, 6], 6),
            ([3, 6, 8, 1, 3, 4, 6], 8),
            ([2, 1, 3, 7, 6, 9, 8, 4], 12)]

TEST_NUM = 20
LRANGE = 1
RRANGE = 10
MIN_SIZE = 1
MAX_SIZE = 10
MIN_PROD = 1
MAX_PROD = 50
TEST_SMALL = [(RandArr(randint(MIN_SIZE, MAX_SIZE), LRANGE, RRANGE).get(), randint(MIN_PROD, MAX_PROD))
            for _ in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name='test_s6t11_basic', scope='session')
class TestSmall:
    @pytest.mark.parametrize('data', TEST_BASIC)
    def test_basic(self, data):
        assert user_sol(data[0], data[1]) == corr_sol(data[0], data[1])

    @pytest.mark.parametrize('data', TEST_SMALL)
    def test_small_random(self, data):
        assert user_sol(data[0], data[1]) == corr_sol(data[0], data[1])
