# Maciej Bartczak
import pytest
from random import randint, shuffle
from .prog import f as user_sol
from .sol import f as correct_sol


def shuffle_number(num):
    digit_list = [int(digit) for digit in str(num)]
    shuffle(digit_list)
    if digit_list[0] == 0:
        for i in range(1, len(digit_list)):
            if digit_list[i] != 0:
                digit_list[0] = digit_list[i]
                break
    return int("".join(map(str, digit_list)))


def generate_test_case(lower_bound, upper_bound):
    num = randint(lower_bound, upper_bound)
    return num, shuffle_number(num)


TEST_CASE_AMOUNT = 100
LOWER_BOUND = 10 ** 50
UPPER_BOUND = 10 ** 51
RANDOM_TESTS = [generate_test_case(LOWER_BOUND, UPPER_BOUND) if case_no % 3 == 0  # let every 3rd test be a false case
                else (randint(LOWER_BOUND, UPPER_BOUND), randint(LOWER_BOUND, UPPER_BOUND))
                for case_no in range(TEST_CASE_AMOUNT)]


@pytest.mark.order(2)
@pytest.mark.dependency(name="test_random_s3t02", depends=["test_basic_s3t02"], scope="session")
@pytest.mark.parametrize("num1, num2", RANDOM_TESTS)
def test_random(num1, num2):
    assert correct_sol(num1, num2) == user_sol(num1, num2)
