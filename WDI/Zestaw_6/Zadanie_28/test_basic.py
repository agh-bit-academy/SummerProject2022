# Izabella Rosikoń
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint
import pytest


MIN_RANGE = 0
MAX_RANGE = 100
TEST_NUM = 15
L_RANGE = 1
R_RANGE = 5
RANDOM_SIZE = [randint(L_RANGE, R_RANGE) for _ in range(TEST_NUM)]

TEST_BASIC = [[0, 1, 2, 3], [5, 6, 10, 7], [2, 4, 8, 16, 32], [1, 17, 29, 42], [13, 17, 19]]

TEST_BASIC_RANDOM = [RandFixArray(RANDOM_SIZE[i], MIN_RANGE, MAX_RANGE).get() for i in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name='s6t28_test_basic', scope='session')
class TestBasic:
    @pytest.mark.parametrize('data', TEST_BASIC)
    def test_basic(self, data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize('data', TEST_BASIC_RANDOM)
    def test_basic_random(self, data):
        assert user_sol(data) == corr_sol(data)
