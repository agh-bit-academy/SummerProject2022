# Karol Sewiło
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol

BASIC_TESTS = [
    [],
    [3],
    [9],
    [0, 0],
    [1, 1, 1],
    [4, 2, 0],
    [2, 1, 3, 7],
    [-2, -1, -3, -7],
    [10001, 3, 2, 7],
    [2, 7, 3, 11, 13, 101, 23]
]

SIZE = 10
LEFT_RANGE = -200
RIGHT_RANGE = 200
TEST_NUM = 40

BASIC_RANDOM_TESTS = [RandFixArray(SIZE, LEFT_RANGE, RIGHT_RANGE).get() for _ in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s3t20", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", BASIC_TESTS)
    def test_basic(self, data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
    def test_basic_random(self, data):
        assert user_sol(data) == corr_sol(data)
