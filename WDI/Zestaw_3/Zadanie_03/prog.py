# Andrzej Karciński
# Znalazłem jakieś ciekawsze sito 
# zwykłe eratostenesa ma O(N log log N)
# to ma O( N/ log log N)
def f(limit):
    sol = 0
    # 2 and 3 are known
    # to be prime
    if limit > 2:
        sol += 1
    if limit > 3:
        sol += 1
 
    # Initialise the sieve
    # array with False values
    sieve = [False] * (limit + 1)
    for i in range(0, limit + 1):
        sieve[i] = False
 
    x = 1
    while x * x <= limit:
        y = 1
        while y * y <= limit:
 
            # Main part of
            # Sieve of Atkin
            n = (4 * x * x) + (y * y)
            if (n <= limit and (n % 12 == 1 or
                                n % 12 == 5)):
                sieve[n] ^= True
 
            n = (3 * x * x) + (y * y)
            if n <= limit and n % 12 == 7:
                sieve[n] ^= True
 
            n = (3 * x * x) - (y * y)
            if (x > y and n <= limit and
                    n % 12 == 11):
                sieve[n] ^= True
            y += 1
        x += 1
 
    # Mark all multiples of
    # squares as non-prime
    r = 5
    while r * r <= limit:
        if sieve[r]:
            for i in range(r * r, limit+1, r * r):
                sieve[i] = False
 
        r += 1
 
        # Print primes
    # using sieve[]
    for a in range(5, limit):
        if sieve[a]:
            sol += 1
    return sol
