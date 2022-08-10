# Julia Smerdel
def f(suma):
    a1, a2, b1, b2 = 1, 1, 1, 1
    fib_suma = 1

    while suma != fib_suma:
        if suma > fib_suma:
            fib_suma += a2
            a1, a2 = a2, a1 + a2
        if suma < fib_suma:
            fib_suma -= b1
            b1, b2 = b2, b1 + b2
        if suma < a2:
            break

    print(suma == fib_suma)
