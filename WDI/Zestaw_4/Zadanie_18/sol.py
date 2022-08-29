# Szymon Ożóg
def sum_horizontal(A):
    max_sum = 0
    sum_prefix_h = [[A[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(1, len(A[0])):
            sum_prefix_h[i][j] += sum_prefix_h[i][j - 1]

    if len(A[0]) <= 10:
        for i in range(len(A)):
            max_sum = max(max_sum, sum_prefix_h[i][len(A[0]) - 1])
    else:
        for i in range(len(A)):
            max_sum = max(max_sum, sum_prefix_h[i][9])
            for j in range(10, len(A[0])):
                max_sum = max(max_sum, sum_prefix_h[i][j] - sum_prefix_h[i][j - 10])
    return max_sum


def sum_vertically(A):
    max_sum = 0
    sum_prefix_v = [[A[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    for j in range(len(A[0])):
        for i in range(1, len(A)):
            sum_prefix_v[i][j] += sum_prefix_v[i - 1][j]

    if len(A) <= 10:
        for j in range(len(A[0])):
            max_sum = max(max_sum, sum_prefix_v[len(A) - 1][j])
    else:
        for j in range(len(A[0])):
            max_sum = max(max_sum, sum_prefix_v[9][j])
            for i in range(10, len(A)):
                max_sum = max(max_sum, sum_prefix_v[i][j] - sum_prefix_v[i - 10][j])
    return max_sum


def f(A):
    return max(sum_horizontal(A), sum_vertically(A))
