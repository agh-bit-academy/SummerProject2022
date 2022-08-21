# Krzysztof Wysocki
import pytest
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

MIN_RANGEE = 10**2
MAX_RANGE = 100**9
AMOUNT_1 = 10
AMOUNT_2 = 10**5


TESTS = []
for i in range(AMOUNT_1):
    tab = [randint(MIN_RANGEE, MAX_RANGE) for i in range(AMOUNT_2)]
    tab = sorted(tab)
    TESTS.append(tab)


@pytest.mark.order(3)
@pytest.mark.dependency(
    name="test_big_s4t06", depends=["test_medium_s4t06"], scope="session"
)
@pytest.mark.parametrize("data", TESTS)
def test_big(data):
    assert sorted(user_sol([data])) == sorted(corr_sol([data]))
