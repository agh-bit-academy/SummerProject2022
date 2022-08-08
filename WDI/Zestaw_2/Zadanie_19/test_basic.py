# Paweł Konopka

import pytest
from .check import my_checkstdout
from .gener_test import decode, gener_test, get_periodic_form
from .prog import f as user_sol


BASIC_TESTS = [
    (1, 3, '0.(3)'),
    (1, 6, '0.1(6)'),
    (7, 9, '0.(7)'),
    (1, 7, '0.(142857)'),
    (1, 15, '0.0(6)')]

INTEGER_LEN = 0
INDENT_LEN = 0
PERIOD_LEN = 2
TEST_NUM = 20

BASIC_RANDOM_TESTS = []

for _ in range(TEST_NUM):
    integ, indent, period = gener_test(INTEGER_LEN, INDENT_LEN, PERIOD_LEN)
    BASIC_RANDOM_TESTS.append(
        (*decode(integ, indent, period), get_periodic_form(integ, indent, period)))

# for row in BASIC_RANDOM_TESTS:
#     print(row)


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s2t19", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", BASIC_TESTS)
    def test_basic(self, data):
        assert my_checkstdout(user_sol, data[:2], data[2])

    @pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
    def test_basic_random(self, data):
        assert my_checkstdout(user_sol, data[:2], data[2])
