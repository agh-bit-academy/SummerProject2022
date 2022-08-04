# Jakub Bizan
def f(n):
    variable = 0
    for i in range(1, n+1):
        flag = True
        pom = i
        while pom != 1:
            if pom % 2 == 0:
                pom //= 2
                continue
            if pom % 3 == 0:
                pom //= 3
                continue
            if pom % 5 == 0:
                pom //= 5
                continue
            flag = 0
            break
        if flag:
            variable += 1
    return variable
