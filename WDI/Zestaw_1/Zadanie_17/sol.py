# Andrzej Karcinski
def f(a, b):
    epsilon = 10 ** (-7)
    bounder = 1
    c = a + b
    while bounder > epsilon:
        quotient_before = c / b
        a, b = b, a + b
        c = a + b
        quotient_after = c / b
        bounder = abs(quotient_before - quotient_after)
    print(quotient_after)
