# Mikołaj Maślak
import pytest
from .prog import f as user_sol
from .sol import f as corr_sol
from .seq_generator import generate_test

MIN_RANGE = 0
MAX_RANGE = 20
ARITHMETIC_RANGE = 10
SEQ_AMMOUNT = 10
TUPLE_LEN = 30
TEST_NUM = 50
SMALL_RANDOM_TESTS = [
    generate_test(MIN_RANGE, MAX_RANGE, TUPLE_LEN, ARITHMETIC_RANGE, SEQ_AMMOUNT)
    for _ in range(TEST_NUM)]

SMALL_TESTS = [
    (1, 0, 1, 0, 1, 0, 1, 0, 1, 0),
    (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    (0, 0, 0, 0, 0),
    (5, 5, 6, 6, 7, 7, 6, 6),
    (5, 1, 6, 2, 7, 3, 8, 5)
]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_small_s3t12", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", SMALL_TESTS)
    def test_small(self, data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize("data", SMALL_RANDOM_TESTS)
    def test_small_random(self, data):
        assert user_sol(data) == corr_sol(data)
