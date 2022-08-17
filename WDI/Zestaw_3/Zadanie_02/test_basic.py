# Maciej Bartczak
import pytest
from .prog import f as user_sol
from .sol import f as correct_sol

BASIC_TESTS = [
    (123, 123),
    (10, 100),
    (123456, 645213),
    (1234567890, 1234098765),
    (111112, 1121111),
    (55566677788890, 90567856785678)
]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s3t02", scope="session")
@pytest.mark.parametrize("num1, num2", BASIC_TESTS)
def test_basic(num1, num2):
    assert correct_sol(num1, num2) == user_sol(num1, num2)
