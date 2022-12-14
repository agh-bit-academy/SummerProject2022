# Krzysztof Mach
import pytest
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

TEST_BASIC = [0, 1, 11, 5, 17]
NO_OF_TESTS = 95
MIN_RANGE = 10 ** 2
MAX_RANGE = 10 ** 4
TEST_RANDOM = [randint(MIN_RANGE, MAX_RANGE) for _ in range(NO_OF_TESTS)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_A_s2t3", scope="session")
class TestA:
    @pytest.mark.parametrize("arg", TEST_BASIC)
    def test_basic(self, arg):
        assert user_sol(arg) == corr_sol(arg)

    @pytest.mark.parametrize("arg", TEST_RANDOM)
    def test_random(self, arg):
        assert user_sol(arg) == corr_sol(arg)
