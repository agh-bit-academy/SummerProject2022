# Karolina Kucia
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol


BASIC_TESTS = [
    [],
    [0],
    [1, 1, 1],
    [1, 2, 3],
    [9, 9, 7],
    [2, 1, 3, 7],
    [2, -3, -3, 1, 3, -3],
    [0, 11, 0, 11, 0, 11],
    [90, 80, 0, 70, 100, 60, 50, 40, 30, 20, 10]
]

SIZE = 100
LRANGE = -100
RRANGE = 100
TEST_NUM = 41

BASIC_RANDOM_TESTS = [RandFixArray(SIZE, LRANGE, RRANGE).get() for _ in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s3t16", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", BASIC_TESTS)
    def test_basic(self, data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
    def test_basic_random(self, data):
        assert user_sol(data) == corr_sol(data)
