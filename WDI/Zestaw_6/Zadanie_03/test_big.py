# Juliusz Wasieleski
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

TEST_NUM = 50
L_BOUND = 1
R_BOUND = 15
MIN_NUM = 0
MAX_NUM = 10 ** 2
MIN_SIZE = 1
MAX_SIZE = 15

ROWS_LENGTH = RandFixArray(TEST_NUM, L_BOUND, R_BOUND)

BOARDS = [[RandFixArray(ROWS_LENGTH[i], MIN_NUM, MAX_NUM).get()
           for _ in range(randint(L_BOUND, R_BOUND))] for i in range(TEST_NUM)]

TEST_BIG = [(BOARDS[i], randint(0, len(BOARDS[i][0]) - 1)) for i in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name='test_big_s6t3', depends=['test_basic_s6t3'], scope='session')
@pytest.mark.parametrize('data', TEST_BIG)
def test_big_rand(data):
    assert user_sol(data[0], data[1]) == corr_sol(data[0], data[1])
