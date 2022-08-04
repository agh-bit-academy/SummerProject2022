# Szczeapan Rzeszutek
def f(n):
    if n < 1:
        return
    for num in range(10**(n-1), 10**n):
        sum = 0
        numCp = num
        while num > 0:
            sum += (num % 10) ** n
            num //= 10
        if sum == numCp:
            print(sum, end = " ")
