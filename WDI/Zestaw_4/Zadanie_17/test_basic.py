# Karolina Kucia
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol


BASIC_TESTS = [
    [[1]],
    [[2, 2], [2, 2]]
    [[1, 2, 3], [4, 5, 6], [8, 9, 10]],
    [[6, 6, 6], [6, 6, 6], [6, 6, 6]],
    [[1, 5, 5, 5], [1, 5, 1, 5], [1, 5, 5, 5], [1, 1, 1, 1]],
    [[9, 8, 9, 8, 9], [8, 9, 8, 9, 8], [9, 8, 9, 8, 9], [8, 9, 8, 9, 8], [9, 8, 9, 8, 9]]
]

SIZE_ROW = 10
SIZE_COL = 12
LRANGE = 1
RRANGE = 100
TEST_NUM = 20

BASIC_RANDOM_TESTS = [[RandFixArray(SIZE_ROW, LRANGE, RRANGE).get() for _ in range(SIZE_COL)] for _ in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s4t17", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", BASIC_TESTS)
    def test_basic(self, data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
    def test_basic_random(self, data):
        assert user_sol(data) == corr_sol(data)
