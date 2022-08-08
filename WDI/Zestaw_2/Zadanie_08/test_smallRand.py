# Juliusz Wasieleski
import pytest
from ....readstdout import checkstdout
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

MIN_RANGE = 0
MAX_RANGE = 5000
TEST_NUM = 100
SMALL_RAND_TESTS = [
    [randint(MIN_RANGE, MAX_RANGE)]
    for _ in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_small_rand_s2t08", depends=["test_basic_s2t08"], scope="session")
@pytest.mark.parametrize("data", SMALL_RAND_TESTS)
def test_small_rand(data):
    assert checkstdout(user_sol, corr_sol, data, float_type=False)
