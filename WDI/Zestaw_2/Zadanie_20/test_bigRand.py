# Andrzej Karciński
import pytest
from random import randint
from ....readstdout import checkstdout
from .prog import f as user_sol
from .sol import f as corr_sol

MIN_RANGE = 1
MAX_RANGE = 10 ** 6
TEST_NUM = 100
BIG_RAND_TESTS = [
    (randint(MIN_RANGE, MAX_RANGE),
     randint(MIN_RANGE, MAX_RANGE))
    for _ in range(TEST_NUM)]

SHIFT = 1000
L_BOUND = MIN_RANGE + SHIFT
U_BOUND = MAX_RANGE - SHIFT
BIG_RAND_RANGE_TESTS = [
    (randint(MIN_RANGE, L_BOUND),
     randint(U_BOUND, MAX_RANGE))
    for _ in range(TEST_NUM)]


@pytest.mark.order(3)
@pytest.mark.dependency(name="test_big_rand_s2t20", depends=["test_small_rand_s2t20"], scope="session")
class TestBig:
    @pytest.mark.parametrize("data", BIG_RAND_TESTS)
    def test_big_rand(self, data):
        assert checkstdout(user_sol, corr_sol, data, float_type=False)

    @pytest.mark.parametrize("data", BIG_RAND_RANGE_TESTS)
    def test_big_rand_range(self, data):
        assert checkstdout(user_sol, corr_sol, data, float_type=False)
