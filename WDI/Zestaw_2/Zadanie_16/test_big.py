# Dominik Adamczyk
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol

MIN_RANGE = 10**7
MAX_RANGE = 10**10
TEST_NUM = 50

BIG_RANDOM_TESTS = RandFixArray(TEST_NUM, MIN_RANGE, MAX_RANGE).get()


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_big_s2t16", depends=["test_edge_s2t16", "test_basic_s2t16"], scope="session")
@pytest.mark.parametrize("data", BIG_RANDOM_TESTS)
def test_big(data):
    assert user_sol(data) == corr_sol(data)
