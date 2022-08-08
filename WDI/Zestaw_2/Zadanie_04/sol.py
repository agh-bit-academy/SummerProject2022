# Jakub Bizan
def f(n):
    variable = 0
    for i in range(1, n + 1):
        flag = True
        help_var = i
        while help_var != 1:
            if help_var % 2 == 0:
                help_var //= 2
                continue
            if help_var % 3 == 0:
                help_var //= 3
                continue
            if help_var % 5 == 0:
                help_var //= 5
                continue
            flag = 0
            break
        if flag:
            variable += 1
    return variable
