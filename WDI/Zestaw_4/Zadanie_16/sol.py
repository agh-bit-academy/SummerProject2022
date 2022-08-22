# Szymon Wójcik


def isprime(n):
    if n<2:
        return False
    elif n == 2:
        return True
    i=2
    while i<= int(n**0.5) + 1:
        if n%i==0:
            return False
        i+=1
    return True


def war(n):
    while n > 0:
        x = n%10
        n = n//10
        if x not in [2, 3, 5, 7, 9]:
            return False
    
    return True



def f(A):
    for i in A:
        for j in i:
            if not isprime(j) and war(j):
                return True
    return False