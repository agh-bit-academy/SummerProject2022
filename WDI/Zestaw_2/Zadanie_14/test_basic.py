# Sebastian Soczawa
import pytest
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

EDGE_TESTS = [
    (1, 1, 1),
    (1, 3, 2),
    (31, 3, 2),
    (3, 13, 1),
    (3, 31, 2),
    (17, 17, 0),
    (11, 17, 2),
]

MIN_VAL = 1
MAX_VAL = 100
TEST_NUM = 43
BASIC_TESTS = [
    (randint(MIN_VAL, MAX_VAL), randint(MIN_VAL, MAX_VAL))
    for _ in range(TEST_NUM)
]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s2t14", scope="session")
class TestInitial:
    @pytest.mark.parametrize("data", BASIC_TESTS)
    def test_basic(self, data):
        assert user_sol(data[0], data[1]) == corr_sol(data[0], data[1])

    @pytest.mark.parametrize("data", EDGE_TESTS)
    def test_edge(self, data):
        assert data[2] == corr_sol(data[0], data[1])
