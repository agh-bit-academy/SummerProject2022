# Andrzej Karciński
from .prog import f as user_sol
from .sol import f as corr_sol
import pytest


KILLER_NUMBER = 1_000_003
SIZE = 100
ROW = []


def make_matrix():
    for _ in range(SIZE // 2):
        ROW.append(KILLER_NUMBER // 2)
        ROW.append(KILLER_NUMBER // 2 + 1)


make_matrix()
TEST_KILLER = [[ROW for _ in range(SIZE)]]


@pytest.mark.order(3)
@pytest.mark.dependency(name="s4t13_test_killer", depends=["s4t13_test_random"], scope="session")
@pytest.mark.parametrize("data", TEST_KILLER)
def test_killer(data):
    assert user_sol(data) == corr_sol(data)
