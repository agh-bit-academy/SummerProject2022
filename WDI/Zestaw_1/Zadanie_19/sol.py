# Izabella Rosikoń
def e_number():
    eps = 0.1 ** 10
    prev = 0
    curr = 1
    silnia = 1
    i = 2

    while abs(curr - prev) > eps:
        prev = curr
        curr += (1 / silnia)
        silnia *= i
        i += 1

    print(curr)
