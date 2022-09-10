# Sebastian Soczawa
import pytest
from random import randint
from ....Rand_Templates.RandFixArray import RandFixArray
from .sol import f as corr_sol
from .prog import f as user_sol


INIT_TESTS = [([1, 1, 1], 3, True),
              ([1, 2, 2], 6, False),
              ([0, 2, 2], 1, True),
              ([1, 1, 0, 1], 3, True),
              ([5, 5, 5], 25, False),
              ([0, 0, 0], 0, True),
              ([1, 1, 1, 1, 1, 1, 1], 5, False),
              ([3, 3, 3], 1, True),
              ([0, 2, 1, 3, 1, 8], 0, True),
              ([2, 2, 4], 5, True),
              ([2, 4, 2], 5, True),
              ([4, 2, 2], 5, True),
              ([4, 2, 2], 6, False)]
LRANGE = 0
RRANGE = 20
SIZE = 10
TEST_NUM = 27
TEST_TAB = RandFixArray(SIZE, LRANGE, RRANGE).get()
BASIC_RAND_TESTS = [[TEST_TAB, randint(LRANGE, RRANGE)]
                    for _ in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s6t23", scope="session")
class TestBasic:
    @pytest.mark.parametrize("tab, res, sol", INIT_TESTS)
    def test_init(self, tab, res, sol):
        assert user_sol(tab, res) == sol

    @pytest.mark.parametrize("tab, res", BASIC_RAND_TESTS)
    def test_rand(self, tab, res):
        assert user_sol(tab, res) == corr_sol(tab, res)
