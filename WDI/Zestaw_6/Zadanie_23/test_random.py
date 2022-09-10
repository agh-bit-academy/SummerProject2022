# Sebastian Soczawa
import pytest
from random import randint
from ....Rand_Templates.RandFixArray import RandFixArray
from .sol import f as corr_sol
from .prog import f as user_sol

LRANGE = 0
RRANGE = 40
SIZE = 50
TEST_NUM = 20
TEST_TAB = RandFixArray(SIZE, LRANGE, RRANGE).get()
STATIC_TABLE_TESTS = [[TEST_TAB, randint(LRANGE, RRANGE)]
                      for _ in range(TEST_NUM)]

RES = randint(LRANGE, RRANGE)
STATIC_RES_TESTS = [[RandFixArray(SIZE, LRANGE, RRANGE).get(), RES]
                    for _ in range(TEST_NUM)]

ALL_RANDOM_TESTS = [[RandFixArray(SIZE, LRANGE, RRANGE).get(), randint(LRANGE, RRANGE)]
                    for _ in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_random_s6t23", depends=["test_basic_s6t23"], scope="session")
class TestRandom:
    @pytest.mark.parametrize("tab, res", STATIC_TABLE_TESTS)
    def test_static_table(self, tab, res):
        assert user_sol(tab, res) == corr_sol(tab, res)

    @pytest.mark.parametrize("tab, res", STATIC_RES_TESTS)
    def test_static_res(self, tab, res):
        assert user_sol(tab, res) == corr_sol(tab, res)

    @pytest.mark.parametrize("tab, res", ALL_RANDOM_TESTS)
    def test_all_random(self, tab, res):
        assert user_sol(tab, res) == corr_sol(tab, res)
