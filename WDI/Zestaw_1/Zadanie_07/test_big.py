# Mikołaj Maślak
import pytest
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint
from ....readstdout import checkstdout

MIN_RANGE = 100000
MAX_RANGE = 10000000
TEST_NUM = 100
BIG_RANDOM_TESTS = [
    (randint(MIN_RANGE, MAX_RANGE),)
    for _ in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_big_s1t07", depends=["test_basic_s1t07"], scope="session")
class TestBig:
    @pytest.mark.parametrize("data", BIG_RANDOM_TESTS)
    def test_big_random(self, data):
        assert checkstdout(user_sol, corr_sol, data, float_type=False)
