# Karolina Kucia
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol


BASIC_TESTS = [
    [[0]],
    [[1, 2], [3, 4]],
    [[6], [66], [666]],
    [[1, 11, 111], [111, 11, 1], [1111, 11, 11111]],
    [[1, 2137, 2], [7321, 11227733, 3721], [3, 3712, 4]]
]

SIZE = 10
LRANGE = 1
RRANGE = 10 ** 3
TEST_NUM = 20

BASIC_RANDOM_TESTS = [[RandFixArray(SIZE, LRANGE, RRANGE).get() for _ in range(SIZE)] for _ in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s4t11", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", BASIC_TESTS)
    def test_basic(self, data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
    def test_basic_random(self, data):
        assert user_sol(data) == corr_sol(data)
