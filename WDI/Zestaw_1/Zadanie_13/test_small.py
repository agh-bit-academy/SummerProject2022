# Krzysztof Wysocki
import pytest
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

MIN_RANGEE = 1
MAX_RANGE = 10**2
AMOUNT = 10
TESTS = [
    (
        randint(MIN_RANGEE, MAX_RANGE),
        randint(MIN_RANGEE, MAX_RANGE),
        randint(MIN_RANGEE, MAX_RANGE),
    )
    for i in range(AMOUNT)
]


@pytest.mark.order(1)
class TestSmall:
    @pytest.mark.parametrize("a,b,c", TESTS)
    def test_small(self, a, b, c):
        assert user_sol(a, b, c) == corr_sol(a, b, c)
