# Julia Smerdel
import pytest
from ....Rand_Templates.RandFixFloat import RandFixFloat
from ....readstdout import checkstdout
from .prog import f as user_sol
from .sol import f as corr_sol

MIN_RANGE = 0
MAX_RANGE = 10 ** 6
TEST_NUM = 100
BIG_RAND_TESTS = [
    (RandFixFloat.gen_random(MIN_RANGE, MAX_RANGE))
    for _ in range(TEST_NUM)]

SHIFT = 100
L_BOUND = MIN_RANGE + SHIFT
U_BOUND = MAX_RANGE - SHIFT
BIG_RAND_RANGE_TESTS = [
    (RandFixFloat.gen_random(MIN_RANGE, L_BOUND))
    for _ in range(TEST_NUM)]


@pytest.mark.order(3)
@pytest.mark.dependency(name="test_big_rand_s1t09", depends=["test_small_rand_s1t09"], scope="session")
class TestBig:
    @pytest.mark.parametrize("data", BIG_RAND_TESTS)
    def test_big_rand(self, data):
        assert checkstdout(user_sol, corr_sol, data, float_type=True)

    @pytest.mark.parametrize("data", BIG_RAND_RANGE_TESTS)
    def test_big_rand_big_range(self, data):
        assert checkstdout(user_sol, corr_sol, data, float_type=True)
