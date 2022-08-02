# Paweł Konopka

import pytest
from ....readstdout import checkstdout
from .prog import f as user_sol
from .gener_sol import f as corr_sol
from random import randint

BASIC_TESTS = [
    [5],
    [0],
    [25],
    [90],
    [100]
    ]

MIN_RANGE = 100
MAX_RANGE = 1_500
TEST_NUM = 25
BASIC_RANDOM_TESTS = [
    [randint(MIN_RANGE, MAX_RANGE)] for _ in range(TEST_NUM)
    ]


@pytest.mark.order(1)
@pytest.mark.dependency(name="testBasic_s2z16", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", BASIC_TESTS)
    def test_basic(self, data):
        assert checkstdout(user_sol, corr_sol, data, float_type=True)

    @pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
    def test_basic_random(self, data):
        assert checkstdout(user_sol, corr_sol, data, float_type=True)
