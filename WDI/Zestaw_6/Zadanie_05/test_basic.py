# Sebastian Soczawa
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint


BASIC_TESTS = [
    ([0], False),
    ([1], False),
    ([1, 0, 0, 1, 1, 1, 1], True),
    ([1, 1, 1, 1, 1], True),
    ([1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1], True),
    ([1, 1, 1, 1, 1, 1], True),
    ([1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1], True),
    ([1, 0, 1, 1, 1, 1, 0, 1, 1, 1], True),
    ([1, 1, 1, 0, 1, 1, 1, 1, 1], True),
    ([1, 1, 1, 1, 0, 0, 1, 0, 0], False)
]

SIZE = 10
LRANGE = 0
RRANGE = 1
TEST_NUM = 50

BASIC_RANDOM_TESTS = [RandFixArray(SIZE + randint(0, 15), LRANGE, RRANGE).get()
                      for _ in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s4t02", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data, sol", BASIC_TESTS)
    def test_basic(self, data, sol):
        assert user_sol(data) == sol

    @pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
    def test_basic_random(self, data):
        assert user_sol(data) == corr_sol(data)
