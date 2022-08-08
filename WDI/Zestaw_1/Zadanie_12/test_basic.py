# Mikołaj Maślak
import pytest
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint
from ....readstdout import checkstdout

MIN_RANGE = 1
MAX_RANGE = 1000
TEST_NUM = 100
BASIC_RANDOM_TESTS = [
    (randint(MIN_RANGE, MAX_RANGE),
     randint(MIN_RANGE, MAX_RANGE),
     randint(MIN_RANGE, MAX_RANGE))
    for _ in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s1t12", scope="session")
@pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
def test_basic(self, data):
    assert checkstdout(user_sol, corr_sol, data, float_type=False)
