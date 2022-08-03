import pytest
from ....readstdout import checkstdout
from .prog import e as user_sol
from .sol import e as corr_sol
from random import randint

class TestE:
    @pytest.mark.parametrize("data")
    