# Dominik Adamczyk

import pytest
from .prog import f as user_sol
from .sol import f as corr_sol
from .test_basic import create_test


A_LEN_MIN = 15
A_LEN_MAX = 30
RANGE_MIN = 1000
RANGE_MAX = 2000
B_LEN_MIN = 40
B_LEN_MAX = 60
TEST_NUM = 20

MID_RAND_TESTS = create_test(A_LEN_MIN, A_LEN_MAX, B_LEN_MIN, B_LEN_MAX, TEST_NUM, RANGE_MIN, RANGE_MAX)


@pytest.mark.order(3)
@pytest.mark.dependency(name="test_mid_s4t14", depends=["test_mid_s4t14"], scope="session")
@pytest.mark.parametrize("data", MID_RAND_TESTS)
def test_big(data):
    assert user_sol(data[0], data[1]) == corr_sol(data[0], data[1])
