# Izabella Rosikoń
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol

SIZE_A = 65
SIZE_B = 55
A_RANGE_L = 65
A_RANGE_R = 10 ** 4
B_RANGE_L = 156
B_RANGE_R = 10 ** 4
SIZE_A_BIG = 65 * (10 ** 4)
SIZE_B_BIG = 55 * (10 ** 4)
A_RANGE_L_BIG = 650
A_RANGE_R_BIG = 10 ** 8
B_RANGE_L_BIG = 1560
B_RANGE_R_BIG = 10 ** 8

RANDOM_TESTS = [(RandFixArray(SIZE_A, A_RANGE_L, A_RANGE_R).get(),
                RandFixArray(SIZE_B, B_RANGE_L, B_RANGE_R).get())
                for _ in range(15)]
BIG_RANDOM_TESTS = [(RandFixArray(SIZE_A_BIG, A_RANGE_L_BIG, A_RANGE_R_BIG).get(),
                    RandFixArray(SIZE_B_BIG, B_RANGE_L_BIG, B_RANGE_R_BIG).get())
                    for _ in range(15)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_random_s3t17", depends=["test_basic_s3t17"], scope="session")
class TestRandom:
    @pytest.mark.parametrize("data", RANDOM_TESTS)
    def test_random(self, data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize("data", BIG_RANDOM_TESTS)
    def test_big_random(self, data):
        assert user_sol(data) == corr_sol(data)
