# Andrzej Karciński
def f(A):
    is_zero_in_row = [False for _ in range(len(A))]
    is_zero_in_col = [False for _ in range(len(A[0]))]

    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] == 0:
                is_zero_in_row[i] = True
                is_zero_in_col[j] = True

    for i in range(len(A)):
        if is_zero_in_row[i] is False:
            return False
    for i in range(len(A[0])):
        if is_zero_in_col[i] is False:
            return False

    return True
