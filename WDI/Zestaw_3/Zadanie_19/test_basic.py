# Juliusz Wasieleski
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol

EDGE_TESTS = [
    [],
    [1],
    [0, 0, 0, 0],
    [1, 2, 3, -4, 5, -6],
    [0, -1, -2, -3, -4, -5],
    [1, 2, 1, 2, 1, 2, 1],
    [0, 1, 2, 3, 4, 5, 6],
    [1, -2, -4, -5, 1, 0, 1],
    [-5, -4, -3, -2, -10, 1, 2, 3]
]
SIZE = 50
LRANGE = -50
RRANGE = 50
TEST_NUM = 91

BASIC_RANDOM_TESTS = [RandFixArray(SIZE, LRANGE, RRANGE).get()
                      for _ in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s3t19", scope="session")
class TestEdge:
    @pytest.mark.parametrize("data", EDGE_TESTS)
    def test_edge(self, data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
    def test_basic_random(self, data):
        assert user_sol(data) == corr_sol(data)
