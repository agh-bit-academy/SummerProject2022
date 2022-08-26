# Bartłomiej Kozera
import pytest
from copy import deepcopy
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

TEST_NUM = 30
LRANGE = -10**5
RRANGE = 10**5
MINSIZE = 10
MAXSIZE = 50

TAB_SIZE = [randint(MINSIZE, MAXSIZE) for _ in range(TEST_NUM)]

TEST_MED_RAND_MAT = [[sorted(RandFixArray(TAB_SIZE[i], LRANGE, RRANGE).get())
                     for _ in range(TAB_SIZE[i])] for i in range(TEST_NUM)]

ANS_TABS = [[None for _ in range(TAB_SIZE[i]**2)] for i in range(TEST_NUM)]

TEST_MED_DATA = [[TEST_MED_RAND_MAT[i], ANS_TABS[i]] for i in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_med_s4t07", depends=['test_small_s4t07'], scope="session")
@pytest.mark.parametrize('data', TEST_MED_DATA)
def test_med(data):
    assert user_sol(deepcopy(data[0]), deepcopy(data[1])) == corr_sol(data[0], data[1])
