# Maciej Sieniek
import pytest
from ....readstdout import checkstdout
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

MIN_RANGE = 0
MAX_RANGE = 10 ** 9
TEST_NUM = 100
TEST_RANDOM = [
    randint(MIN_RANGE, MAX_RANGE)
    for _ in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_Rand_s2ex7", depends=["test_basic_s2ex7"], scope="session")
class Tests:
    @pytest.mark.parametrize("data", TEST_RANDOM)
    def test_random(self, data):
        assert checkstdout(user_sol, corr_sol, [data])
