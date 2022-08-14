# Mikołaj Maślak
import pytest
from .prog import f as user_sol
from .sol import f as corr_sol
from .seq_generator import generate_test

MIN_RANGE = -100
MAX_RANGE = 200
ARITHMETIC_RANGE = 50
SEQ_AMMOUNT = 400
TUPLE_LEN = 1000
TEST_NUM = 50
BIG_RANDOM_TESTS = [
    generate_test(MIN_RANGE, MAX_RANGE, TUPLE_LEN, ARITHMETIC_RANGE, SEQ_AMMOUNT)
    for _ in range(TEST_NUM)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_big_s3t12", depends=["test_small_s3t12"], scope="session")
@pytest.mark.parametrize("data", BIG_RANDOM_TESTS)
def test_big(data):
    assert user_sol(data) == corr_sol(data)
