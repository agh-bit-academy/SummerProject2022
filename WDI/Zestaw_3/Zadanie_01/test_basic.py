# Karolina Kucia
import pytest
from random import randint
from .prog import f as user_sol
from .sol import f as corr_sol


BASIC_TESTS = [
    (1, 2),
    (1, 15),
    (10, 2),
    (10, 3),
    (15, 4),
    (15, 7),
    (2137, 11),
    (246, 13),
    (25, 14),
    (997, 16)
]

MIN_RANGE = 1
MAX_RANGE = 200
TEST_NUM = 10
BASE_LRANGE = 2
BASE_RRANGE = 16

BASIC_RANDOM_TESTS = [(randint(MIN_RANGE, MAX_RANGE), randint(BASE_LRANGE, BASE_RRANGE))
                      for _ in range(TEST_NUM)]


@pytest.mark.order(1)
@pytest.mark.dependency(name="test_basic_s3t1", scope="session")
class TestBasic:
    @pytest.mark.parametrize("data", BASIC_TESTS)
    def test_basic(self, data):
        assert user_sol(*data) == corr_sol(*data)

    @pytest.mark.parametrize("data", BASIC_RANDOM_TESTS)
    def test_basic_random(self, data):
        assert user_sol(*data) == corr_sol(*data)
