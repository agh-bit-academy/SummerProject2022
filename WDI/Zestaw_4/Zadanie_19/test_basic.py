# Andrzej Karciński
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint
import pytest

TEST_BASIC = [
    ([[1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1]], 1),

    ([[1]], 1),

    ([[1, 1],
      [1, 1]], 1)

    ([[1, 2, 1],
      [2, 5, 6],
      [7, 8, 4]], 8),

    ([[421, 21, 1, 7, 9, 82],
      [1, 3, 9, 32, 2137, 1],
      [32, 1, 512, 9, 8, 51],
      [12, 16, 16, 26, 1, 1]], 512)
]

MIN_RANGE = 1
MAX_RANGE = 20
SIZE = 5
TEST_NUM = 20
TEST_RANDOM = [
    ([RandFixArray(SIZE, MIN_RANGE, MAX_RANGE).get() for __ in range(SIZE)], randint(MAX_RANGE, MAX_RANGE ** 2))
    for _ in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="s4t19_test_basic", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", TEST_BASIC)
    def test_basic(self, data):
        assert user_sol(data[0], data[1]) == corr_sol(data[0], data[1])

    @pytest.mark.parametrize("data", TEST_RANDOM)
    def test_random(self, data):
        assert user_sol(data[0], data[1]) == corr_sol(data[0], data[1])
