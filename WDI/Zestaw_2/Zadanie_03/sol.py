# Michał Kobiera
def reverse(x):
    new_x = 0
    while x > 0:
        new_x *= 10
        new_x += x % 10
        x //= 10
    return new_x

def f(num):
    # sprawdzanie czy liczba jest palindromem w systemie dziesiętnym
    if reverse(num) == num:
        dec_pal = True
    else:
        dec_pal = False

    # zamiana na system binarny
    bin_num = 2  # 2 -> partyzancki sposób na zera na początku liczby ("01")
    temp = num
    while temp > 0:
        bin_num *= 10
        bin_num += temp % 2
        temp //= 2
    bin_num = bin_num * 10 + 2

    # sprawdzanie czy liczba jest palindromem w systemi binarnym
    if reverse(bin_num) == bin_num:
        bin_pal = True
    else:
        bin_pal = False

    return (dec_pal, bin_pal)
