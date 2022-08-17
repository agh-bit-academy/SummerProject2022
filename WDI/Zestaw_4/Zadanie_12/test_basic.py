import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from ....Rand_Templates.RandFixMatrix import RandFixMatrix
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint


BASIC_TESTS = [([[0, 1, 2],
                [3, 4, 5],
                [6, 7, 8]], 10),
               ([[0, 1, 2],
                [3, 4, 5],
                [6, 7, 8]], 16)]


MIN_RANGE = 0
MAX_RANGE = 10 ** 2
MIN_ARRAY_SIZE = 0
MAX_ARRAY_SIZE = 10
MIN_K_VAL = 0
MAX_K_VAL = 10 ** 3
TEST_NUM = 18
MATRIX_RANDOM_SIZE = RandFixArray(TEST_NUM, MIN_ARRAY_SIZE, MAX_ARRAY_SIZE).get()
BASIC_RANDOM_TESTS = [(RandFixMatrix(MATRIX_RANDOM_SIZE[i], MATRIX_RANDOM_SIZE[i], MIN_RANGE, MAX_RANGE).get(),
                       randint(MIN_K_VAL, MAX_K_VAL))
                      for i in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name='test_basic_s4t12', scope='session')
class TestBasic:
    @pytest.mark.parametrize('array, k', BASIC_TESTS)
    def test_basic(self, array, k):
        assert user_sol(array, k) == corr_sol(array, k)

    @pytest.mark.parametrize('array, k', BASIC_RANDOM_TESTS)
    def test_random_basic(self, array, k):
        assert user_sol(array, k) == corr_sol(array, k)
