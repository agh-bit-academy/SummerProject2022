# Andrzej Karcinski

EPSILON = 10 ** -7


def f(a=1, b=1):
    bounder = 1
    c = a + b
    while bounder > EPSILON:
        quotientBefore = c / b
        a, b = b, a + b
        c = a + b
        quotientAfter = c / b
        bounder = abs(quotientBefore - quotientAfter)
    print(quotientAfter)
