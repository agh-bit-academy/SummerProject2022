# Bartłomiej Kozera


def f(x):
    sum = 0
    factorial = 1

    for n in range(10**6):  # im więcej razy wykona się ta pętla, tym dokładniejszy wynik otrzymamy
        if n > 0:
            factorial *= 2*n-1
            factorial *= 2*n
        component = (-1)**n * x**(2*n)
        component /= factorial
        if abs(component) < 10 ** (-6):
            break
        sum += component
    print(sum)

