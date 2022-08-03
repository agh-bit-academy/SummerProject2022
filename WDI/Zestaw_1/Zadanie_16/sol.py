# Sebastian Soczawa

def f():
    maxSteps = 0
    solution = 2
    for i in range(2, 10001):
        steps = 0
        a = i
        while a != 1:
            a = (a % 2) * (3 * a + 1) + (1 - a % 2) * (a / 2)
            steps += 1
        if maxSteps < steps:
            maxSteps = steps
            solution = i

    print(solution)
