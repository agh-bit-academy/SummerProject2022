# Juliusz Wasieleski
import pytest
from random import randint
from .prog import f as user_sol
from .sol import f as corr_sol

INT_MIN = -10000
INT_MAX = 10000
SIZE_MIN = 1
SIZE_MAX = 25
R_MIN = 0
R_MAX = 100
K_MIN = 1
K_MAX = 10
TEST_NUM = 20

BIG_RANDOM_TESTS = [
    [[(randint(INT_MIN, INT_MAX), randint(INT_MIN, INT_MAX)) for _ in range(randint(SIZE_MIN, SIZE_MAX))],
     randint(R_MIN, R_MAX), randint(K_MIN, K_MAX)] for _ in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_big_s6t30", depends=["test_basic_s6t30"], scope="session")
@pytest.mark.parametrize("data", BIG_RANDOM_TESTS)
def test_big_random(data):
    assert user_sol(data[0], data[1], data[2]) == corr_sol(data[0], data[1], data[2])
