# Kacper Słoniec
import pytest
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

BASIC_TESTS = [
    1,
    2,
    3,
    4,
    6,
    9,
    17,
    34,
    99,
    100]

MIN_RANGE = 1
MAX_RANGE = 100
TEST_NUM = 90
BASIC_RANDOM_TESTS = [
    randint(MIN_RANGE, MAX_RANGE)
    for _ in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s2t1", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", BASIC_TESTS)
    def test_basic(self, data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
    def test_basic_random(self, data):
        assert user_sol(data) == corr_sol(data)
