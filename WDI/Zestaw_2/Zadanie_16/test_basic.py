# Dominik Adamczyk
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol

MIN_RANGE = 1
MAX_RANGE = 1000
TEST_NUM = 40

EDGE_TEST = [1, 2, 3, 4, 5, 6, 7, 22, 27, 58, 85, 94, 121, 166, 202, 265, 274, 319, 346,
             355, 378, 382, 391, 438, 454, 483, 517, 526, 535, 562, 576, 588, 627, 634,
             636, 645, 648, 654, 663, 666, 690, 706, 728, 729, 762, 778, 825, 852, 861,
             895, 913, 915, 922, 958, 985, 1086, 1111, 1165, 1219, 1002]
BASIC_RANDOM_TESTS = RandFixArray(TEST_NUM, MIN_RANGE, MAX_RANGE).get()


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s2t16", scope="session")
class TestBasic:
    @pytest.mark.dependency(name="test_edge_s2t16", scope="session")
    @pytest.mark.parametrize("data", EDGE_TEST)
    def test_edge(self, data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
    def test_small_rand(self, data):
        assert user_sol(data) == corr_sol(data)
