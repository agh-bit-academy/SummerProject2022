# Maciej Bartczak
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol

TEST_NUM = 40
MIN_SIZE = 2
MAX_SIZE = 10 ** 2
MIN_NUM = 1
MAX_NUM = 20

TEST_SIZE = RandFixArray(TEST_NUM, MIN_SIZE, MAX_SIZE).get()
TEST_BIG = [RandFixArray(size, MIN_NUM, MAX_NUM).get() for size in TEST_SIZE]


@pytest.mark.order(2)
@pytest.mark.dependency(name='test_big_s6t22', depends=['test_basic_s6t22'], scope='session')
@pytest.mark.parametrize('data', TEST_BIG)
def test_big_rand(data):
    assert user_sol(data) == corr_sol(data)
