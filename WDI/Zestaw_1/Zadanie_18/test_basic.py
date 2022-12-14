# Juliusz Wasieleski
import pytest
from ....readstdout import checkstdout
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

BASIC_TESTS = [[0],
               [1],
               [0.5],
               [2],
               [4],
               [9],
               [1.25],
               [10],
               [8],
               [0.25]]

MIN_RANGE = 10
MAX_RANGE = 1000
NO_OF_TESTS = 90

RANDOM_TESTS = [[randint(MIN_RANGE, MAX_RANGE)] for _ in range(NO_OF_TESTS)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s1t18", scope="session")
class TestBasic:
    @pytest.mark.parametrize("arg", BASIC_TESTS)
    def test_basic(self, arg):
        assert checkstdout(user_sol, corr_sol, arg, True)

    @pytest.mark.parametrize("arg", RANDOM_TESTS)
    def test_random(self, arg):
        assert checkstdout(user_sol, corr_sol, arg, True)
