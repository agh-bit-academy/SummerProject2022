# Andrzej Karciński
import pytest
from .prog import f as user_sol
from .check import f as corr_sol
from random import randint

TEST_NUM = 100
MIN_RANGE = 10
MAX_RANGE = 1000
TEST_RAND = [randint(MIN_RANGE, MAX_RANGE)
             for _ in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_smallRand_s3t06", scope="session")
@pytest.mark.parametrize("data", TEST_RAND)
def test_smallRand(data):
    user_array, user_state = user_sol(data)
    corr_state = corr_sol(user_array)
    assert corr_state == user_state
