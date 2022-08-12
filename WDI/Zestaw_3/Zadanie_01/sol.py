# Juliusz Wasieleski
def f(n, p):
    letters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    output = ""
    while n > 0:
        output = letters[n % p] + output
        n //= p
    return output
