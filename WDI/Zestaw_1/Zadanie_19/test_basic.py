# Izabella Rosikoń
from ....readstdout import checkstdout
from .prog import e_number as user_sol
from .sol import e_number as corr_sol


def test_basic():
    assert checkstdout(user_sol, corr_sol, ())
