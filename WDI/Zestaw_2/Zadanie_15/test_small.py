# Sebastian Soczawa
import pytest
from ....readstdout import checkstdout
from .prog import f as user_sol
from .sol import f as corr_sol

BASIC_TESTS = [[1], [2], [3]]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s2t15", scope="session")
@pytest.mark.parametrize("data", BASIC_TESTS)
def test_basic(data):
    assert checkstdout(user_sol, corr_sol, data)
