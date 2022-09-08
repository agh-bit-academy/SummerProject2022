# Sebastian Soczawa
def prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    k = 6
    k_range = int(n ** 0.5) + 1
    while k <= k_range:
        if n % (k - 1) == 0 or n % (k + 1) == 0:
            return False
        k += 6
    return True

def bin_to_dec(n):
    num = 0
    i = 0
    while n > 0:
        num += (n % 10) * (2 ** i)
        n //= 10
        i += 1
    return num
    
def rek(A, i, number = 0, count = 0, possible = False):
    if i == len(A):
        if count == 1:
            return False
        return possible
    if count > 5:
        return False
    # if number == 0 and A[i] == 0: # Tutaj zabezpieczenie, jeśli liczb binarna zaczyna się od zera
    #     return False
    number = number * 10 + A[i]
    dec_number = bin_to_dec(number)
    if prime(dec_number):
        return rek(A, i + 1, 0,  count + 1, True) or \
               rek(A, i + 1, number, count, False)
    return rek(A, i + 1, number, count, False)

def f(A):
    return rek(A, 0)
