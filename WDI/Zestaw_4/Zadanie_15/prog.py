#Szczepan Rzeszutek
def f(T):
    # wpisz swoje rozwiązanie
    PRIMES = [0, 0, 1, 1, 0, 1, 0, 1, 0, 0]
    n = len(T)
    flag = False
    for i in range(n):
        for j in range(n):
            flag = True
            temp = T[i][j]
            while temp != 0:
                num = temp % 10
                if PRIMES[num] == 1:
                    break
                temp //= 10
            if temp == 0:
                flag = False
                break
        if flag:
            return True

    return False


