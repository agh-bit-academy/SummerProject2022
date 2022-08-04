# Izabella Rosikoń
from .prog import e_number as user_sol
from .sol import e_number as corr_sol
from random import randint

SET_PRECISION = 0.1 ** 6

def test_e():
    assert abs(user_sol() - corr_sol()) < SET_PRECISION
