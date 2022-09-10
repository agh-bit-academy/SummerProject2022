# Izabella Rosikoń
from ....Rand_Templates.RandFixArray import RandFixArray
from ....Rand_Templates.RandFixMatrix import RandFixMatrix
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint
import pytest


MIN_RANGE_M = 100
MAX_RANGE_M = 10 ** 4
MAX_R = 15
MAX_C = 71
MIN_R = 10
MIN_C = 10
MIN_RANGE_B = 10 ** 4
MAX_RANGE_B = 10 ** 6
TEST_NUM = 15
RANDOM_SIZE_ROWS = [randint(MIN_R, MAX_R) for _ in range(TEST_NUM)]
RANDOM_SIZE_COLS = [randint(MIN_C, MAX_C) for _ in range(TEST_NUM)]

TEST_RANDOM_MEDIUM = [RandFixMatrix(RANDOM_SIZE_COLS[i], RANDOM_SIZE_ROWS[i], MIN_RANGE_M, MAX_RANGE_M).get()
                      for i in range(TEST_NUM)]
TEST_RANDOM_BIG = [RandFixMatrix(RANDOM_SIZE_COLS[i], RANDOM_SIZE_ROWS[i], MIN_RANGE_B, MAX_RANGE_B).get()
                      for i in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="s6t10_test_bigger", depends=['s6t10_test_basic'], scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", TEST_RANDOM_MEDIUM)
    def test_basic(data):
        assert user_sol(data) == corr_sol(data)
    @pytest.mark.parametrize("data", TEST_RANDOM_BIG)
    def test_basic_random(data):
        assert user_sol(data) == corr_sol(data)
