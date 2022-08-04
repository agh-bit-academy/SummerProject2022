# Paweł Konopka

# Oznaczenia:
# 1.20(61) -> INTEGER.INDENT(PERIOD)


from math import isqrt
from random import randint


def rand_digit(zero=True):
    return str(
        randint((0 if zero else 1), 9))


def rand_seq(length, zero=False):
    ans = ""
    if length > 0:
        ans += rand_digit(zero)
    for _ in range(length - 1):
        ans += rand_digit()
    return ans


# Special function since 0.(999) = 1 = 69 / 69 and that's problematic to check
# Also 0.(3131) sholud be 0.(31)
def gener_period(period_len):
    ok = False
    while not ok:
        print('iter')
        a = rand_seq(period_len, True)
        ok = is_ok(a)

    return a


def is_ok(seq):
    n = len(seq)
    if n == 1:
        return seq != '9' and seq != '0'
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            if not check_given_len(seq, i) or not check_given_len(seq, n // i):
                return False
    return True


def check_given_len(seq, length):
    n = len(seq)
    if n == length:
        return True

    podseq = [seq[length * x:length * (x+1)] for x in range(n // length)]
    podseq.sort()

    j = 1
    while j < len(podseq):
        if podseq[j-1] != podseq[j]:
            return True
        j += 1

    return False


def gener_test(integr_len, indent_len, period_len):
    if integr_len == 0:
        integer = '0'
    else:
        integer = rand_seq(integr_len)
    indent = rand_seq(indent_len)
    period = gener_period(period_len)

    # Making sure that it's not 0.6(226) since it's just 0.(622)
    if indent_len > 0 and indent[-1] == period[-1]:
        indent = indent[:-1] + str((int(indent[-1]) + 1) % 10)
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


# Maximum denominator that is being simplified because it can take a long time
MAX_OPER = 40_000_000


def decode(integer, indent, period):
    left1 = 1
    left1 *= 10 ** len(indent)

    right1 = int(integer) * left1 + (int(indent) if indent != '' else 0)

    left2 = left1 * 10 ** len(period)
    right2 = right1 * 10 ** len(period) + int(period)

    numerator = right2 - right1
    denominator = left2 - left1

    if denominator < MAX_OPER:
        numerator, denominator = simplify(numerator, denominator)
    print('gdzie')

    # print(get_periodic_form(integer, indent, period))
    # print(numerator, '/', denominator)
    # print(numerator / denominator)

    return numerator, denominator


def get_periodic_form(integer, indent, period):
    return f'{integer}.{indent}({period})'
