# 1,20(61) -> INTEGER,INDENT(PERIOD)


from math import isqrt
from random import randint


def rand_digit(zero=True):
    return str(
        randint((0 if zero else 1), 9))

def rand_seq(length):
    ans = ""
    if length > 0:
        ans += rand_digit(False)
    for _ in range(length - 1):
        ans += rand_digit()
    return ans

# Special function since 0,(999) = 1 = 69 / 69 and that's problematic to check
def gener_period(period_len):
    ok = False
    while not ok:
        a = rand_seq(period_len)
        for x in a:
            if x != '9': 
                ok = True
                break

    return a


def gener_test(integr_len, indent_len, period_len):
    if integr_len == 0:
        integer = '0'
    else:
        integer = rand_seq(integr_len)
    indent = rand_seq(indent_len)
    period = gener_period(period_len)
    return integer, indent, period


def simplify(a, b):
    integr = a // b
    a -= integr * b

    if b % a == 0:
        b //= a
        a = 1

    else:
        while a % 2 == 0 and b % 2 == 0:
            a //= 2
            b //= 2

        for i in range(3, max(isqrt(b) + 1, a // 2), 2):
            while a % i == 0 and b % i == 0:
                a //= i
                b //= i

    return a + integr * b, b      


def decode(integer, indent, period):
    left1 = 1
    left1 *= 10 ** len(indent)

    right1 = int(integer) * left1 + (int(indent) if indent != '' else 0)

    left2 = left1 * 10 ** len(period)
    right2 = right1 * 10 ** len(period) + int(period)

    numerator = right2 - right1
    denominator = left2 - left1

    numerator, denominator = simplify(numerator, denominator)

    # print(get_periodic_form(integer, indent, period))
    # print(numerator, '/', denominator)
    # print(numerator / denominator)

    return numerator, denominator


def get_periodic_form(integer, indent, period):
    return f'{integer}.{indent}({period})'


for _ in range(10):
    a, b, c = gener_test(0, 0, 3)
    # print(a, b, c)
    print(get_periodic_form(a, b, c))
    l, m = decode(a, b, c)

    print(l, '/', m)
    print('')