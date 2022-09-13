# Izabella Rosikoń
from ....Rand_Templates.RandFixMatrix import RandFixMatrix
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint
import pytest


MIN_R_M = 20
MAX_R_M = 40
MAX_R = 15
MIN_R = 10
MIN_R_B = 100
MAX_R_B = 150
TEST_NUM = 15
R_SIZE = [randint(MIN_R, MAX_R) for _ in range(TEST_NUM)]

TEST_RANDOM_MEDIUM = [RandFixMatrix(R_SIZE[i], R_SIZE[i], MIN_R_M, MAX_R_M).get() for i in range(TEST_NUM)]
TEST_RANDOM_BIG = [RandFixMatrix(R_SIZE[i], R_SIZE[i], MIN_R_B, MAX_R_B).get() for i in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name='s6t10_test_bigger', depends=['s6t10_test_basic'], scope='session')
class TestBasic:
    @pytest.mark.parametrize('data', TEST_RANDOM_MEDIUM)
    def test_basic(self, data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize('data', TEST_RANDOM_BIG)
    def test_basic_random(self, data):
        assert user_sol(data) == corr_sol(data)
