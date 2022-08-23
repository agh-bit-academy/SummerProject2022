# Bartłomiej Kozera
def f(A, k):
    moves = [(2, 1), (1, 2), (2, -1), (1, -2)]  # Ruchy skoczka tylko w dol szachownicy
    n = len(A)
    m = len(A[0])
    counter = 0
    for i in range(n - 1):  # Kiedy patrze ruchami skoczka w dół, nie musze iterować do końca tablicy
        for j in range(m):
            for el in moves:
                y, x = i + el[0], j + el[1]
                if y < n and 0 <= x < m:
                    curr_num = A[i][j] * A[y][x]
                    if curr_num == k:
                        counter += 1
    return counter
