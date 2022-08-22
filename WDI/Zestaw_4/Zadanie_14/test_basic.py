# Dominik Adamczyk

import pytest
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint
from ....Rand_Templates.RandFixMatrix import RandFixMatrix


A_LEN_MIN = 2
A_LEN_MAX = 5
RANGE_MIN = 1
RANGE_MAX = 10
B_LEN_MIN = 4
B_LEN_MAX = 8
TEST_NUM = 20


def create_test(amin, amax, bmin, bmax, notest, minrange, maxrange):
    output = []
    for _ in range(notest):
        blen = randint(bmin, bmax)
        alen = randint(amin, min(blen - 1, amax))
        output.append([RandFixMatrix(alen, alen, minrange, maxrange).get(),
                       RandFixMatrix(blen, blen, minrange, maxrange).get()])
    return output


EDGE_TESTS = [
    [[[3, 3],
      [3, 3]],
     [[2, 2, 2],
      [2, 2, 2],
      [2, 2, 2]]],

    [[[3, 3],
      [3, 3]],
     [[2, 2, 2],
      [2, 2, 3],
      [2, 2, 3]]],

    [[[3, 3],
      [3, 3]],
     [[2, 2, 2],
      [2, 2, 2],
      [2, 3, 3]]],

    [[[3, 3],
      [3, 3]],
     [[3, 2, 3],
      [2, 2, 2],
      [3, 2, 3]]],

    [[[3, 3],
      [3, 3]],
     [[2, 2, 2],
      [2, 2, 2],
      [2, 3, 2]]],

    [[[1]],
     [[2, 2, 2],
      [2, 2, 2],
      [2, 3, 2]]],

    [[[3]],
     [[2, 2, 2],
      [2, 2, 2],
      [2, 2, 2]]],

    [[[1]],
     [[3]]],

    [[[5]],
     [[3]]],

    [[[7, 3],
      [5, 7]],
     [[2, 2, 5],
      [2, 3, 2],
      [2, 3, 2]]]
]
BASIC_RAND_TESTS = create_test(A_LEN_MIN, A_LEN_MAX, B_LEN_MIN, B_LEN_MAX, TEST_NUM, RANGE_MIN, RANGE_MAX)


@pytest.mark.order(1)
class TestBasic:
    @pytest.mark.dependency(name="test_edge_s4t14", scope="session")
    @pytest.mark.parametrize("data", EDGE_TESTS)
    def test_edge(self, data):
        assert user_sol(data[0], data[1]) == corr_sol(data[0], data[1])

    @pytest.mark.dependency(name="test_basic_s4t14", scope="session")
    @pytest.mark.parametrize("data", BASIC_RAND_TESTS)
    def test_small(self, data):
        assert user_sol(data[0], data[1]) == corr_sol(data[0], data[1])
