# Karol Sewiło
import pytest
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

BASIC_TESTS = [13, 3, -1, 0, -2312312]
MIN_RANGE = 10
MAX_RANGE = 10 ** 4
TEST_NUM = 45
BASIC_RANDOM_TESTS = [randint(MIN_RANGE, MAX_RANGE) for _ in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s6t1", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", BASIC_TESTS)
    def test_basic(self, data):
        assert sorted(user_sol(data)) == sorted(corr_sol(data))

    @pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
    def test_basic_random(self, data):
        assert sorted(user_sol(data)) == sorted(corr_sol(data))
