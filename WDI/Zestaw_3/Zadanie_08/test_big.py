# Maciej Sieniek
import pytest
from ....Rand_Templates import RandFixArray as randArr
from .prog import f as user_sol
from .sol import f as corr_sol


MIN_RANGE = 0
MAX_RANGE = 10 ** 4
LIST_RANGE = 10 ** 3
TEST_NUM = 70
FIXED = True
BIG_RANDOM_TESTS = [
    randArr.RandFixArray(LIST_RANGE, MIN_RANGE, MAX_RANGE, fixed=FIXED).get()
    for _ in range(TEST_NUM)
]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_big_s3t8", depends=["test_basic_s3t8"], scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", BIG_RANDOM_TESTS)
    def test_big_random(self, data):
        assert user_sol(data) == corr_sol(data)
