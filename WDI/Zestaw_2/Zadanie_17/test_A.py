# Jakub Bizan
from .prog import f as user_sol
from .sol import f as corr_sol


def test_basic():
    assert user_sol() == corr_sol()
