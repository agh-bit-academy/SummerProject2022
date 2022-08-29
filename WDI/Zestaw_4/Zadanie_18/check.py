# Szymon Ożóg
def f(A):
    max_sum = 0
    for i in range (len(A)):
        for p in range(len(A[0])):
            for q in range(p, min(len(A[0]), p + 10)):
                temp_sum = 0
                for k in range(p, q + 1):
                    temp_sum += A[i][k]
                max_sum = max(max_sum, temp_sum)
    
    for j in range(len(A[0])):
        for p in range(len(A)):
            for q in range(min(len(A), p + 10)):
                temp_sum = 0
                for k in range(p, q + 1):
                    temp_sum += A[k][j]
                max_sum= max(max_sum, temp_sum)
    return max_sum