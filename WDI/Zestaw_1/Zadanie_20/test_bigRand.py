# Szymon Rusiecki
import pytest
from ....randTemplates.RFloat import RFloat
from ....readstdout import checkstdout
from .prog import f as user_sol
from .sol import f as corr_sol

MIN_RANGE = 0
MAX_RANGE = 10 ** 6
TEST_NUM = 100
BIG_RAND_TESTS = [
    ((RFloat.gen_random(MIN_RANGE, MAX_RANGE),
      RFloat.gen_random(MIN_RANGE, MAX_RANGE)))
    for _ in range(TEST_NUM)]

L_BOUND = MIN_RANGE + 100
U_BOUND = MAX_RANGE - 100
BIG_RAND_RANGE_TESTS = [
    ((RFloat.gen_random(MIN_RANGE, L_BOUND),
      RFloat.gen_random(U_BOUND, MAX_RANGE)))
    for _ in range(TEST_NUM)]


@pytest.mark.order(3)
@pytest.mark.dependency(name="testBigRand_s1z20", depends=["testSmallRand_s1z20"], scope="session")
class TestBig:
    @pytest.mark.parametrize("data", BIG_RAND_TESTS)
    def test_big_rand(self, data):
        assert checkstdout(user_sol, corr_sol, data, float_type=True)

    @pytest.mark.parametrize("data", BIG_RAND_RANGE_TESTS)
    def test_big_rand_big_range(self, data):
        assert checkstdout(user_sol, corr_sol, data, float_type=True)
