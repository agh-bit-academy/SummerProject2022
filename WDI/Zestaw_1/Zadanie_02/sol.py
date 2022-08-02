# Krzysztof Mach


def f(increasing=True):
    """
    Znajduje i zwraca początkowe wyrazy o najmniejszej sumie ciągu analogicznego do Fibonacciego
    zawierającego liczbę bieżącego roku (w tym przypadku 2022)

    WAŻNE - domyślnie drugi wyraz zawsze większy od drugiego, aby drugi mógł być mniejszy,
    dopisać False do argumentów. To zmienia wynik.
    """
    year = 2022
    minSum = year + 1  # zawsze możliwym rozwiązaniem jest 1 + (year - 1), więc aby je znalazło taka suma na start
    minTuple = (-1, -1)
    a, b = 1, 1
    while a + b < minSum:
        while a + b < minSum:
            fibA, fibB = a, b
            while fibA + fibB < year:
                fibA, fibB = fibB, fibA + fibB
                if fibA + fibB == year:
                    minSum = a + b
                    minTuple = (a, b)
            b += 1
        a += 1
        b = a if increasing else 1
    return minTuple
