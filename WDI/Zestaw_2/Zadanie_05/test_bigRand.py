# Karol Sewiło
import pytest
from ....readstdout import checkstdout
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

MIN_RANGE_NUMBER = 0
MAX_RANGE_NUMBER = 10 ** 10
MIN_RANGE_DIVISOR = 1
MAX_RANGE_DIVISOR = 10 ** 3
TEST_NUM = 100
BIG_RAND_TESTS = [
    (randint(MIN_RANGE_NUMBER, MAX_RANGE_NUMBER),
     randint(MIN_RANGE_DIVISOR, MAX_RANGE_DIVISOR))
    for _ in range(TEST_NUM)]


@pytest.mark.order(3)
@pytest.mark.dependency(name="test_big_rand_s2t05", depends=["test_small_rand_s2t05"], scope="session")
@pytest.mark.parametrize("data", BIG_RAND_TESTS)
def test_big_rand(data):
    assert checkstdout(user_sol, corr_sol, data, float_type=True)

