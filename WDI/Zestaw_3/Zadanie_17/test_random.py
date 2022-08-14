# Izabella Rosikoń
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol

SIZE_A = 5
SIZE_B = 7
A_RANGE_L = 65
A_RANGE_R = 10 ** 3
B_RANGE_L = 156
B_RANGE_R = 10 ** 3


RANDOM_TESTS = [(RandFixArray(SIZE_A, A_RANGE_L, A_RANGE_R).get(),
                RandFixArray(SIZE_B, B_RANGE_L, B_RANGE_R).get())
                for _ in range(15)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_random_s3t17", depends=["test_basic_s3t17"], scope="session")
@pytest.mark.parametrize("tab1, tab2", RANDOM_TESTS)
def test_random(tab1, tab2):
    assert user_sol(tab1, tab2) == corr_sol(tab1, tab2)
