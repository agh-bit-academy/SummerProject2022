# Szczepan Rzeszutek
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

TEST_BASIC = [
    ([1, 2, 3, 4, 5], 8),
    ([5, 2, 4, 3, 5], 0),
    ([3, 0, 3, 9, 4], 12),
    ([5, 2, 7, 4, 5], 1),
    ([0, 0, 0, 0, 0], 5)

]
START = 1
END = 10
TEST_NUM = 15
WEIGHT = randint(10, 20)
TEST_BASIC_RANDOM = [[RandFixArray(1, START, END).get(), WEIGHT] for _ in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s6t7", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", TEST_BASIC)
    def test_basic(self, data):
        assert user_sol(data[0], data[1]) == corr_sol(data[0], data[1])

    @pytest.mark.parametrize("data", TEST_BASIC_RANDOM)
    def test_basic_random(self, data):
        assert user_sol(data[0], data[1]) == corr_sol(data[0], data[1])
