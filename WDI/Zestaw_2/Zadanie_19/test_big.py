# Paweł Konopka
import pytest
from .check import my_checkstdout
from .gener_test import decode, gener_test, get_periodic_form
from .prog import f as user_sol
from random import randint

# Test A
INTEGER_MIN_LEN, INTEGER_MAX_LEN = 2, 5
INDENT_MIN_LEN, INDENT_MAX_LEN = 2, 5
PERIOD_MIN_LEN, PERIOD_MAX_LEN = 100, 200
TEST_NUM = 20

BIG_TESTS_A = []
for _ in range(TEST_NUM):
    integ, indent, period = gener_test(
        randint(INTEGER_MIN_LEN, INTEGER_MAX_LEN),
        randint(INDENT_MIN_LEN, INDENT_MAX_LEN),
        randint(PERIOD_MIN_LEN, PERIOD_MAX_LEN))
    a, b = decode(integ, indent, period)

    BIG_TESTS_A.append(
        (a, b, get_periodic_form(integ, indent, period)))

# Test B
INTEGER_MIN_LEN, INTEGER_MAX_LEN = 100, 200
INDENT_MIN_LEN, INDENT_MAX_LEN = 100, 200
PERIOD_MIN_LEN, PERIOD_MAX_LEN = 50, 100
TEST_NUM = 20

BIG_TESTS_B = []
for _ in range(TEST_NUM):
    integ, indent, period = gener_test(
        randint(INTEGER_MIN_LEN, INTEGER_MAX_LEN),
        randint(INDENT_MIN_LEN, INDENT_MAX_LEN),
        randint(PERIOD_MIN_LEN, PERIOD_MAX_LEN))
    a, b = decode(integ, indent, period)

    BIG_TESTS_B.append(
        (a, b, get_periodic_form(integ, indent, period)))


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_big_s2t19", depends=["test_mid_s2t19"], scope="session")
class TestBig:
    @pytest.mark.parametrize("data", BIG_TESTS_A)
    def test_big(self, data):
        assert my_checkstdout(user_sol, data[:2], data[2])

    @pytest.mark.parametrize("data", BIG_TESTS_B)
    def test_mid_b(self, data):
        assert my_checkstdout(user_sol, data[:2], data[2])
