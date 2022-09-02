# Krzysztof Wysocki
import pytest
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

MIN_RANGE = 20
MAX_RANGE = 40
AMOUNT = 10


TESTS = [randint(MIN_RANGE, MAX_RANGE) for i in range(AMOUNT)]


@pytest.mark.order(2)
@pytest.mark.dependency(
    name="test_medium_s6t13", depends=["test_small_s6t13"], scope="session"
)
@pytest.mark.parametrize("data", TESTS)
def test_medium(data):
    assert user_sol(data) == corr_sol(data)
