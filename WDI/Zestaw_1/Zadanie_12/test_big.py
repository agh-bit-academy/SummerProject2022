# Mikołaj Maślak
import pytest
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint
from ....readstdout import checkstdout

MIN_RANGE = 10
MAX_RANGE = 1000000
TEST_NUM = 100
BIG_RANDOM_TESTS = [
    (randint(MIN_RANGE, MAX_RANGE),
     randint(MIN_RANGE, MAX_RANGE),
     randint(MIN_RANGE, MAX_RANGE))
    for _ in range(TEST_NUM)]

PRIMES_TEST = [
    (917923, 166081, 316621),
    (818171, 863539, 24509),
    (223061, 326597, 756667),
    (319747, 76001, 856081),
    (101183, 911831, 414241),
    (646873, 471959, 383681),
    (118583, 987991, 193577),
    (811297, 30707, 827131),
    (367823, 270443, 7873),
    (781519, 567719, 738217),
    (434267, 949111, 396631),
    (932227, 644491, 918793),
    (237509, 845657, 251467),
    (822221, 676961, 413681),
    (167521, 678023, 693137),
    (427681, 504617, 689033)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_big_s1t12", depends=["test_basic_s1t12"], scope="session")
class TestBig:
    @pytest.mark.parametrize("data", PRIMES_TEST)
    def test_primes_random(self, data):
        assert checkstdout(user_sol, corr_sol, data, float_type=False)

    @pytest.mark.parametrize("data", BIG_RANDOM_TESTS)
    def test_big_random(self, data):
        assert checkstdout(user_sol, corr_sol, data, float_type=False)
