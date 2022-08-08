# Dominik Adamczyk

import pytest
from ....readstdout import checkstdout
from .prog import f as user_sol
from .sol import f as corr_sol
from .test_basic import fill_tabs

BIG_RANDOM_TESTS = []

MAX_RANGE = 35000
RANDOM_TESTS_NUMBER = 40
FIBONACCI_TAB = []


fill_tabs(MAX_RANGE, RANDOM_TESTS_NUMBER, FIBONACCI_TAB, BIG_RANDOM_TESTS)


@pytest.mark.order(3)
@pytest.mark.dependency(name="test_medium_s1t03", depends=["test_basic_s1t03", "test_medium_s1t03"], scope="session")
class TestBig:
    @pytest.mark.parametrize("data", BIG_RANDOM_TESTS)
    def test_medium(self, data):
        assert checkstdout(user_sol, corr_sol, data)
