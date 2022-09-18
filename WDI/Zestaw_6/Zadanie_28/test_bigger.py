# Izabella Rosikoń
# Juliusz Wasieleski
from .prog import f as user_sol
from .sol import f as corr_sol
from .test_basic import generate
from random import randint
import pytest


MIN_RANGE_M = 1
MAX_RANGE_M = 15
MIN_RANGE_B = 16
MAX_RANGE_B = 25
TEST_NUM = 15
L_RANGE_M = 8
R_RANGE_M = 10
L_RANGE_B = 11
R_RANGE_B = 13
RANDOM_SIZE_M = [randint(L_RANGE_M, R_RANGE_M) for _ in range(TEST_NUM)]
RANDOM_SIZE_B = [randint(L_RANGE_B, R_RANGE_B) for _ in range(TEST_NUM)]

TEST_RANDOM_MEDIUM = [generate(MIN_RANGE_M, MAX_RANGE_M, L_RANGE_M, R_RANGE_M) for _ in range(TEST_NUM)]

TEST_RANDOM_BIG = [generate(MIN_RANGE_B, MAX_RANGE_B, L_RANGE_B, R_RANGE_B) for _ in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name='s6t28_test_bigger', depends=['s6t28_test_basic'], scope='session')
class TestBasic:
    @pytest.mark.parametrize('data', TEST_RANDOM_MEDIUM)
    def test_basic(self, data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize('data', TEST_RANDOM_BIG)
    def test_basic_random(self, data):
        assert user_sol(data) == corr_sol(data)
