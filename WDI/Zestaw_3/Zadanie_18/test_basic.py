# Mikołaj Maślak
import pytest
from .prog import f as user_sol
from .sol import f as corr_sol

BASIC_TESTS = [
    [1, 2, 4, 8, 4, 2, 1],
    [3, 3, 3, 3, 3],
    [2, 5, 7, 3, 3, 7, 8, 3, 4, 3, 8],
    [1, 3, 6, 9, 12, 13, 15, 15, 13],
    [2, 2, 2, 2],
    [3, 5, 7, 9, 11, 13, 11, 9, 7, 5, 3],
    [9, 5, 9, 7, 5, 9, 5, 7, 5],
]

@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s3t18", scope="session")
@pytest.mark.parametrize("data", BASIC_TESTS)
def test_basic(data):
    assert user_sol(data) == corr_sol(data)
