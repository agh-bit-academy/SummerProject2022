# Sebastian Soczawa
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from random import randint
from .sol import f as corr_sol
from .prog import f as user_sol

L_RANGE = -1000
R_RANGE = 1000
SIZE = 15
TEST_NUM = 20
COORDS_TAB = [RandFixArray(3, L_RANGE, R_RANGE) for _ in range(SIZE)]

STATIC_TABLE_TESTS = [[COORDS_TAB, randint(0, R_RANGE)]
                      for _ in range(TEST_NUM)]

R = randint(0, R_RANGE)
STATIC_R_TESTS = [[[RandFixArray(3, L_RANGE, R_RANGE)
                    for _ in range(SIZE)], R]
                  for _ in range(TEST_NUM)]

ALL_RANDOM_TESTS = [[[RandFixArray(3, L_RANGE, R_RANGE)
                      for _ in range(SIZE)], randint(0, R_RANGE)]
                    for _ in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_random_s6t29", depends=["test_basic_s6t29"], scope="session")
class TestRandom:
    @pytest.mark.parametrize("tab, r", STATIC_TABLE_TESTS)
    def test_static_table(self, tab, r):
        assert user_sol(tab, r) == corr_sol(tab, r)

    @pytest.mark.parametrize("tab, r", STATIC_R_TESTS)
    def test_static_res(self, tab, r):
        assert user_sol(tab, r) == corr_sol(tab, r)

    @pytest.mark.parametrize("tab, r", ALL_RANDOM_TESTS)
    def test_all_random(self, tab, r):
        assert user_sol(tab, r) == corr_sol(tab, r)
