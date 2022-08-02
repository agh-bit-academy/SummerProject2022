#Julia Smerdel


def f(suma):
    a1, a2, b1, b2 = 1, 1, 1, 1
    fibSuma = 1

    while suma != fibSuma:
        if suma > fibSuma:
            fibSuma += a2
            a1, a2 = a2, a1 + a2
        if suma < fibSuma:
            fibSuma -= b1
            b1, b2 = b2, b1 + b2
        if suma < a2:
            break
    
    print(suma == fibSuma)




