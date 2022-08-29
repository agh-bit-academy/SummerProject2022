# Dominik Adamczyk

import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .check import check
from random import randint

EDGE_TESTS = [
    [1, 7, 3, 5, 11, 2],
    [1, 1],
    [9, 8, 7, 6, 5, 4, 3],
    [1],
    [1, 2, 3, 4, 5],
    [2, 9, 8, 1],
    [1, 1, 2, 3, 4],
    [4, 8, 1, 1, 1],
    [5, 2, 1],
    [1, 2, 3, 3]
]

MIN_SIZE = 2
MAX_SIZE = 12
LRANGE = 1
RRANGE = 15
TEST_NUM = 30

BASIC_RAND_TESTS = [RandFixArray(randint(MIN_SIZE, MAX_SIZE), LRANGE, RRANGE).get() for _ in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s6t06", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", EDGE_TESTS)
    def test_edge(self, data):
        solutions = check(data)
        if len(solutions) == 0:
            assert user_sol(data) is None
        else:
            assert user_sol(data) in solutions

    @pytest.mark.parametrize("data", BASIC_RAND_TESTS)
    def test_rand(self, data):
        solutions = check(data)
        if len(solutions) == 0:
            assert user_sol(data) is None
        else:
            assert user_sol(data) in solutions
