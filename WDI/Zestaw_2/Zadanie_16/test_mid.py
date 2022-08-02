# Paweł Konopka

import pytest
from ....readstdout import checkstdout
from .prog import f as user_sol
from .gener_sol import f as corr_sol
from random import randint


MIN_RANGE = 1_500
MAX_RANGE = 10_000
TEST_NUM = 80
MID_TESTS_A = [
    [randint(MIN_RANGE, MAX_RANGE)] for _ in range(TEST_NUM)
    ]

MIN_RANGE = 10_000
MAX_RANGE = 50_000
TEST_NUM = 15
MID_TESTS_B = [
    [randint(MIN_RANGE, MAX_RANGE)] for _ in range(TEST_NUM)
    ]

MIN_RANGE = 50_000
MAX_RANGE = 100_000
TEST_NUM = 5
MID_TESTS_C = [
    [randint(MIN_RANGE, MAX_RANGE)] for _ in range(TEST_NUM)
    ]


@pytest.mark.order(2)
@pytest.mark.dependency(name="testMid_s2z16", scope="session")
class TestMid:
    @pytest.mark.parametrize("data", MID_TESTS_A)
    def test_mid_a(self, data):
        assert checkstdout(user_sol, corr_sol, data, float_type=True)

    @pytest.mark.parametrize("data", MID_TESTS_B)
    def test_mid_b(self, data):
        assert checkstdout(user_sol, corr_sol, data, float_type=True)

    @pytest.mark.parametrize("data", MID_TESTS_C)
    def test_mid_c(self, data):
        assert checkstdout(user_sol, corr_sol, data, float_type=True)
