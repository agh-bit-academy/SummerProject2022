# Paweł Konopka
import pytest
from .check import my_checkstdout
from .gener_test import decode, gener_test, get_periodic_form
from .prog import f as user_sol
from random import randint

# Test A
INTEGER_MIN_LEN, INTEGER_MAX_LEN = 2, 5
INDENT_MIN_LEN, INDENT_MAX_LEN = 2, 5
PERIOD_MIN_LEN, PERIOD_MAX_LEN = 3, 5
TEST_NUM = 50

MID_TESTS_A = []
for _ in range(TEST_NUM):
    integ, indent, period = gener_test(
        randint(INTEGER_MIN_LEN, INTEGER_MAX_LEN),
        randint(INDENT_MIN_LEN, INDENT_MAX_LEN),
        randint(PERIOD_MIN_LEN, PERIOD_MAX_LEN))
    a, b = decode(integ, indent, period)

    MID_TESTS_A.append(
        (a, b, get_periodic_form(integ, indent, period)))

# Test B
INTEGER_MIN_LEN, INTEGER_MAX_LEN = 1, 2
INDENT_MIN_LEN, INDENT_MAX_LEN = 1, 2
PERIOD_MIN_LEN, PERIOD_MAX_LEN = 5, 8
TEST_NUM = 50

MID_TESTS_B = []
for _ in range(TEST_NUM):
    integ, indent, period = gener_test(
        randint(INTEGER_MIN_LEN, INTEGER_MAX_LEN),
        randint(INDENT_MIN_LEN, INDENT_MAX_LEN),
        randint(PERIOD_MIN_LEN, PERIOD_MAX_LEN))
    a, b = decode(integ, indent, period)

    MID_TESTS_B.append(
        (a, b, get_periodic_form(integ, indent, period)))

# Test C
INTEGER_MIN_LEN, INTEGER_MAX_LEN = 0, 0
INDENT_MIN_LEN, INDENT_MAX_LEN = 0, 0
PERIOD_MIN_LEN, PERIOD_MAX_LEN = 8, 10
TEST_NUM = 20

MID_TESTS_C = []
for _ in range(TEST_NUM):
    integ, indent, period = gener_test(
        randint(INTEGER_MIN_LEN, INTEGER_MAX_LEN),
        randint(INDENT_MIN_LEN, INDENT_MAX_LEN),
        randint(PERIOD_MIN_LEN, PERIOD_MAX_LEN))
    a, b = decode(integ, indent, period)

    MID_TESTS_C.append(
        (a, b, get_periodic_form(integ, indent, period)))


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_mid_s2t19", depends=["test_basic_s2t19"], scope="session")
class TestMid:
    @pytest.mark.parametrize("data", MID_TESTS_A)
    def test_mid_a(self, data):
        assert my_checkstdout(user_sol, data[:2], data[2])

    @pytest.mark.parametrize("data", MID_TESTS_B)
    def test_mid_b(self, data):
        assert my_checkstdout(user_sol, data[:2], data[2])

    @pytest.mark.parametrize("data", MID_TESTS_C)
    def test_mid_c(self, data):
        assert my_checkstdout(user_sol, data[:2], data[2])
