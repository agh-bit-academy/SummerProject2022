# Karolina Kucia
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol


SIZE = 50
LRANGE = 0
RRANGE = 10 ** 3
TEST_NUM = 20

SMALL_RANDOM_TESTS = [[RandFixArray(SIZE, LRANGE, RRANGE).get() for _ in range(SIZE)] for _ in range(TEST_NUM)]


@pytest.mark.order(3)
@pytest.mark.dependency(name="test_small_s4t02", depends=["test_basic_s4t02"], scope="session")
@pytest.mark.parametrize("data", SMALL_RANDOM_TESTS)
def test_small_random(data):
    assert user_sol(data) == corr_sol(data)
