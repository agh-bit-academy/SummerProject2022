# Karol Sewiło
import pytest
from .prog import f as user_sol
from .sol import f as corr_sol

TEST_BASIC = [i for i in range(5)]


@pytest.mark.parametrize('data', TEST_BASIC)
def test_basic(data):
    assert user_sol(data) == corr_sol(data)
