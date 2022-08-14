# Izabella Rosikoń
def f(T):
    count = 2
    save = 0
    for i in range(1, len(T) - 2):
        if T[i] ** 2 == T[i + 1] * T[i - 1]:
            count += 1
        elif T[i] ** 2 != T[i + 1] * T[i - 1]:
            if count > save:
                save = count
                count = 2
            else:
                count = 2
    if save >= count:
        return save
    else:
        return count
