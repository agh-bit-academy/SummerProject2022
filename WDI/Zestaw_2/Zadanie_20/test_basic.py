#Andrzej Karciński
import pytest
from ....readstdout import checkstdout
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

BASIC_TESTS = [
    (1, 1),
    (2, 2),
    (2, 1),
    (5, 6),
    (10, 25)
    ]

MIN_RANGE = 1
MAX_RANGE = 20
TEST_NUM = 5
BASIC_RANDOM_TESTS = [
    (randint(MIN_RANGE, MAX_RANGE),
     randint(MIN_RANGE, MAX_RANGE))
    for _ in range(TEST_NUM)]

@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s2t20", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", BASIC_TESTS)
    def test_basic_(self, data):
        assert checkstdout(user_sol, corr_sol, data, float_type=False)

    @pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
    def test_basic_random(self, data):
        assert checkstdout(user_sol, corr_sol, data, float_type=False)

