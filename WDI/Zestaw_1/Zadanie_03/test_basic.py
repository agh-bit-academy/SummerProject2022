# Dominik Adamczyk
import pytest
from ....readstdout import checkstdout
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

BASIC_TESTS = [
    [1],
    [3],
    [7],
    [22],
    [20],
    [110],
    [11],
    [512],
    [21],
    [1779979415736799893]
]

BASIC_RANDOM_TESTS = []

MAX_RANGE = 100
RANDOM_TESTS_NUMBER = 10
FIBONACCI_TAB = []


def fill_tabs(fibNo, length, fibTab, testTab):
    a, b = 1, 1
    for _ in range(fibNo):
        fibTab.append(a)
        a, b = b, a + b

    for _ in range(length):
        midPoint = randint(1, fibNo - 2)
        toInsert = sum(fibTab[randint(0, midPoint):randint(midPoint, fibNo)])
        toInsert += randint(0, 1) * fibTab[randint(0, fibNo-1)]
        testTab.append([toInsert])


fill_tabs(MAX_RANGE, RANDOM_TESTS_NUMBER, FIBONACCI_TAB, BASIC_RANDOM_TESTS)


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s1t03", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", BASIC_TESTS)
    def test_basic(self, data):
        assert checkstdout(user_sol, corr_sol, data)

    @pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
    def test_basic_random(self, data):
        assert checkstdout(user_sol, corr_sol, data)
