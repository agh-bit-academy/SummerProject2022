# Juliusz Wasieleski
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol

SIZE = 10 ** 4
LRANGE = -1000
RRANGE = 1000
TEST_NUM = 100

SMALL_RANDOM_TESTS = [RandFixArray(SIZE, LRANGE, RRANGE).get() for _ in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_random_s3t19", depends=["test_basic_s3t19"], scope="session")
@pytest.mark.parametrize("data", SMALL_RANDOM_TESTS)
def test_small_random(data):
    assert user_sol(data) == corr_sol(data)
