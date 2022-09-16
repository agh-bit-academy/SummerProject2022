# Maciej Bartczak
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol

TEST_BASIC = [[0],
              [1],
              [0, 0],
              [2, 2, 2],
              [3, 0, 0, 0],
              [2, 1, 2, 1, 2]]

TEST_NUM = 20
MIN_SIZE = 1
MAX_SIZE = 20
MIN_NUM = 1
MAX_NUM = 10 ** 2

TEST_SIZE = RandFixArray(TEST_NUM, MIN_SIZE, MAX_SIZE).get()
TEST_SMALL = [RandFixArray(size, MIN_NUM, MAX_NUM).get() for size in TEST_SIZE]


@pytest.mark.order(1)
@pytest.mark.dependency(name='test_basic_s6t22', scope='session')
class TestBasic:
    @pytest.mark.parametrize('data', TEST_BASIC)
    def test_basic(self, data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize('data', TEST_SMALL)
    def test_small_rand(self, data):
        assert user_sol(data) == corr_sol(data)
