# Karol Sewiło
import pytest
from ....readstdout import checkstdout
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

BASIC_TESTS = [
    (0, 7),
    (2315, 7),
    (1, 10),
    (1, 1),
    (1342, 3),
    (10000, 20),
    (4235, 5),
    (7, -7),
    (100, 100),
    (400, 10)]

MIN_RANGE_NUMBER = 0
MAX_RANGE_NUMBER = 1000
MIN_RANGE_DIVISOR = 1
MAX_RANGE_DIVISOR = 10
TEST_NUM = 90
BASIC_RANDOM_TESTS = [
    (randint(MIN_RANGE_NUMBER, MAX_RANGE_NUMBER),
     randint(MIN_RANGE_DIVISOR, MAX_RANGE_DIVISOR))
    for _ in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s2t05", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", BASIC_TESTS)
    def test_basic(self, data):
        assert checkstdout(user_sol, corr_sol, data)

    @pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
    def test_basic_random(self, data):
        assert checkstdout(user_sol, corr_sol, data)
