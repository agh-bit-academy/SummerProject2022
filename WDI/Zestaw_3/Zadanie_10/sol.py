# Karolina Kucia
def f(A):
    n = len(A)
    if n <= 2:
        return n

    diff = A[1] - A[0]
    max_length = 1
    curr_length = 1
    for i in range(1, n):
        if A[i] == A[i - 1] + diff:
            curr_length += 1
        else:
            max_length = max(max_length, curr_length)
            curr_length = 2
            diff = A[i] - A[i - 1]
    return max(max_length, curr_length)
