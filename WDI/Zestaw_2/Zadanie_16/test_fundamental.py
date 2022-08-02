# Paweł Konopka

import pytest
from ....readstdout import checkstdout
from .gener_sol import f as corr_sol
from .prog import f as user_sol


ARG = 1_000_000


@pytest.mark.order(4)
@pytest.mark.dependency(name="testFundamental_s2z16", scope="session")
class TestFundamental:
    def test_fundamental(self):
        assert checkstdout(user_sol, corr_sol, [ARG], float_type=True)
