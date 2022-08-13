# Karolina Kucia
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol


SIZE = 10**5
TEST_NUM = 25
LRANGE = 0
RRANGE_1 = 100
RRANGE_2 = 10**6

BIG_RANDOM_TESTS_1 = [RandFixArray(SIZE, LRANGE, RRANGE_1).get() for _ in range(TEST_NUM)]
BIG_RANDOM_TESTS_2 = [RandFixArray(SIZE, LRANGE, RRANGE_2).get() for _ in range(TEST_NUM)]


@pytest.mark.order(3)
@pytest.mark.dependency(name="test_big_s3t16", depends=["test_small_s3t16"], scope="session")
class TestBigRandom:
    @pytest.mark.parametrize("data", BIG_RANDOM_TESTS_1)
    def test_big_random_1(data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize("data", BIG_RANDOM_TESTS_2)
    def test_big_random_2(data):
        assert user_sol(data) == corr_sol(data)
