# Andrzej Karciński
import sympy

def f(n):
    x = sympy.primepi(n)
    if sympy.isprime(n):
        x -= 1
    return x
