# Szymon Rusiecki
import pytest
from ....readstdout import checkstdout
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

BASIC_TESTS = [
    (0, 0),
    (1, 2),
    (1, 10),
    (1, 1),
    (3, 8),
    (4, 20),
    (99, 100),
    (7, 7),
    (100, 100),
    (99, 101)]

MIN_RANGE = 0
MAX_RANGE = 1000
TEST_NUM = 90
BASIC_RANDOM_TESTS = [
    (randint(MIN_RANGE, MAX_RANGE),
     randint(MIN_RANGE, MAX_RANGE))
    for _ in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="testBasic_s1z20", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", BASIC_TESTS)
    def test_basic(self, data):
        assert checkstdout(user_sol, corr_sol, data, float_type=True)

    @pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
    def test_basic_random(self, data):
        assert checkstdout(user_sol, corr_sol, data, float_type=True)
