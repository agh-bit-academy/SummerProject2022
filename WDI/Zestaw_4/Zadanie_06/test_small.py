# Krzysztof Wysocki
import pytest
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

MIN_RANGEE = 1
MAX_RANGE = 100
AMOUNT_1 = 10
AMOUNT_2 = 10


TESTS = []
for i in range(AMOUNT_1):
    tab = [randint(MIN_RANGEE, MAX_RANGE) for i in range(AMOUNT_2)]
    tab = sorted(tab)
    TESTS.append(tab)


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_small_s4t06", scope="session")
@pytest.mark.parametrize("data", TESTS)
def test_small(data):
    assert sorted(user_sol([data])) == sorted(corr_sol([data]))
