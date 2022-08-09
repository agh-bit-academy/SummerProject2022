# Dominik Adamczyk

import pytest
from .gen_helper import gen_test_tab, gen_arith_tab
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

EDGE_TESTS = [
    ([1], 1),
    ([1, 2], 2),
    ([0, 0, 0, 0], 4),
    ([1, -2, 3, -4, 5, -6], 2),
    ([0, -1, -2, -3, -4, -5], 6),
    ([1, 2, 3, 2, 1, 0, -1], 5)
]

LPIECESIZE = 5
RPIECESIZE = 20
NOPIECES = 4
LRANGE = -20
RRANGE = 20
MINDIFF = -5
MAXDIFF = 5

BASIC_RANDOM_TESTS = [gen_test_tab(LPIECESIZE, RPIECESIZE, NOPIECES, LRANGE, RRANGE, MINDIFF, MAXDIFF)
                      for _ in range(10)]

EDGE_RANDOM_TESTS = [gen_arith_tab(randint(LPIECESIZE, RPIECESIZE), randint(LRANGE, RRANGE),
                                   randint(MINDIFF, MAXDIFF)) for _ in range(10)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s3t10", scope="session")
class TestEdge:
    @pytest.mark.parametrize("data, ans", EDGE_TESTS)
    def test_edge(self, data, ans):
        assert user_sol(data) == ans

    @pytest.mark.parametrize("data", EDGE_RANDOM_TESTS)
    def test_edge_random(self, data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
    def test_basic_random(self, data):
        assert user_sol(data) == corr_sol(data)
