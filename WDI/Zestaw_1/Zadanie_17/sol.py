# Andrzej Karcinski


def f(a=1, b=1):
    epsilon = 10 ** -7
    bounder = 1
    c = a + b
    while bounder > epsilon:
        quotientBefore = c / b
        a, b = b, a + b
        c = a + b
        quotientAfter = c / b
        bounder = abs(quotientBefore - quotientAfter)
    print(quotientAfter)
