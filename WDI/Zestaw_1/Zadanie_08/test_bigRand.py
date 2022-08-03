# Bartłomiej Kozera
import pytest
from ....readstdout import checkstdout
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

MIN_RANGE = 10**4
MAX_RANGE = 10**6
TEST_NUM = 30
SMALL_RANDOM_TESTS = [(randint(MIN_RANGE, MAX_RANGE),) for _ in range(TEST_NUM)]


@pytest.mark.order(3)
@pytest.mark.dependency(name="test_big_rand_s1t8", depends=["test_small_rand_s1t8"], scope="session")
@pytest.mark.parametrize("data", SMALL_RANDOM_TESTS)
def test_big_random(data):
    assert checkstdout(user_sol, corr_sol, data, float_type=False)
