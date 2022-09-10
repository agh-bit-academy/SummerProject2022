# Izabella Rosikoń
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint
import pytest


MIN_RANGE_M = 0
MAX_RANGE_M = 100
MIN_RANGE_B = 100
MAX_RANGE_B = 10 ** 2
TEST_NUM = 15
L_RANGE_M = 100
R_RANGE_M = 10 ** 2
L_RANGE_B = 10 ** 2 
R_RANGE_B = 10 ** 4
RANDOM_SIZE_M = [randint(L_RANGE_M, R_RANGE_M) for _ in range(TEST_NUM)]
RANDOM_SIZE_B = [randint(L_RANGE_B, R_RANGE_B) for _ in range(TEST_NUM)]

TEST_RANDOM_MEDIUM = [RandFixArray(RANDOM_SIZE_M[i], MIN_RANGE_M, MAX_RANGE_M).get() for i in range(TEST_NUM)]

TEST_RANDOM_BIG = [RandFixArray(RANDOM_SIZE_B[i], MIN_RANGE_B, MAX_RANGE_B).get() for i in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="s6t28_test_bigger", depends=['s6t28_test_basic'], scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", TEST_RANDOM_MEDIUM)
    def test_basic(data):
        assert user_sol(data) == corr_sol(data)
    @pytest.mark.parametrize("data", TEST_RANDOM_BIG)
    def test_basic_random(data):
        assert user_sol(data) == corr_sol(data)
