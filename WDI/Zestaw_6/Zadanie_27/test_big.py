# Juliusz Wasieleski
import pytest
from .prog import f as user_sol
from .sol import f as corr_sol
from .test_basic import get_cords

SIZE_MIN = 10
SIZE_MAX = 20
MIN_INT = -20000
MAX_INT = 20000
TEST_NUM = 20

BIG_RANDOM_TESTS = [get_cords(MIN_INT, MAX_INT, SIZE_MIN, SIZE_MAX) for _ in
                    range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_big_s6t27", depends=["test_basic_s6t27"], scope="session")
@pytest.mark.parametrize("data", BIG_RANDOM_TESTS)
def test_big_random(data):
    assert user_sol(data) == corr_sol(data)
