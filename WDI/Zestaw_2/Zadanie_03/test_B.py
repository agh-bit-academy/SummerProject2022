# Krzysztof Mach
import pytest
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint


NO_OF_TESTS = 100
MIN_RANGE = 10 ** 4
MID_RANGE = 10 ** 6
MAX_RANGE = 10 ** 8
TEST_SMALL = [randint(MIN_RANGE, MID_RANGE) for _ in range(NO_OF_TESTS)]
TEST_BIG = [randint(MID_RANGE, MAX_RANGE) for _ in range(NO_OF_TESTS)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_B_s2t3", depends=["test_A_s2t3"], scope="session")
class Test:
    @pytest.mark.parametrize("arg", TEST_SMALL)
    def test_small(self, arg):
        assert user_sol(arg) == corr_sol(arg)

    @pytest.mark.parametrize("arg", TEST_BIG)
    def test_big(self, arg):
        assert user_sol(arg) == corr_sol(arg)
