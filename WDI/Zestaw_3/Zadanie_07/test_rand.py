# Dominik Adamczyk
import pytest
from .prog import f as user_sol
from .check import f as corr_sol
from random import randint


MIN_LEN_SMALL = 1
MAX_LEN_SMALL = 10
MIN_LEN_BIG = 1000
MAX_LEN_BIG = 10000
TEST_NUM = 20
SMALL_RANDOM_TESTS = [randint(MIN_LEN_SMALL, MAX_LEN_SMALL)for _ in range(TEST_NUM)]

BIG_RANDOM_TESTS = [randint(MIN_LEN_BIG, MAX_LEN_BIG) for _ in range(TEST_NUM)]


@pytest.mark.order(1)
class TestRandom:
    @pytest.mark.parametrize("data", SMALL_RANDOM_TESTS)
    def test_small(self, data):
        arr, ans = user_sol(data)
        assert ans == corr_sol(arr)

    @pytest.mark.parametrize("data", BIG_RANDOM_TESTS)
    def test_big(self, data):
        arr, ans = user_sol(data)
        assert ans == corr_sol(arr)
