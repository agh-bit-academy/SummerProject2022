# Szymon Rusiecki
import pytest
from ....randTemplates.RFloat import RandFixFloat
from ....readstdout import checkstdout
from .prog import f as user_sol
from .sol import f as corr_sol

MIN_RANGE = 0
MAX_RANGE = 100
TEST_NUM = 100
SMALL_RAND_TESTS = [
    ((RandFixFloat.gen_random(MIN_RANGE, MAX_RANGE),
      RandFixFloat.gen_random(MIN_RANGE, MAX_RANGE)))
    for _ in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="testSmallRand_s1t20", depends=["testBasic_s1t20"], scope="session")
@pytest.mark.parametrize("data", SMALL_RAND_TESTS)
def test_small_rand(data):
    assert checkstdout(user_sol, corr_sol, data, float_type=True)
