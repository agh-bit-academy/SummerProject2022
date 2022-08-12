# Juliusz Wasieleski
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol

BIG_SIZE = 10**4
BIG_LRANGE = -10**8
BIG_RRANGE = 10**8
TEST_NUM = 100

BIG_RANDOM_TESTS = [RandFixArray(BIG_SIZE, BIG_LRANGE, BIG_RRANGE).get()
                    for _ in range(TEST_NUM)]


@pytest.mark.order(3)
@pytest.mark.dependency(name="test_random_s3t19", depends=["test_basic_s3t19"], scope="session")
@pytest.mark.parametrize("data", BIG_RANDOM_TESTS)
def test_big_random(data):
    assert user_sol(data) == corr_sol(data)
