# Juliusz Wasieleski
def f(A):
    if len(A[0]) == 0:
        return 0
    n = len(A)
    m = len(A[0])
    sum_of_rows = [sum(A[i]) for i in range(n)]
    sum_of_cols = [sum(A[i][j] for i in range(n)) for j in range(m)]
    max_val = -(float('inf'))
    x1, y1, x2, y2 = 0, 0, 0, 0
    for row1 in range(n):
        for col1 in range(m):
            for row2 in range(n):
                for col2 in range(m):
                    if row1 == row2 and col1 == col2:
                        tmp_val = sum_of_rows[row1] + sum_of_cols[col1] - 2 * A[row1][col1]
                    elif row1 == row2:
                        tmp_val = sum_of_rows[row1] + sum_of_cols[col1] + sum_of_cols[col2] - 2 * A[row1][col1] - 2 * \
                            A[row2][col2]
                    elif col1 == col2:
                        tmp_val = sum_of_rows[row1] + sum_of_cols[col1] + sum_of_rows[row2] - 2 * A[row1][col1] - 2 * \
                            A[row2][col2]
                    else:
                        tmp_val = sum_of_rows[row1] + sum_of_cols[col1] + sum_of_rows[row2] + sum_of_cols[col2] - 2 * \
                            A[row1][col1] - 2 * A[row2][col2] - A[row1][col2] - A[row2][col1]
                    if tmp_val > max_val:
                        max_val = tmp_val
                        x1, y1, x2, y2 = row1, col1, row2, col2

    return x1, y1, x2, y2
