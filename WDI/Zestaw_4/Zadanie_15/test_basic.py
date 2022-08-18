# Szczepan Rzeszutek
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol

TEST_BASIC = [
    [[0]],
    [[1, 4, 5], [5, 7, 5], [3, 6, 7]],
]
SIZE = 100
START = 0
END = 100
TEST_NUM = 10
TEST_BASIC_RANDOM = [[RandFixArray(SIZE, START, END).get() for _ in range(SIZE)] for _ in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s4t15", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", TEST_BASIC)
    def test_basic(self, data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize("data", TEST_BASIC_RANDOM)
    def test_basic_random(self, data):
        assert user_sol(data) == corr_sol(data)
