# Mikołaj Maślak
import pytest
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

MIN_RANGE = 1
MAX_RANGE = 10000
TEST_NUM = 100
BASIC_RANDOM_TESTS = [
    randint(MIN_RANGE, MAX_RANGE)
    for _ in range(TEST_NUM)]


@pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
def test_basic(data):
    assert user_sol(data) == corr_sol(data)
