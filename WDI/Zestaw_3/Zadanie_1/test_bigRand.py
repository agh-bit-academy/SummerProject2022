# Karolina Kucia
import pytest
from random import randint
from .prog import f as user_sol
from .sol import f as corr_sol


MIN_RANGE = 10**3
MAX_RANGE = 10**6
TEST_NUM = 20
BASE_LRANGE = 2
BASE_RRANGE = 16

BIG_RANDOM_TESTS = [
    (randint(MIN_RANGE, MAX_RANGE), randint(BASE_LRANGE, BASE_RRANGE))
    for _ in range(TEST_NUM)]


@pytest.mark.order(3)
@pytest.mark.dependency(name="test_big_s3t1", depends=["test_small_s3t1"], scope="session")
@pytest.mark.parametrize("data", BIG_RANDOM_TESTS)
def test_basic_random(data):
    assert user_sol(data) == corr_sol(data)
