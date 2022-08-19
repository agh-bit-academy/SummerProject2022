# Maciej Sieniek
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray as randArr
from .prog import f as user_sol
from .sol import f as corr_sol


BASIC_TESTS = [[[[0, 1, 2], [3, 4, 5], [6, 7, 8]],
               [[0, 1, 2], [3, 4, 5], [6, 7, 8]],
               [[0, 1, 2], [3, 4, 5], [6, 7, 8]]],
               [[[0, 1, 2], [3, 4, 5], [6, 7, 8]],
               [[8, 6, 8], [6, 8, 6], [8, 6, 8]],
               [[0, 1, 2], [3, 4, 5], [6, 7, 8]]]]


MIN_RANGE = 0
MAX_RANGE = 10 ** 2
MIN_ARR_SIZE = 0
MAX_ARR_SIZE = 10
TEST_NUM = 8
RANDOM_ARR_SIZE = randArr(TEST_NUM, MIN_ARR_SIZE, MAX_ARR_SIZE).get()
BASIC_RANDOM_TESTS = [[[randArr(RANDOM_ARR_SIZE[i], MIN_RANGE, MAX_RANGE)
                      for _ in range(RANDOM_ARR_SIZE[i])]
                      for _ in range(RANDOM_ARR_SIZE[i])]
                      for i in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name='test_basic_s4t12', scope='session')
class TestBasic:
    @pytest.mark.parametrize('array', BASIC_TESTS)
    def test_basic(self, array):
        assert user_sol(array) == corr_sol(array)

    @pytest.mark.parametrize('array', BASIC_RANDOM_TESTS)
    def test_random_basic(self, array):
        assert user_sol(array) == corr_sol(array)
