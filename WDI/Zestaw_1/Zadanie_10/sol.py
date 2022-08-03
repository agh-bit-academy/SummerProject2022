# Sebastian Soczawa
def f():
    for i in range(2, 1000000):
        sum = 1
        for div in range(2, int(i**0.5)+1):
            if i % div == 0:
                sum += div + i/div
        if sum == i:
            print(i)

# Żeby testy działały krócej należy zmienić 1000000 na coś mniejszego,
# albo użyć funkcji f poniżej, która opiera się na matematycznych właściwościach liczb doskonałych
# Hint: Są 4 liczby doskonałe mniejsze od miliona, wszystkie mniejsze od 10 000
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


# def f(n=4):
#     pow2 = 2
#     while n > 0:
#         pow2 *= 2
#         if prime(pow2 - 1):
#             print(int((pow2 - 1) * pow2 / 2))
#             n -= 1
# -------------------------------------------
