# Dominik Adamczyk

import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .check import check
from random import randint

MIN_SIZE = 13
MAX_SIZE = 20
LRANGE = 1
RRANGE = 30
TEST_NUM = 20

BIG_RAND_TESTS = [RandFixArray(randint(MIN_SIZE, MAX_SIZE), LRANGE, RRANGE).get() for _ in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_big_s6t06", depends=["test_basic_s6t06"], scope="session")
@pytest.mark.parametrize("data", BIG_RAND_TESTS)
def test_big(data):
    solutions = check(data)
    if len(solutions) == 0:
        assert user_sol(data) is None
    else:
        assert user_sol(data) in solutions
