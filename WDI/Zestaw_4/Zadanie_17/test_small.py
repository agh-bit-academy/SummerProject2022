# Karolina Kucia
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .check import check


SIZE = 50
LRANGE = 1
RRANGE = 10 ** 3
TEST_NUM = 25

SMALL_RANDOM_TESTS = [[RandFixArray(SIZE, LRANGE, RRANGE).get() for _ in range(SIZE)] for _ in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_small_s4t17", depends=["test_basic_s4t17"], scope="session")
@pytest.mark.parametrize("data", SMALL_RANDOM_TESTS)
def test_small_random(data):
    assert user_sol(data) in check(data)
