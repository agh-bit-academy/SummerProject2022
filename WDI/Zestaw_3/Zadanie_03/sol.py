# Andrzej Karciński

def f(n):
    isPrime = [True for _ in range(n)]
    isPrime[0] = False
    isPrime[1] = False
    numOfPrimes = 0
    for i in range(2, n):
        if isPrime[i]:
            numOfPrimes += 1
            # warto zauważyć, że jeżeli i to liczba pierwsza to sitem eliminujemy jej wielokrotności stąd step = i,
            # oraz zaczynamy eliminację od 2 * i
            for j in range(i + i, n, i):
                isPrime[j] = False
    return numOfPrimes
