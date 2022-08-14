# Andrzej Karciński
def f(n):
    is_prime = [True for _ in range(n)]
    is_prime[0] = False
    is_prime[1] = False
    num_of_primes = 0
    for i in range(2, n):
        if is_prime[i]:
            num_of_primes += 1
            # warto zauważyć, że jeżeli i to liczba pierwsza to sitem eliminujemy jej wielokrotności stąd step = i,
            # oraz zaczynamy eliminację od 2 * i
            for j in range(i + i, n, i):
                is_prime[j] = False
    return num_of_primes
