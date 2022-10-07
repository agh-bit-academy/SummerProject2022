# Sebastian Soczawa
import pytest
from random import randint
from .prog import f as user_sol
from .sol import f as corr_sol


L_RANGE = 5
R_RANGE = 10
TEST_NUM = 51

BIG_RANDOM_TESTS = [(randint(L_RANGE, R_RANGE), randint(L_RANGE, R_RANGE))
                    for _ in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_big_s6t26", depends=['test_small_s6t26'], scope="session")
@pytest.mark.parametrize("data", BIG_RANDOM_TESTS)
def test_basic_random(data):
    assert user_sol(data[0], data[1]) == corr_sol(data[0], data[1])
