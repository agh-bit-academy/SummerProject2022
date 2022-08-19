# Szymon Ożóg
import pytest
from .prog import f as user_sol
from .sol import f as correct_sol
from random import randint
from ....Rand_Templates.RandFixMatrix import RandFixMatrix

TEST_CASE_AMOUNT = 100
LOWER_BOUND = -1000
UPPER_BOUND = 1000
TABLE_SIZE_MIN = 3
TABLE_SIZE_MAX = 10
RANDOM_TESTS = [(RandFixMatrix(randint(TABLE_SIZE_MIN, TABLE_SIZE_MAX), randint(TABLE_SIZE_MIN, TABLE_SIZE_MAX),
                 LOWER_BOUND, UPPER_BOUND).get()) for i in range(TEST_CASE_AMOUNT)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_random_s4t03", depends=["test_basic_s4t03"], scope="session")
@pytest.mark.parametrize("tab", RANDOM_TESTS)
def test_random(tab):
    assert correct_sol(tab) == user_sol(tab)
