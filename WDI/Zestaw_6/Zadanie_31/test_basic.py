# Sebastian Soczawa
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol


BASIC_TESTS = [(2, 2),
               (60, 71),
               (1, 0),
               (0, 0),
               (31, 31),
               (10, 17),
               (6, 11),
               (1024, 2),
               (42, 95)]

L_RANGE = 3
R_RANGE = 1000
TEST_NUM = 21

BASIC_RANDOM_TESTS = RandFixArray(TEST_NUM, L_RANGE, R_RANGE).get()


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s6t31", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data, answer", BASIC_TESTS)
    def test_basic(self, data, answer):
        assert user_sol(data) == answer

    @pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
    def test_basic_random(self, data):
        assert user_sol(data) == corr_sol(data)
