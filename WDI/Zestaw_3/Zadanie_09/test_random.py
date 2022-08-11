# Sebastian Soczawa
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol

SMALL_SIZE = 10**3
SMALL_LRANGE = -50
SMALL_RRANGE = 50
SMALL_TEST_NUM = 30
BIG_SIZE = 10**5
BIG_LRANGE = -10**8
BIG_RRANGE = 10**8
BIG_TEST_NUM = 30

SMALL_RANDOM_TESTS = [RandFixArray(SMALL_SIZE, SMALL_LRANGE, SMALL_RRANGE).get()
                      for _ in range(SMALL_TEST_NUM)]
BIG_RANDOM_TESTS = [RandFixArray(BIG_SIZE, BIG_LRANGE, BIG_RRANGE).get()
                    for _ in range(BIG_TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_random_s3t09", depends=["test_basic_s3t09"], scope="session")
class TestRandom:
    @pytest.mark.parametrize("data", SMALL_RANDOM_TESTS)
    def test_small_random(self, data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize("data", BIG_RANDOM_TESTS)
    def test_big_random(self, data):
        assert user_sol(data) == corr_sol(data)
