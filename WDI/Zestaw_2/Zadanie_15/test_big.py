# Sebastian Soczawa
import pytest
from ....readstdout import checkstdout
from .prog import f as user_sol
from .sol import f as corr_sol

BIG_TESTS = [[4], [5], [6]]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_big_s2t15", depends=["test_basic_s2t15"], scope="session")
@pytest.mark.parametrize("data", BIG_TESTS)
def test_basic(data):
    assert checkstdout(user_sol, corr_sol, data)
