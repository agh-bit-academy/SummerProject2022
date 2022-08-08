# Sebastian Soczawa
def f(n):
    if n == 1:  # edge case
        print("NIE")
        return
    var_sum = 1
    for div in range(2, int(n ** 0.5) + 1):
        if n % div == 0:
            var_sum += div + (n / div)
    if var_sum == n:
        print(True)
    else:
        print(False)

# Poniżej funkcja wykorzystująca matematyczne właściwości liczb doskonałych
# Odkomentuj to i zakomentuj poprzednią funkcję
# -------------------(*)----------------------
# def prime(n):
#     if n < 2:
#         return False
#     if n == 2 or n == 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     k = 6
#     while k + 1 < int(n**0.5) + 1:
#         if n % (k - 1) == 0 or n % (k + 1) == 0:
#             return False
#         k += 6
#     return True


# def f(n):
#     pow2 = 2
#     while pow2 <= n:
#         pow2 *= 2
#         if prime(pow2 - 1):
#             if int((pow2 - 1) * pow2 / 2) == n:
#                 print("TAK")
#                 return
#     print("NIE")
# -------------------------------------------
