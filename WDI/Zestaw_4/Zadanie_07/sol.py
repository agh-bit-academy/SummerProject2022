# Sebastian Soczawa
# Algorytm polega na ciągłym braniu minimum z pierwszych elementów w wierszach
def f(A, B):
    n = len(A)
    row_index = [0 for _ in range(n)]  # aktualny indeks dla danego wiersza
    i_b = 0  # indeks w tablicy b
    for _ in range(n * n):
        curr_min = float("inf")
        for j in range(n):
            if row_index[j] < n and curr_min > A[j][row_index[j]]:
                curr_min = A[j][row_index[j]]
                row_i = j
        B[i_b] = curr_min   # przepisuję liczbę do tablicy
        row_index[row_i] += 1   # przesuwam indeks o 1 w prawo
        i_b += 1
    return B
