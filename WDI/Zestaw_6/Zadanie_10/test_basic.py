# Izabella Rosikoń
from ....Rand_Templates.RandFixArray import RandFixArray
from ....Rand_Templates.RandFixMatrix import RandFixMatrix
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint
import pytest


MIN_RANGE = 0
MAX_RANGE = 100
TEST_NUM = 15
RANDOM_SIZE = [randint(1, 5) for _ in range(TEST_NUM)]

TEST_BASIC = [[[1, 2], [3, 4]],
                [[0, 1], [1, 0]],
                [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
]

TEST_BASIC_RANDOM = [RandFixMatrix(RANDOM_SIZE[i], RANDOM_SIZE[i] + 1, MIN_RANGE, MAX_RANGE).get()
                      for i in range(TEST_NUM)]

@pytest.mark.order(1)
@pytest.mark.dependency(name="s6t10_test_basic", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", TEST_BASIC)
    def test_basic(data):
        assert user_sol(data) == corr_sol(data)
    @pytest.mark.parametrize("data", TEST_BASIC_RANDOM)
    def test_basic_random(data):
        assert user_sol(data) == corr_sol(data)
