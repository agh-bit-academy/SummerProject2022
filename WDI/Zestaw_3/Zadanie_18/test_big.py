# Mikołaj Maślak
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol

SIZE = 1000
TEST_NUM = 50
MIN_RANGE = 1
MAX_RANGE = 100

BIG_RANDOM_TEST = [RandFixArray(SIZE, MIN_RANGE, MAX_RANGE).get() for _ in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_big_s3t18", depends=["test_basic_s3t18"], scope="session")
@pytest.mark.parametrize("data", BIG_RANDOM_TEST)
def test_basic(data):
    assert user_sol(data) == corr_sol(data)
