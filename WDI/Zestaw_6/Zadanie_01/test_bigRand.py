# Karol Sewiło
import pytest
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

MIN_RANGE = 10 ** 7
MAX_RANGE = 10 ** 9
TEST_NUM = 50
BIG_RANDOM_TESTS = [randint(MIN_RANGE, MAX_RANGE) for _ in range(TEST_NUM)]


@pytest.mark.order(3)
@pytest.mark.dependency(name="test_big_rand_s6t1", depends=["test_small_rand_s6t1"], scope="session")
@pytest.mark.parametrize("data", BIG_RANDOM_TESTS)
def test_big_random(data):
    assert sorted(user_sol(data)) == sorted(corr_sol(data))
