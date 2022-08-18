# Szymon Ożóg
import pytest
from prog import f as user_sol
from sol import f as correct_sol

BASIC_TESTS = [([[]]), ([[0]]), ([[2, 2]]), ([[1, 1], [2, 3], [9, 3]]), ([[-2, 5], [-7, 1]])]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s4t03", scope="session")
@pytest.mark.parametrize("tab", BASIC_TESTS)
def test_basic(tab):
    assert correct_sol(tab) == user_sol(tab)
