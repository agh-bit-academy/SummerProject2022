# Karol Sewiło
import pytest
from ....readstdout import checkstdout
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

BASIC_TESTS = [[4], [9], [25], [1], [0], [-4], [-1], [-1234345], [3], [100]]


MIN_RANGE = 0
MAX_RANGE = 1000
TEST_NUM = 90

BASIC_RANDOM_TESTS = [[randint(MIN_RANGE, MAX_RANGE)] for _ in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s1t04", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", BASIC_TESTS)
    def test_basic(self, data):
        assert checkstdout(user_sol, corr_sol, data)

    @pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
    def test_basic_random(self, data):
        assert checkstdout(user_sol, corr_sol, data)
