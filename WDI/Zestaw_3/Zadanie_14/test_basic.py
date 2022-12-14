# Szymon Rusiecki
import pytest
from .prog import f as user_sol
from .sol import f as corr_sol

BASIC_TESTS = [20, 30, 40]
SET_PRECISION = 10 ** (-2)


@pytest.mark.parametrize("data", BASIC_TESTS)
def test_basic(data):
    assert abs(user_sol(data) - corr_sol(data)) < SET_PRECISION
