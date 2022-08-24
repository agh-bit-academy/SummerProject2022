from ....readstdout import checkstdout
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint
import pytest

MIN_RANGE = -4
MAX_RANGE = 4
TEST_NUM = 100
TEST_RAND = [
    [randint(MIN_RANGE, MAX_RANGE)]
    for _ in range(TEST_NUM)
]


@pytest.mark.parametrize("data", TEST_RAND)
def test(data):
    assert checkstdout(user_sol, corr_sol, data, float_type=True)
