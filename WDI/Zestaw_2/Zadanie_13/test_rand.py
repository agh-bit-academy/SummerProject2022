# Izabella Rosikoń
import pytest
from .prog import unique_digit as user_sol
from .sol import unique_digit as corr_sol
from random import randint

MIN_RANGE = 100
MAX_RANGE = 1000
TEST_NUM = 100
BASIC_RANDOM_TESTS = [
    randint(MIN_RANGE, MAX_RANGE)
    for _ in range(TEST_NUM)
]

@pytest.mark.order(2)
@pytest.mark.dependency(name="test_rand_s2t13", depends=["test_basic_s2t13"], scope="session")
@pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
def test_random(data):
    assert user_sol(data) == corr_sol(data)
