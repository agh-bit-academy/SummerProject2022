# Karolina Kucia
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol


SIZE = 100
LRANGE = 0
RRANGE = 10 ** 6
TEST_NUM = 20

BIG_RANDOM_TESTS = [[RandFixArray(SIZE, LRANGE, RRANGE).get() for _ in range(SIZE)] for _ in range(TEST_NUM)]


@pytest.mark.order(3)
@pytest.mark.dependency(name="test_big_s4t02", depends=["test_small_s4t02"], scope="session")
@pytest.mark.parametrize("data", BIG_RANDOM_TESTS)
def test_big_random(data):
    assert user_sol(data) == corr_sol(data)
