from ....readstdout import checkstdout
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint
import pytest

FRIENDLY_NUMBERS = [
    [220, 284],
    [1184, 1210],
    [2620, 2924],
    [5020, 5564],
    [6232, 6368],
    [10744, 10856],
    [12285, 14595],
    [17296, 18416],
    [63020, 76084],
    [66928, 66992]]

MIN_RANGE = 10
MAX_RANGE = 10 ** 6
TEST_NUM = 90
TEST_RANDOM = [
    [randint(MIN_RANGE, MAX_RANGE), randint(MIN_RANGE, MAX_RANGE)]
    for _ in range(TEST_NUM)]


class Test:
    @pytest.mark.parametrize("data", FRIENDLY_NUMBERS)
    def test_basic(self, data):
        assert checkstdout(user_sol, corr_sol, data)

    @pytest.mark.parametrize("data", TEST_RANDOM)
    def test_random(self, data):
        assert checkstdout(user_sol, corr_sol, data)
