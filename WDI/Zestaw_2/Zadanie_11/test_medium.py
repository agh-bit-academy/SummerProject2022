# Krzysztof Wysocki
import pytest
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

MIN_RANGEE = 10**3
MAX_RANGE = 10**6
AMOUNT = 10
TESTS = [randint(MIN_RANGEE, MAX_RANGE) for i in range(AMOUNT)]


@pytest.mark.order(2)
@pytest.mark.parametrize("data", TESTS)
def test_medium(data):
    assert user_sol(data) == corr_sol(data)
