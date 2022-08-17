# Maciej Sieniek
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from ....Rand_Templates.RandFixMatrix import RandFixMatrix
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint


MIN_RANGE = 0
MAX_RANGE = 10 ** 3
MIN_ARRAY_SIZE = 10
MAX_ARRAY_SIZE = 10 ** 2
MIN_K_VAL = 0
MAX_K_VAL = 10 ** 4
TEST_NUM = 5
MATRIX_RANDOM_SIZE = RandFixArray(TEST_NUM, MIN_ARRAY_SIZE, MAX_ARRAY_SIZE).get()
BIG_RANDOM_TESTS = [(RandFixMatrix(MATRIX_RANDOM_SIZE[i], MATRIX_RANDOM_SIZE[i], MIN_RANGE, MAX_RANGE).get(),
                     randint(MIN_K_VAL, MAX_K_VAL))
                    for i in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name='test_big_s4t9', depends=['test_basic_s4t9'], scope='session')
class TestBasic:
    @pytest.mark.parametrize('array, k', BIG_RANDOM_TESTS)
    def test_random_basic(self, array, k):
        assert user_sol(array, k) == corr_sol(array, k)
