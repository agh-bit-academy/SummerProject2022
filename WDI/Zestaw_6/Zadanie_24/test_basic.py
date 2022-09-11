# Juliusz Wasieleski
import pytest
from random import randint
from .prog import f as user_sol
from .sol import f as corr_sol

BASIC_TESTS = [[(11, 2), (11, 2)],
               [(1, 0), (2, 0), (3, 0)],
               [(2, 2), (3, 3), (1, 2)]]

SIZE_MIN = 2
SIZE_MAX = 8
MIN_INT = -100
MAX_INT = 100
TEST_NUM = 37
EPS = 10 ** -6

BASIC_RANDOM_TESTS = [
    [(randint(MIN_INT, MAX_INT), randint(MIN_INT, MAX_INT)) for _ in range(randint(SIZE_MIN, SIZE_MAX))] for _ in
    range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s6t24", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", BASIC_TESTS)
    def test_basic(self, data):
        assert abs(user_sol(data) - corr_sol(data)) < EPS

    @pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
    def test_basic_random(self, data):
        assert abs(user_sol(data) - corr_sol(data)) < EPS
