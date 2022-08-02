#Julia Smerdel

def czyIstniejeFib(liczba):
    a1, a2, b1, b2 = 1, 1, 1, 1
    fibSuma = 1

    while liczba != fibSuma:
        if liczba > fibSuma:
            fibSuma += a2
            a1, a2 = a2, a1 + a2
        if liczba < fibSuma:
            fibSuma -= b1
            b1, b2 = b2, b1 + b2
        if liczba < a2:
            break
    
    return(liczba == fibSuma)


def f(n):
    while czyIstniejeFib(n+1):
        n += 1
    
    print(n + 1)
    

