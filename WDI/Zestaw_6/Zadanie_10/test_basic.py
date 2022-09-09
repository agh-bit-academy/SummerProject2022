# Izabella Rosikoń
from ....Rand_Templates.RandFixArray import RandFixArray
from ....Rand_Templates.RandFixMatrix import RandFixMatrix
from .prog import f as user_sol
from .sol import f as corr_sol
import pytest

TEST_RANDOM = []


@pytest.mark.order(1)
@pytest.mark.dependency(name="s6t10_test_basic", scope="session")
@pytest.mark.parametrize("data", TEST_RANDOM)
def test_basic(data):
    assert user_sol(data) == corr_sol(data)
