# Paweł Konopka

import pytest
from ....readstdout import checkstdout
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint


MIN_RANGE = 100_000
MAX_RANGE = 200_000
TEST_NUM = 3
BIG_TESTS_A = [
    [randint(MIN_RANGE, MAX_RANGE)] for _ in range(TEST_NUM)
    ]

MIN_RANGE = 250_000
MAX_RANGE = 400_000
BIG_TEST_B = [randint(MIN_RANGE, MAX_RANGE)]

MIN_RANGE = 500_000
MAX_RANGE = 800_000
BIG_TEST_C = [randint(MIN_RANGE, MAX_RANGE)]


@pytest.mark.order(3)
@pytest.mark.dependency(name="testBig_s2z16", scope="session")
class TestBig:
    @pytest.mark.parametrize("data", BIG_TESTS_A)
    def test_big_a(self, data):
        assert checkstdout(user_sol, corr_sol, data, float_type=True)

    def test_big_b(self):
        assert checkstdout(user_sol, corr_sol, BIG_TEST_B, float_type=True)

    def test_big_c(self):
        assert checkstdout(user_sol, corr_sol, BIG_TEST_C, float_type=True)
