# Sebastian Soczawa
import pytest
from ....Rand_Templates.RandFixMatrix import RandFixMatrix
from .prog import f as user_sol
from .sol import f as corr_sol
from copy import deepcopy


VAL = 0


INIT_NUM = 10
INIT_TESTS = [RandFixMatrix(i, i, VAL, VAL).get() for i in range(2, INIT_NUM)]

ODD_START = 11
ODD_END = 100
ODD_TESTS = [RandFixMatrix(i, i, VAL, VAL).get() for i in range(ODD_START, ODD_END, 6)]

EVEN_START = 12
EVEN_END = 99
EVEN_TESTS = [RandFixMatrix(i, i, VAL, VAL).get() for i in range(EVEN_START, EVEN_END, 6)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_square_s4t01", scope="session")
class TestSquare:
    @pytest.mark.parametrize('matrix', INIT_TESTS)
    def test_init(self, matrix):
        assert corr_sol(deepcopy(matrix)) == user_sol(matrix)

    @pytest.mark.parametrize('matrix', EVEN_TESTS)
    def test_even(self, matrix):
        assert user_sol(deepcopy(matrix)) == corr_sol(matrix)

    @pytest.mark.parametrize('matrix', ODD_TESTS)
    def test_odd(self, matrix):
        assert user_sol(deepcopy(matrix)) == corr_sol(matrix)
