# Sebastian Soczawa
import pytest
from copy import deepcopy
from random import randint
from ....Rand_Templates.RandFixMatrix import RandFixMatrix
from .prog import f as user_sol
from .sol import f as corr_sol


VAL = 0

TEST_NUM = 20
LRANGE_BIG = 100
RRANGE_BIG = 500
RANDOM_BIG = [RandFixMatrix(randint(LRANGE_BIG, RRANGE_BIG),
                            randint(LRANGE_BIG, RRANGE_BIG), VAL, VAL).get()
              for _ in range(TEST_NUM)]


@pytest.mark.order(3)
@pytest.mark.dependency(name="test_big_random_s4t01", depends=["test_small_random_s4t01"], scope="session")
@pytest.mark.parametrize('matrix', RANDOM_BIG)
def test_odd(matrix):
    assert user_sol(deepcopy(matrix)) == corr_sol(matrix)
