# Mikołaj Maślak
import pytest
from ....Rand_Templates.RandFixArray import RandFixArray
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint



SIZE = 1000
TEST_NUM = 50
FIB_INDEXES = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
MIN_RANGE = 1
MAX_RANGE = 100000

BIG_RANDOM_TEST = [RandFixArray(SIZE, MIN_RANGE, MAX_RANGE).get() for _ in range(TEST_NUM)]
for fib_index in FIB_INDEXES:
    BIG_RANDOM_TEST[fib_index] = randint(1, 5) * randint(MIN_RANGE, MAX_RANGE)

BIG_PRIMES_TEST = [6194477389, 8679184303, 9127519153, 4620918451, 8914927831, 2576618873, 9398214823,
 4224499583, 2584211501, 9035786077, 5032543963, 1621780267, 9510134939, 8174041669, 6431561107, 4679181791,
  9936187267, 1279785061, 1514742283, 8725180441, 4258810091, 9607575563, 3817588457, 1421303867, 8067281029,
   5092825477, 9442897859, 1028521177, 6309455813, 9529269059]



@pytest.mark.order(2)
@pytest.mark.dependency(name="test_big_s3t15", depends=["test_basic_s3t15"], scope="session")
class TestBig:
    @pytest.mark.parametrize("data", BIG_RANDOM_TEST)
    def test_big_random(data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize("data", BIG_RANDOM_TEST)
    def test_big_primes(data):
        assert user_sol(data) == corr_sol(data)