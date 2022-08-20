# Juliusz Wasieleski
def find_longest_sec(tab, row, col):
    n = len(tab)
    m = len(tab[0])
    if row >= n or col >= m:
        return 0
    if row + 1 == n or col + 1 == m:
        return 1
    if row + 2 == n or col + 2 == m:
        return 2

    max_leng = 2
    leng = 1
    q = tab[row][col] / tab[row + 1][col + 1]
    while row + 1 < n and col + 1 < m:
        if tab[row][col] == tab[row + 1][col + 1] * q:
            row += 1
            col += 1
            leng += 1
        else:
            if max_leng < leng:
                max_leng = leng
            leng = 1
            q = tab[row][col] / tab[row + 1][col + 1]
            row += 1
            col += 1
    return max_leng


def f(tab):
    n = len(tab)
    m = len(tab[0])
    max_length = 0
    for i in range(n):
        tmp_length = find_longest_sec(tab, i, 0)
        if tmp_length > max_length:
            max_length = tmp_length

    for i in range(m):
        tmp_length = find_longest_sec(tab, 0, i)
        if tmp_length > max_length:
            max_length = tmp_length
    return max_length
