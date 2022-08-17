# Maciej Sieniek
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray as randArr
from .prog import f as user_sol
from .sol import f as corr_sol


MIN_RANGE = 0
MAX_RANGE = 10 ** 3
MIN_ARR_SIZE = 0
MAX_ARR_SIZE = 10 ** 2
TEST_NUM = 15
RANDOM_ARR_SIZE = randArr(TEST_NUM, MIN_ARR_SIZE, MAX_ARR_SIZE).get()
BIG_RANDOM_TESTS = [[[randArr(RANDOM_ARR_SIZE[i], MIN_RANGE, MAX_RANGE)
                    for _ in range(RANDOM_ARR_SIZE[i])]
                    for _ in range(RANDOM_ARR_SIZE[i])]
                    for i in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name='test_big_s4t12', depends=['test_basic_s4t12'], scope='session')
@pytest.mark.parametrize('array', BIG_RANDOM_TESTS)
def test_random_big(array):
    assert user_sol(array) == corr_sol(array)
