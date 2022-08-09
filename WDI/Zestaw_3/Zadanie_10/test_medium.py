# Dominik Adamczyk

import pytest
from .gen_helper import gen_test_tab
from .prog import f as user_sol
from .sol import f as corr_sol

LPIECESIZE = 250
RPIECESIZE = 500
NOPIECES = 15
LRANGE = -1000
RRANGE = 1000
MINDIFF = -50
MAXDIFF = 50

MEDIUM_RANDOM_TESTS = [gen_test_tab(LPIECESIZE, RPIECESIZE, NOPIECES, LRANGE, RRANGE, MINDIFF, MAXDIFF)
                       for _ in range(30)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_medium_s3t10", depends=["test_basic_s3t10"], scope="session")
@pytest.mark.parametrize("data", MEDIUM_RANDOM_TESTS)
def test_medium(data):
    assert user_sol(data) == corr_sol(data)
