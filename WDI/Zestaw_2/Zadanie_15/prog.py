# Szczeapan Rzeszutek
def f(n):
    if n < 1:
        return
    for num in range(10 ** (n - 1), 10 ** n):
        var_sum = 0
        num_cp = num
        while num > 0:
            var_sum += (num % 10) ** n
            num //= 10
        if var_sum == num_cp:
            print(var_sum, end=" ")
