# Szczepan Rzeszutek
import pytest
from ....readstdout import checkstdout
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

MIN_RANGE = 100
MAX_RANGE = 10000
MIN_NUM = -100000
MAX_NUM = 100000
TEST_NUM = 100
BIG_RANDOM_TESTS = [
    (randint(MIN_NUM, MAX_NUM),
     randint(MIN_NUM, MAX_NUM),
     randint(MIN_RANGE, MAX_RANGE))
    for _ in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_big_random_s2t2", depends=["test_basic_s2t2"], scope="session")
class TestBasic:
    @pytest.mark.parametrize("tests", BIG_RANDOM_TESTS)
    def test_basic(self, tests):
        assert checkstdout(user_sol, corr_sol, tests)