# Sebastian Soczawa
import pytest
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

BASIC_MIN_RANGE = 1
BASIC_MAX_RANGE = 1000
BASIC_TEST_NUM = 20
BASIC_RANDOM_TESTS = [
    randint(BASIC_MIN_RANGE, BASIC_MAX_RANGE)
    for _ in range(BASIC_TEST_NUM)
]

BIG_MIN_RANGE = 10**10
BIG_MAX_RANGE = 10**15
BIG_TEST_NUM = 80
BIG_RANDOM_TESTS = [
    randint(BIG_MIN_RANGE, BIG_MAX_RANGE)
    for _ in range(BIG_TEST_NUM)
]


@pytest.mark.dependency(name="test_basic_s2ex7", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
    def test_basic(self, data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize("data", BIG_RANDOM_TESTS)
    def test_basic_random(self, data):
        assert user_sol(data) == corr_sol(data)
