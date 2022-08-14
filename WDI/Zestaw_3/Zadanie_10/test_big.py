# Dominik Adamczyk

import pytest
from .gen_helper import gen_test_tab
from .prog import f as user_sol
from .sol import f as corr_sol

LPIECESIZE = 1000
RPIECESIZE = 2000
NOPIECES = 20
LRANGE = -100000
RRANGE = 100000
MINDIFF = -5000
MAXDIFF = 5000
TESTNUM = 30

BIG_RANDOM_TESTS = [gen_test_tab(LPIECESIZE, RPIECESIZE, NOPIECES, LRANGE, RRANGE, MINDIFF, MAXDIFF)
                    for _ in range(TESTNUM)]


@pytest.mark.order(3)
@pytest.mark.dependency(name="test_big_s3t10", depends=["test_medium_s3t10"], scope="session")
@pytest.mark.parametrize("data", BIG_RANDOM_TESTS)
def test_big(data):
    assert user_sol(data) == corr_sol(data)
