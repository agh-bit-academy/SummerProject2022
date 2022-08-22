# Bartłomiej Kozera
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray as RandArr
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

TEST_NUM = 20
L_BOUND = 10**2
R_BOUND = 500
MIN_NUM = 10**3
MAX_NUM = 10**8

ROWS_LENGTH = RandArr(TEST_NUM, L_BOUND, R_BOUND)

BIG_RAND_TESTS = [[RandArr(ROWS_LENGTH[i], MIN_NUM, MAX_NUM).get()
                    for _ in range(randint(L_BOUND, R_BOUND))] for i in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name='test_big_s4t4', depends=['test_small_s4t4'], scope='session')
@pytest.mark.parametrize('data', BIG_RAND_TESTS)
def test_med_rand(data):
    assert user_sol(data) == corr_sol(data)
