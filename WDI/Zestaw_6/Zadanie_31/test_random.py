# Sebastian Soczawa
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol


L_RANGE = 10 ** 3
R_RANGE = 10 ** 5
TEST_NUM = 70

RANDOM_TESTS = RandFixArray(TEST_NUM, L_RANGE, R_RANGE).get()


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_random_s6t31", depends=['test_basic_s6t31'], scope="session")
@pytest.mark.parametrize("data", RANDOM_TESTS)
def test_random(data):
    assert user_sol(data) == corr_sol(data)
