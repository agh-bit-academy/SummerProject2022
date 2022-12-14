# Dominik Adamczyk

import pytest
from .prog import f as user_sol
from .sol import f as corr_sol
from .test_basic import create_test


A_LEN_MIN = 7
A_LEN_MAX = 25
RANGE_MIN = 1
RANGE_MAX = 500
B_LEN_MIN = 25
B_LEN_MAX = 50
TEST_NUM = 20

MID_RAND_TESTS = create_test(A_LEN_MIN, A_LEN_MAX, B_LEN_MIN, B_LEN_MAX, TEST_NUM, RANGE_MIN, RANGE_MAX)


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_mid_s4t14", depends=["test_basic_s4t14", "test_edge_s4t14"], scope="session")
@pytest.mark.parametrize("data", MID_RAND_TESTS)
def test_mid(data):
    assert user_sol(data[0], data[1]) == corr_sol(data[0], data[1])
