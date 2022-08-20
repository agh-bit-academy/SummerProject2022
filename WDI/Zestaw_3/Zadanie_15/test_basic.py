



# Mikołaj Maślak
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol


BASIC_TESTS = [
    [2, 2],
    [4, 4],
    [7, 8, 9, 13, 17],
    [1, 2, 4, 8, 16],
    [2, 3, 5, 7, 9, 11, 13, 17, 19, 23, 29],
    [2, 1, 3, 7],
    [435, 300, 1432, 71, 13]
]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s3t15", scope="session")
@pytest.mark.parametrize("data", BASIC_TESTS)
def test_big(data):
    assert user_sol(data) == corr_sol(data)
