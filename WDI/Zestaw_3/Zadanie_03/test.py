# Andrzej Karciński
import pytest
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

MIN_RANGE = 10 ** 3
MAX_RANGE = 10 ** 6
TEST_NUM = 100
TEST = [
    randint(MIN_RANGE, MAX_RANGE)
    for _ in range(TEST_NUM)]

@pytest.mark.parametrize("data", TEST)
def test_rand(data):
    assert user_sol(data) == corr_sol(data)
