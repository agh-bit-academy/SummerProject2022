# Dominik Adamczyk

import pytest
from .gen_helper import gen_test_table
from .prog import f as user_sol
from .sol import f as corr_sol

LPIECESIZE = 75
RPIECESIZE = 100
NOPIECES = 5
LRANGE = -200
RRANGE = 200
TESTNUM = 30

MID_TEST = [gen_test_table(LPIECESIZE, RPIECESIZE, NOPIECES, LRANGE, RRANGE) for _ in range(TESTNUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_mid_s3t13", depends=["test_basic_s3t13"], scope="session")
@pytest.mark.parametrize("data", MID_TEST)
def test_mid(data):
    assert user_sol(data) == corr_sol(data)
