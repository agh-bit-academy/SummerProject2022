# Sebastian Soczawa
def f(A):
    n = len(A)
    m = len(A[0])
    counter = 0
    row, column = 0, -1
    size_m = m
    size_n = n
    while counter < n * m:
        for _ in range(size_m):
            counter += 1
            column += 1
            A[row][column] = counter
        size_n -= 1
        if size_n < 1:
            break
        for _ in range(size_n):
            counter += 1
            row += 1
            A[row][column] = counter
        size_m -= 1
        if size_m < 1:
            break
        for _ in range(size_m):
            counter += 1
            column -= 1
            A[row][column] = counter
        size_n -= 1
        if size_n < 1:
            break
        for _ in range(size_n):
            counter += 1
            row -= 1
            A[row][column] = counter
        size_m -= 1
    return A
