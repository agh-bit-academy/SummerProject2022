# Krzysztof Wysocki
import pytest
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

MIN_RANGE = 10
MAX_RANGE = 10**9
AMOUNT_1 = 10**2
AMOUNT = 10

TESTS = [
    [randint(MIN_RANGE, MAX_RANGE) for i in range(AMOUNT_1)] for j in range(AMOUNT)
]


@pytest.mark.order(2)
@pytest.mark.dependency(
    name="test_medium_s3t05", depends=["test_small_s3t05"], scope="session"
)
@pytest.mark.parametrize("data", TESTS)
def test_medium(data):
    assert user_sol(data) == corr_sol(data)
