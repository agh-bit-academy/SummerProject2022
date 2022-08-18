# Szczepan Rzeszutek
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol

SIZE = 100
START = 10 ** 5
END = 10 ** 10
TEST_NUM = 40
TEST_BIG = [[RandFixArray(SIZE, START, END).get() for _ in range(SIZE)] for _ in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_big_s4t15", scope="session")
class TestBig:
    @pytest.mark.parametrize("data", TEST_BIG)
    def test_basic(self, data):
        assert user_sol(data) == corr_sol(data)
