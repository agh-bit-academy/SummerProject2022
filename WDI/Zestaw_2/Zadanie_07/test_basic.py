# Maciej Sieniek
import pytest
from ....readstdout import checkstdout
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

BASIC_TESTS = [i for i in range(5)]

MIN_RANGE = 4
MAX_RANGE = 1000
TEST_NUM = 45
BASIC_RANDOM_TESTS = [
    randint(MIN_RANGE, MAX_RANGE)
    for _ in range(TEST_NUM)
]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s2ex7", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", BASIC_TESTS)
    def test_basic(self, data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
    def test_basic_random(self, data):
        assert user_sol(data) == corr_sol(data)
