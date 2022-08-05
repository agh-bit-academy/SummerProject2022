# Izabella Rosikoń
import pytest
from .prog import unique_digit as user_sol
from .sol import unique_digit as corr_sol

BASIC_TESTS = [i for i in range(5, 16)] + [j * 110 for j in range(1, 10)]

@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s2t13", scope="session")
@pytest.mark.parametrize("data", BASIC_TESTS)
def test_basic(data):
    assert user_sol(data) == corr_sol(data)