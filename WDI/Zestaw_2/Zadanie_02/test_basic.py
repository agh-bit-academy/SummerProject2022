# Szczepan Rzeszutek
import pytest
from ....readstdout import checkstdout
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

MIN_RANGE = 0
MAX_RANGE = 100
MIN_NUM = 1
MAX_NUM = 100
TEST_NUM = 100
BASIC_RANDOM_TESTS = [
    (randint(MIN_NUM, MAX_NUM),
     randint(MIN_NUM, MAX_NUM),
     randint(MIN_RANGE, MAX_RANGE))
    for _ in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s2t2", scope="session")
@pytest.mark.parametrize("tests", BASIC_RANDOM_TESTS)
def test_basic(tests):
    assert checkstdout(user_sol, corr_sol, tests)
