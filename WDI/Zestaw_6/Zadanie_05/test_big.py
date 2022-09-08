# Sebastian Soczawa
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint


SIZE = 35
SHIFT = 10
LRANGE = 0
RRANGE = 1
TEST_NUM = 40

BIG_RANDOM_TESTS = [RandFixArray(SIZE + randint(-SHIFT, SHIFT), LRANGE, RRANGE).get()
                    for _ in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_big_s4t02", depends=["test_basic_s4t02"], scope="session")
@pytest.mark.parametrize("data", BIG_RANDOM_TESTS)
def test_big_random(data):
    assert user_sol(data) == corr_sol(data)
