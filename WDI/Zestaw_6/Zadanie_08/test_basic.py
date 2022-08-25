# Bartłomiej Kozera
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

TEST_BASIC = [([1, 1, 1, 1], 4), ([2, 5], 4), ([1, 4, 5], 8), ([2, 4, 6], 7), ([1, 3, 9, 11], 17)]

TEST_NUM = 50
MIN_SIZE = 1
MAX_SIZE = 10
LLRANGE = 1
RRANGE = 100

WEIGHTS = RandFixArray(TEST_NUM, LLRANGE, RRANGE).get()

TEST_SMALL = [(RandFixArray(randint(MIN_SIZE, MAX_SIZE), LLRANGE, RRANGE).get(), WEIGHTS[i]) for i in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name='test_basic_s6t8', scope='sessiion')
class TestBasic:
    @pytest.mark.parametrize('data', TEST_BASIC)
    def test_basic(self, data):
        assert user_sol(data[0], data[1]) == corr_sol(data[0], data[1])

    @pytest.mark.parametrize('data', TEST_SMALL)
    def test_small_rand(self, data):
        assert user_sol(data[0], data[1]) == corr_sol(data[0], data[1])
