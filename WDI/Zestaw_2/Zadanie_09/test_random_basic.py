# Radek Niżnik

import pytest
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint


MIN_RANGE = 2
MAX_RANGE = 1000000
TEST_NUM = 90
SET_PRECISION = 10 ** (-2)
BASIC_RANDOM_TESTS = [
    randint(MIN_RANGE, MAX_RANGE)
    for _ in range(TEST_NUM)]


@pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
def test_rand(data):
    assert abs(user_sol(data) - corr_sol(data)) < SET_PRECISION
