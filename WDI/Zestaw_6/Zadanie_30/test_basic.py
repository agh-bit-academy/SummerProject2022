# Juliusz Wasieleski
import pytest
from random import randint
from .prog import f as user_sol
from .sol import f as corr_sol

BASIC_TESTS = [[[(11, 2), (11, 2)], 11, 4],
               [[(1, 0), (2, 0), (3, 0)], 5, 5],
               [[(2, 2), (3, 3), (1, 2)], 4, 5]]

INT_MIN = -100
INT_MAX = 100
SIZE_MIN = 1
SIZE_MAX = 20
R_MIN = 0
R_MAX = 100
K_MIN = 1
K_MAX = 10
TEST_NUM = 37

BASIC_RANDOM_TESTS = [
    [[(randint(INT_MIN, INT_MAX), randint(INT_MIN, INT_MAX)) for _ in range(randint(SIZE_MIN, SIZE_MAX))],
     randint(R_MIN, R_MAX), randint(K_MIN, K_MAX)] for _ in range(TEST_NUM)]
print(BASIC_RANDOM_TESTS)


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s6t30", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", BASIC_TESTS)
    def test_basic(self, data):
        assert user_sol(data[0], data[1], data[2]) == corr_sol(data[0], data[1], data[2])

    @pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
    def test_basic_random(self, data):
        assert user_sol(data[0], data[1], data[2]) == corr_sol(data[0], data[1], data[2])
