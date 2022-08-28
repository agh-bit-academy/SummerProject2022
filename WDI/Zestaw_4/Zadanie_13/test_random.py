# Andrzej Karciński
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol
import pytest

MIN_RANGE = 1000
MAX_RANGE = 10000
SIZE = 20
TEST_NUM = 80
TEST_RANDOM = [
    [RandFixArray(SIZE, MIN_RANGE, MAX_RANGE).get() for __ in range(SIZE)]
    for _ in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="s4t13_test_random", depends=["s4t13_test_basic"], scope="session")
@pytest.mark.parametrize("data", TEST_RANDOM)
def test_random(data):
    assert user_sol(data) == corr_sol(data)
