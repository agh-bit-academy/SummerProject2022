# Kacper Słoniec

def f(arr):
    maxi = 0
    n = len(arr)
    for i in range(n):
        for j in range(n - 1, -1, -1):
            k = 0
            length = 0
            while i + k < n and j - k >= 0 and arr[i + k] % 2 == 1 and arr[i + k] == arr[j - k]:
                k += 1
                length += 1
            if j - k + 1 == i and length > maxi:
                maxi = length
    return maxi
