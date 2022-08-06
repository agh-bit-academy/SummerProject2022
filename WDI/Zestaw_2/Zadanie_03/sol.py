# Michał Kobiera

def f(num):
    def reverse(x):
        newX = 0
        while x > 0:
            newX *= 10
            newX += x % 10
            x //= 10
        return newX

    # sprawdzanie czy liczba jest palindromem w systemie dziesiętnym
    if reverse(num) == num:
        decPal = True
    else:
        decPal = False

    # zamiana na system binarny
    binNum = 2  # 2 -> partyzancki sposób na zera na początku liczby ("01")
    temp = num
    while temp > 0:
        binNum *= 10
        binNum += temp % 2
        temp //= 2
    binNum = binNum * 10 + 2

    # sprawdzanie czy liczba jest palindromem w systemi binarnym
    if reverse(binNum) == binNum:
        binPal = True
    else:
        binPal = False

    return (decPal, binPal)
