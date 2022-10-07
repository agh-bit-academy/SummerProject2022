# Sebastian Soczawa
import pytest
from .prog import f as user_sol
from .sol import f as corr_sol


A_B_RANGE = 7

SMALL_RANDOM_TESTS = [[A, B] for A in range(A_B_RANGE)
                      for B in range(A_B_RANGE)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_small_s6t26", scope="session")
@pytest.mark.parametrize("data", SMALL_RANDOM_TESTS)
def test_basic_random(data):
    assert user_sol(data[0], data[1]) == corr_sol(data[0], data[1])
