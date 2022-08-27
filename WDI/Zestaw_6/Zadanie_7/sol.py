# Szczepan Rzeszutek
def f(T, M, i=0):
    if M == 0:
        return True
    if i == len(T):
        return False
    return f(T, M - T[i], i + 1) or f(T, M, i + 1)
