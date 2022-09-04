# Juliusz Wasieleski
import pytest
from .prog import f as user_sol
from .sol import is_it_possible


def check(tab):
    n = len(tab)
    if n != 8:
        return False
    for i in range(n):
        if (tab[i] < 0 or tab[i] >= n) and not is_it_possible(tab, i, tab[i]):
            return False
    return True


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s6t15", scope="session")
def test_small():
    assert check(user_sol())
