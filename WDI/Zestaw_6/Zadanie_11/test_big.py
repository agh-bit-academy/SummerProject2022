# Bartłomiej Kozera
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray as RandArr
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

TEST_NUM = 20
LRANGE = 10
RRANGE = 30
MIN_SIZE = 1
MAX_SIZE = 10**2
MIN_PROD = 1
MAX_PROD = 10**3
TEST_BIG = [(RandArr(randint(MIN_SIZE, MAX_SIZE), LRANGE, RRANGE).get(), randint(MIN_PROD, MAX_PROD))
            for _ in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name='test_s6t11_big', depends=['test_s6t11_basic'], scope='session')
@pytest.mark.parametrize('data', TEST_BIG)
def test_big(data):
    assert user_sol(data[0], data[1]) == corr_sol(data[0], data[1])
