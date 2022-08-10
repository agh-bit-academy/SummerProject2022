# Dominik Adamczyk

import pytest
from .gen_helper import gen_test_table, gen_palindromic_table
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

LPIECESIZE = 90
RPIECESIZE = 110
NOPIECES = 8
LRANGE = -1000
RRANGE = 1000
TESTNUM = 15
FACTOR = 3

BIG_TEST = [gen_test_table(LPIECESIZE, RPIECESIZE, NOPIECES, LRANGE, RRANGE) for _ in range(TESTNUM)]
BIGPAL_TEST = [gen_palindromic_table(randint(LPIECESIZE * NOPIECES * FACTOR, RPIECESIZE * NOPIECES * FACTOR),
                                     LRANGE, RRANGE) for _ in range(TESTNUM)]


@pytest.mark.order(3)
@pytest.mark.dependency(name="test_big_s3t13", depends=["test_mid_s3t13"], scope="session")
class TestBig:
    @pytest.mark.parametrize("data", BIG_TEST)
    def test_big_rand(self, data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize("data", BIGPAL_TEST)
    def test_big_pal(self, data):
        assert user_sol(data) == corr_sol(data)
