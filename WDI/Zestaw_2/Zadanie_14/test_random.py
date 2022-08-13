# Sebastian Soczawa
import pytest
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

MIN_VAL = 100
MAX_VAL = 100000
TEST_NUM = 50
RANDOM_TESTS = [
    (randint(MIN_VAL, MAX_VAL), randint(MIN_VAL, MAX_VAL))
    for _ in range(TEST_NUM)
]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_random_s2t14", depends=["test_basic_s2t14"], scope="session")
@pytest.mark.parametrize("data", RANDOM_TESTS)
def test_random(data):
    assert user_sol(data[0], data[1]) == corr_sol(data[0], data[1])
