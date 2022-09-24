# Szczepan Rzeszutek
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

START = 10 * 10
END = 10 ** 30
TEST_NUM = 80
WEIGHT = randint(10 * 10, 10 ** 30)
TEST_BIG = [(RandFixArray(1, START, END).get(), WEIGHT) for _ in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_big_s6t7", depends=["test_basic_s6t7"], scope="session")
@pytest.mark.parametrize("data", TEST_BIG)
def test_big(data):
    assert user_sol(data[0], data[1]) == corr_sol(data[0], data[1])
