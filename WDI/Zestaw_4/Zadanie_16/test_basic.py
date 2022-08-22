#Szymon Wójcik

import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol

BASIC = [[[1,2],[2,1]]
    [[1,1,1],[1,1,22],[1,3,4]]
    [[2,3,5,7,9],[3,5,7,9,2],[5,7,9,2,3],[7,9,2,3,5],[9,2,3,5,7]]]

SIZE = 100
START = 0
END = 100
TEST_NUM = 10
BASIC_RANDOM = [[RandFixArray(SIZE, START, END).get() for _ in range(SIZE)] for _ in range(TEST_NUM)]

@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s4t15", scope="session")
class TestBasic():
    @pytest.mark.parametrize("data", BASIC)
    def test_basic(self, data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize("data", BASIC_RANDOM)
    def test_basic_random(self, data):
        assert user_sol(data) == corr_sol(data)