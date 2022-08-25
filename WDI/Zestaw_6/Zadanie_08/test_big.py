# Bartłomiej Kozera
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

TEST_NUM = 20
MIN_SIZE = 10
MAX_SIZE = 15
LLRANGE = 1
RRANGE = 10**5

WEIGHTS = RandFixArray(TEST_NUM, LLRANGE, RRANGE).get()

TEST_BIG = [(RandFixArray(randint(MIN_SIZE, MAX_SIZE), LLRANGE, RRANGE).get(), WEIGHTS[i]) for i in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name='test_big_s6t8', depends=['test_basic_s6t8'], scope='session')
@pytest.mark.parametrize('data', TEST_BIG)
def test_big_rand(data):
    assert user_sol(data[0], data[1]) == corr_sol(data[0], data[1])
