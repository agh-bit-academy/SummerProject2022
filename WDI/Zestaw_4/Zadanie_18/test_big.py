# Szymon Ożóg
import pytest
from .prog import f as user_sol
from .sol import f as correct_sol
from random import randint
from ....Rand_Templates.RandFixMatrix import RandFixMatrix


TEST_CASE_AMOUNT = 25
LOWER_BOUND = 1
UPPER_BOUND = 100000
TABLE_SIZE_MIN = 100
TABLE_SIZE_MAX = 200

BIG_TESTS = [(RandFixMatrix(randint(TABLE_SIZE_MIN, TABLE_SIZE_MAX), randint(TABLE_SIZE_MIN, TABLE_SIZE_MAX),
              LOWER_BOUND, UPPER_BOUND)).get() for i in range(TEST_CASE_AMOUNT)]


@pytest.mark.order(3)
@pytest.mark.dependency(name="test_big_s4t18", depends=["test_small_s4t18"], scope="session")
@pytest.mark.parametrize("tab", BIG_TESTS)
def test_small(tab):
    assert correct_sol(tab) == user_sol(tab)
