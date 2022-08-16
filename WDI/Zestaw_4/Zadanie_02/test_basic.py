# Karolina Kucia
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol


BASIC_TESTS = [
    [[]],
    [[0]],
    [[1]],
    [[-13]],
    [[9, 6], [3, 11]],
    [[64, 22], [16, 18]],
    [[-1, -2], [2, 1]],
    [[99, 82, 62, 15], [81, 15, 23, 16]],
    [[8, 2, 91], [64, 24, 88], [99, 66, 11]],
    [[12, 34, 56], [78, 90, 10], [32, 47, 91]],
    [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14]]
]

SIZE = 10
LRANGE = -100
RRANGE = 100
TEST_NUM = 20

BASIC_RANDOM_TESTS = [[RandFixArray(SIZE, LRANGE, RRANGE).get() for _ in range(SIZE)] for _ in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s4t02", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", BASIC_TESTS)
    def test_basic(self, data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
    def test_basic_random(self, data):
        assert user_sol(data) == corr_sol(data)
