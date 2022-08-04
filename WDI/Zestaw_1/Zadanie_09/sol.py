# Juliusz Wasieleski

def f(n):
    if n ==2 or n == 3:
        print(1)
        print(n)
    elif n!=0:
        stack = []
        for i in range(1, int(sqrt(n))):
            if n % i == 0:
                print(i)
                stack.append(n // i)

        if n // int(sqrt(n)) == sqrt(n):
            print(int(sqrt(n)))

        while len(stack) > 0:
            i = stack.pop()
            print(i)