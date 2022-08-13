# Andrzej Karciński
import pytest
from .prog import f as user_sol
from .check import f as corr_sol
from random import randint

TEST_NUM = 200
MIN_RANGE = 10 ** 4
MAX_RANGE = 10 ** 5
TEST_RAND = [randint(MIN_RANGE, MAX_RANGE)
             for _ in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_bigRand_s3t06", depend=["test_smallRand_s3t06"], scope="session")
@pytest.mark.parametrize("data", TEST_RAND)
def test_smallRand(data):
    (user_array, user_state) = user_sol(data)
    corr_state = corr_sol(user_array)
    assert corr_state == user_state
