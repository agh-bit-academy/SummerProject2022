# Krzysztof Wysocki
import pytest
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

MIN_RANGE = 30
MAX_RANGE = 50
AMOUNT = 10


TESTS = [randint(MIN_RANGE, MAX_RANGE) for i in range(AMOUNT)]


@pytest.mark.order(3)
@pytest.mark.dependency(
    name="test_big_s6t13", depends=["test_medium_s6t13"], scope="session"
)
@pytest.mark.parametrize("data", TESTS)
def test_big(data):
    assert user_sol(data) == corr_sol(data)
