import pytest
from ....Rand_Templates.RandFixArray import RandFixArray as RandArr
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

TEST_NUM = 20
LRANGE = 10**2
RRANGE = 10**4
MIN_SIZE = 10
MAX_SIZE = 20
TEST_MED = [RandArr(randint(MIN_SIZE, MAX_SIZE), LRANGE, RRANGE).get() for _ in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name='test_s6t2_med', depends=['test_s6t2_basic'], scope='session')
@pytest.mark.parametrize('data', TEST_MED)
def test_med_random(data):
    assert user_sol(data) == corr_sol(data)
