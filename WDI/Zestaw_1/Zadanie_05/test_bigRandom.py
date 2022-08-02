# Krzysztof Mach
import pytest
from ....readstdout import checkstdout
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint


NO_OF_TESTS = 100

MIN_RANGE_MID = 10 ** 6
MAX_RANGE_MID = 10 ** 8
midRandomTests = [(randint(MIN_RANGE_MID, MAX_RANGE_MID),) for _ in range(NO_OF_TESTS)]

MIN_RANGE_BIG = 10 ** 8
MAX_RANGE_BIG = 10 ** 10
bigRandomTests = [(randint(MIN_RANGE_BIG, MAX_RANGE_BIG),) for _ in range(NO_OF_TESTS)]


"""
Wszystkie argumenty funkcji muszą być iterable, inaczej checkstdout się wysypuje,
więc dałem je do jednoelementowych krotek
"""


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_big_random_s1t5", depends=["test_basic_s1t5"], scope="session")
class Test:
    @pytest.mark.dependency()
    @pytest.mark.parametrize("arg", midRandomTests)
    def test_mid(self, arg):
        assert checkstdout(user_sol, corr_sol, arg, True)

    @pytest.mark.dependency(depends=["test_mid"], scope="class")
    @pytest.mark.parametrize("arg", bigRandomTests)
    def test_big(self, arg):
        assert checkstdout(user_sol, corr_sol, arg, True)
