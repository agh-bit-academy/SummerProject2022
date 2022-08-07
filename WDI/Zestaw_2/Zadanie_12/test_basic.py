# Juliusz Wasieleski
import pytest
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

BASIC_TESTS = [
    1,
    4,
    5,
    10,
    12,
    20,
    21,
    32,
    40]

MIN_RANGE = 0
MAX_RANGE = 400
TEST_NUM = 90
BASIC_RANDOM_TESTS = [
    randint(MIN_RANGE, MAX_RANGE)
    for _ in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s1t09", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", BASIC_TESTS)
    def test_basic(self, data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
    def test_basic_random(self, data):
        assert user_sol(data) == corr_sol(data)
