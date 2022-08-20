# Andrzej Karciński
import pytest
from .prog import f as user_sol
from .sol import f as corr_sol
from .random_size_matrix import random_size_matrix

TEST_ARRAY = [
    [[0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 1]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0], [0], [0], [0], [0], [0]],
    [[1], [1], [1], [1], [1], [1]],
    [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]]
]

TEST_NUMBER = 100
MIN_SIZE = 20
MAX_SIZE = 50

TEST_RANDOM_ARRAY = [
    random_size_matrix(MIN_SIZE, MAX_SIZE)
    for _ in range(TEST_NUMBER)]


@pytest.mark.dependency(name="test_rand_s4t10", scope="session")
class TestRandom:
    @pytest.mark.parametrize("data", TEST_ARRAY)
    def test_basic(self, data):
        assert user_sol(data) == corr_sol(data)

    @pytest.mark.parametrize("data", TEST_RANDOM_ARRAY)
    def test_random(self, data):
        assert user_sol(data) == corr_sol(data)
