# Bartłomiej Kozera
def f(A):
    n, m = len(A), len(A[0])
    curr_num = 1
    max_num = n * m
    x, y = 0, 0
    while curr_num <= max_num:
        while x < m - 1 and A[y][x + 1] == 0:
            A[y][x] = curr_num
            x += 1
            curr_num += 1
        while y < n - 1 and A[y + 1][x] == 0:
            A[y][x] = curr_num
            y += 1
            curr_num += 1
        while x > 0 and A[y][x - 1] == 0:
            A[y][x] = curr_num
            x -= 1
            curr_num += 1
        while y > 0 and A[y - 1][x] == 0:
            A[y][x] = curr_num
            y -= 1
            curr_num += 1
    return A
