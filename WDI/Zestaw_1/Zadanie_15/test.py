from ....readstdout import checkstdout
from .prog import f as user_sol
from .sol import f as corr_sol


def test():
    assert checkstdout(user_sol, corr_sol, (), float_type=True)
