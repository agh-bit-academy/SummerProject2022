# Paweł Konopka

# def f(l, m, sol):
#     print(sol)
#     # Tutaj wprowadź swój kod
#     pass

# Rozwiązanie podebrane z wiki

def find_expansion(a, b):
    digits = []
    modulo = []

    while a > 0:
        a *= 10
        digits.append(a // b)

        if a not in modulo:
            modulo.append(a)
        else:
            break

#        print("a:", a)

        a %= b

#        print("digits:", digits)
#        print("modulo:", modulo)

    if a == 0:
        return "".join(map(str, digits))

    repeating_from = modulo.index(a)

    return "".join(map(str, digits[:repeating_from])) + "(" + "".join(map(str, digits[repeating_from:-1])) + ")"


def f(a, b):
    print(a // b, "." if a % b != 0 else "", sep="", end="")
    a %= b

    print(find_expansion(a, b))
