# Karolina Kucia
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol


BASIC_TESTS = [
    [[0, 0], [0, 0]],
    [[9, 6], [3, 11]],
    [[-1, -2], [2, 1]],
    [[-64, -22], [-16, -18]],
    [[0, 1, 2], [3, 4, 5], [6, 7, 8]],
    [[-10, -1, -2], [-3, -4, -5], [-6, -7, -8]],
    [[-8, 2, -91], [64, 24, -88], [-99, 66, 11]],
    [[1, 3, 1, 3, 1], [3, 1, 3, 3, 3], [1, 3, 1, 3, 1], [3, 3, 3, 1, 3], [1, 3, 1, 3, 1]],
    [1, 1, -9, 1, -9], [1, 1, 1, -100, 1], [-9, 1, -9, 1, -9], [1, -100, 1, 1, 1], [-9, 1, -9, 1, 1]
]

SIZE = 10
LRANGE = -100
RRANGE = 100
TEST_NUM = 21

BASIC_RANDOM_TESTS = [[RandFixArray(SIZE, LRANGE, RRANGE).get() for _ in range(SIZE)] for _ in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s4t20", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", BASIC_TESTS)
    def test_basic(self, data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
    def test_basic_random(self, data):
        assert user_sol(data) == corr_sol(data)
