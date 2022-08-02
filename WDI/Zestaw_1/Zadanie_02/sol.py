# Krzysztof Mach


def f(increasing=True):
    """
    Znajduje i zwraca początkowe wyrazy o najmniejszej sumie ciągu analogicznego do Fibonacciego
    zawierającego liczbę bieżącego roku (w tym przypadku 2022)

    WAŻNE - domyślnie drugi wyraz zawsze większy od drugiego, aby drugi mógł być mniejszy,
    dopisać False do argumentów. To zmienia wynik.
    """
    year = 2022
    min_sum = year + 1  # zawsze możliwym rozwiązaniem jest 1 + (year - 1), więc aby je znalazło taka suma na start
    min_tuple = (-1, -1)
    a, b = 1, 1
    while a + b < min_sum:
        while a + b < min_sum:
            fib_a, fib_b = a, b
            while fib_a + fib_b < year:
                fib_a, fib_b = fib_b, fib_a + fib_b
                if fib_a + fib_b == year:
                    min_sum = a + b
                    min_tuple = (a, b)
            b += 1
        a += 1
        b = a if increasing else 1
    return min_tuple


print(f())
