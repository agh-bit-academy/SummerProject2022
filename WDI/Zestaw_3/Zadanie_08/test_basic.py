# Maciej Sieniek
import pytest
from ....Rand_Templates import RandFixArray as randArr
from .prog import f as user_sol
from .sol import f as corr_sol

BASIC_TESTS = [
    [2, 0, 0],
    [1, 0, 0],
    [3, 0, 0],
    [6, 0, 3, 2, 0, 1],
    [5, 5, 5, 5, 5, 5]
]

MIN_RANGE = 0
MAX_RANGE = 100
LIST_RANGE = 50
TEST_NUM = 25
FIXED = True
BASIC_RANDOM_TESTS = [
    randArr.RandFixArray(LIST_RANGE, MIN_RANGE, MAX_RANGE, fixed=FIXED).get()
    for _ in range(TEST_NUM)
]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s3t8", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", BASIC_TESTS)
    def test_basic(self, data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
    def test_basic_random(self, data):
        assert user_sol(data) == corr_sol(data)
