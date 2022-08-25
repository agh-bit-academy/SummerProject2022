# Sebastian Soczawa
import pytest
from copy import deepcopy
from random import randint
from ....Rand_Templates.RandFixMatrix import RandFixMatrix
from .prog import f as user_sol
from .sol import f as corr_sol
1

VAL = 0

TEST_NUM = 42
LRANGE_SMALL = 1
RRANGE_SMALL = 50
RANDOM_SMALL = [RandFixMatrix(randint(LRANGE_SMALL, RRANGE_SMALL),
                              randint(LRANGE_SMALL, RRANGE_SMALL), VAL, VAL).get()
                for _ in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_small_random_s4t01", depends=["test_square_s4t01"], scope="session")
@pytest.mark.parametrize('matrix', RANDOM_SMALL)
def test_odd(matrix):
    assert user_sol(deepcopy(matrix)) == corr_sol(matrix)
