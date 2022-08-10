import pytest
from .gen_helper import gen_palindromic_table, gen_test_table
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

EDGE_TESTS = [
    ([1], 1),
    ([1, 2], 1),
    ([0, 0, 0, 0], 4),
    ([1, -2, 1], 3),
    ([1, 1, 2, 1, 2, 1], 5),
    ([2, 9, 3, 1, 7, 11, 9, 6, 7, 7, 1, 3, 9, 12, 15], 4),
    ([1, 2, 3, 4, 5, 6], 1),
    ([1, 2, 3, 4, 5, 6, 4, 2, 1], 2),
    ([3, 4, 3, 4, 3, 4, 3, 4], 7),
    ([1, 2, 3, 5, 4, 1, 4, 3, 2, 1], 3)
]

LPIECESIZE = 5
RPIECESIZE = 20
NOPIECES = 4
LRANGE = -20
RRANGE = 20
TESTNUM = 10

PAL_TEST = [gen_palindromic_table(randint(LPIECESIZE, RPIECESIZE), LRANGE, RRANGE) for _ in range(TESTNUM)]
RAND_TEST = [gen_test_table(LPIECESIZE, RPIECESIZE, NOPIECES, LRANGE, RRANGE) for _ in range(TESTNUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s3t13", scope="session")
class TestEdge:
    @pytest.mark.parametrize("data, ans", EDGE_TESTS)
    def test_edge(self, data, ans):
        assert user_sol(data) == ans

    @pytest.mark.dependency(name="test_basicpal_s3t13", depends=["test_basic_s3t13"], scope="session")
    @pytest.mark.parametrize("data", PAL_TEST)
    def test_pal(self, data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.dependency(name="test_basicrand_s3t13", depends=["test_basic_s3t13"], scope="session")
    @pytest.mark.parametrize("data", RAND_TEST)
    def test_small_rand(self, data):
        assert user_sol(data) == corr_sol(data)
