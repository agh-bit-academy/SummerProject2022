# Andrzej Karciński
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint
import pytest

MIN_RANGE = 100
MAX_RANGE = 200
SIZE = 20
TEST_NUM = 100
TEST_RANDOM = [
    ([RandFixArray(SIZE, MIN_RANGE, MAX_RANGE).get() for __ in range(SIZE)], randint(MAX_RANGE, MAX_RANGE ** 2))
    for _ in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="s4t19_test_big", depends=["s4t19_test_basic"], scope="session")
@pytest.mark.parametrize("data", TEST_RANDOM)
def test_big(data):
    assert user_sol(data[0], data[1]) == corr_sol(data[0], data[1])
