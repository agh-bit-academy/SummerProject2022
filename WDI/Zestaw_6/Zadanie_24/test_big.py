# Juliusz Wasieleski
import pytest
from random import randint
from .prog import f as user_sol
from .sol import f as corr_sol

SIZE_MIN = 2
SIZE_MAX = 11
MIN_INT = -10 ** 5
MAX_INT = 10 ** 5
TEST_NUM = 20
EPS = 10 ** -6

BIG_RANDOM_TESTS = [
    [(randint(MIN_INT, MAX_INT), randint(MIN_INT, MAX_INT)) for _ in range(randint(SIZE_MIN, SIZE_MAX))] for _ in
    range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_big_s6t24", depends=["test_basic_s6t24"], scope="session")
@pytest.mark.parametrize("data", BIG_RANDOM_TESTS)
def test_big_random(data):
    assert abs(user_sol(data) - corr_sol(data)) < EPS
