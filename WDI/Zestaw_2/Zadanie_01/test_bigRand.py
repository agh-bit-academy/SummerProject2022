# Kacper Słoniec
import pytest
from ....readstdout import checkstdout
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

MIN_RANGE = 1
MAX_RANGE = 10 ** 6
TEST_NUM = 100
BIG_RAND_TESTS = [
    (randint(MIN_RANGE, MAX_RANGE), )
    for _ in range(TEST_NUM)]


@pytest.mark.order(3)
@pytest.mark.dependency(name="test_big_rand_s2t1", depends=["test_small_rand_s2t1"], scope="session")
class TestBig:
    @pytest.mark.parametrize("data", BIG_RAND_TESTS)
    def test_big_rand(self, data):
        assert checkstdout(user_sol, corr_sol, data, float_type=False)
