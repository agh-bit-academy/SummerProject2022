# Krzysztof Wysocki
import pytest
from .prog import f as user_sol
from .sol import f as corr_sol
from random import shuffle
from random import randint

MIN_RANGEE = 10
MAX_RANGE = 10**2
AMOUNT = 10


TESTS = []
for i in range(AMOUNT):
    A, R, LGT = (
        randint(MIN_RANGEE, MAX_RANGE),
        randint(MIN_RANGEE, MAX_RANGE),
        randint(MIN_RANGEE, MAX_RANGE),
    )
    t = [A * R ** (n - 1) for n in range(1, LGT)]
    shuffle(t)
    TESTS.append(t)


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_small_s3t11", scope="session")
@pytest.mark.parametrize("data", TESTS)
def test_small(data):
    assert user_sol(data) == corr_sol(data)
