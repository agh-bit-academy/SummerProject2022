# Izabella Rosikoń
import pytest
from .prog import f as user_sol
from .sol import f as corr_sol

BASIC_TESTS = [
    ([1, 2, 3], [2, 6, 1, 9]),
    ([0], [0]),
    ([17, 10, 24, 82], [24, 24, 12, 12]),
    ([14, 17, 10, 1000, 1666], [0]),
    ([192873645, 1928436483, 1928394], [199191, 384, 1919373, 183743, 191, 1])
]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s3t17", scope="session")
@pytest.mark.parametrize("tab1, tab2", BASIC_TESTS)
def test_basic(tab1, tab2):
    assert corr_sol(tab1, tab2) == user_sol(tab1, tab2)
