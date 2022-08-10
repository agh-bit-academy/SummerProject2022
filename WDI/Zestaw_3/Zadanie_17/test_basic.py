# Izabella Rosikoń
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

BASIC_TESTS = [
    ([1, 2, 3], [2, 6, 1, 9])
]