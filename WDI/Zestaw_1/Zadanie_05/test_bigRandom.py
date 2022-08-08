# Krzysztof Mach
import pytest
from ....readstdout import checkstdout
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

NO_OF_TESTS = 100

MIN_RANGE_MID = 10 ** 5
MAX_RANGE_MID = 10 ** 7
MID_RANDOM_TESTS = [(randint(MIN_RANGE_MID, MAX_RANGE_MID),) for _ in range(NO_OF_TESTS)]

MIN_RANGE_BIG = 10 ** 8
MAX_RANGE_BIG = 10 ** 9
BIG_RANDOM_TESTS = [(randint(MIN_RANGE_BIG, MAX_RANGE_BIG),) for _ in range(NO_OF_TESTS)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_big_random_s1t5", depends=["test_basic_s1t5"], scope="session")
class Test:
    @pytest.mark.parametrize("arg", MID_RANDOM_TESTS)
    def test_mid(self, arg):
        assert checkstdout(user_sol, corr_sol, arg, True)

    @pytest.mark.parametrize("arg", BIG_RANDOM_TESTS)
    def test_big(self, arg):
        assert checkstdout(user_sol, corr_sol, arg, True)
