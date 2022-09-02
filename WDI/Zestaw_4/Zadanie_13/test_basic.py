# Andrzej Karciński
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol
import pytest

MIN_RANGE = 10
MAX_RANGE = 20
SIZE = 4
TEST_NUM = 10
TEST_RANDOM = [
    [RandFixArray(SIZE, MIN_RANGE, MAX_RANGE).get() for __ in range(SIZE)]
    for _ in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="s4t13_test_basic", scope="session")
@pytest.mark.parametrize("data", TEST_RANDOM)
def test_basic(data):
    assert user_sol(data) == corr_sol(data)
