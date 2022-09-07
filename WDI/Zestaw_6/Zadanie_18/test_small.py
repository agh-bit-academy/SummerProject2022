# Juliusz Wasieleski
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol

BASIC_TESTS = [
    [[]],
    [[1]],
    [[1, 4, 6, 2, 3, 5, 35, 2],
     [1, 4, 6, 2, 3, 5, 35, 2],
     [1, 4, 6, 82, 3, 5, 35, 2],
     [1, 4, 6, 2, 3, 5, 35, 2],
     [1, 4, 6, 2, 3, 5, 91, 2],
     [1, 4, 6, 82, 3, 5, 24, 2],
     [1, 4, 6, 2, 3, 5, 35, 7],
     [1, 4, 6, 2, 3, 5, 35, 8]],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6],
     [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6],
     [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6],
     [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6],
     [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6],
     [2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5],
     [3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4],
     [4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3],
     [5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2],
     [6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1],
     [7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
     [8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1]],
    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
     [1, 1, 1, 1, 1, 1, 1, 1, 5, 1, 1]]
]

SIZE = 10
LRANGE = 0
RRANGE = 100
TEST_NUM = 35

BASIC_RANDOM_TESTS = [[RandFixArray(SIZE, LRANGE, RRANGE).get() for _ in range(SIZE)] for _ in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_small_s6t18", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", BASIC_TESTS)
    def test_basic(self, data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
    def test_basic_random(self, data):
        assert user_sol(data) == corr_sol(data)
