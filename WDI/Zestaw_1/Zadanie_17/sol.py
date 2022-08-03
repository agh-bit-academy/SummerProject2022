# Andrzej Karcinski

EPSILON = 10 ** -7


def f(a=1, b=1):
    bounder = 1
    c = a + b
    while bounder > EPSILON:
        quotient_before = c / b
        a, b = b, a + b
        c = a + b
        quotient_after = c / b
        bounder = abs(quotient_before - quotient_after)
    print(quotient_after)
