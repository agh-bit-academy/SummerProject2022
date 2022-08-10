# Sebastian Soczawa
import pytest
from ....readstdout import checkstdout
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

BASIC_RANDOM_TESTS = [randint(1, 100) for _ in range(20)]

MIN_RANGE = 10**10
MAX_RANGE = 10**15
TEST_NUM = 80
BIG_RANDOM_TESTS = [
    randint(MIN_RANGE, MAX_RANGE)
    for _ in range(TEST_NUM)
]

@pytest.mark.dependency(name="test_basic_s2ex7", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
    def test_basic(self, data):
        assert checkstdout(user_sol, corr_sol, [data])

    @pytest.mark.parametrize("data", BIG_RANDOM_TESTS)
    def test_basic_random(self, data):
        assert checkstdout(user_sol, corr_sol, [data])
