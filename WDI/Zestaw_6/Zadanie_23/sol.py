# Sebastian Soczawa
def rek(T, R, res=0, count=0, r1=0, r2=0, i=0):
    if count == 3:
        if res == R:
            return True
        return False
    if i == len(T):
        return False
    if count == 0:
        # - Wybieramy pierwszy opornik, albo
        # - wybieramy pierwszy opornik z myślą dołączenie do niego szeregowo
        # układu dwóch innych podłączonych równolegle, albo
        # - szukamy innego opornika
        return rek(T, R, T[i], count + 1, i, 0, 0) or\
            rek(T, R - T[i], 0, count + 1, i, 0, 0) or\
            rek(T, R, 0, count, 0, 0, i + 1)
    elif count == 1:
        # jeśli już wzięliśmy opornik, to nie możemy go wziąć drugi raz
        if i == r1:
            return rek(T, R, res, count, r1, 0, i + 1)
        else:
            r_serial = res + T[i]
            if (res == 0 and T[r1] != 0) or (res + T[i] == 0):
                r_parallel = T[i]
            else:
                r_parallel = (res * T[i]) / (res + T[i])
            # - Podłączamy kolejny opornik szeregowo, albo
            # - równolegle, albo
            # - szukamy kolejnego opornika
            return rek(T, R, r_serial, count + 1, r1, i, 0) or\
                rek(T, R, r_parallel, count + 1, r1, i, 0) or\
                rek(T, R, res, count, r1, 0, i + 1)
    elif count == 2:
        # jeśli już wzięliśmy opornik, to nie możemy go wziąć drugi raz
        if i == r1 or i == r2:
            return rek(T, R, res, count, r1, r2, i + 1)
        else:
            r_serial = res + T[i]
            if (res == 0 and T[r1] != 0 and T[r2] != 0) or (res + T[i] == 0):
                r_parallel = T[i]
            else:
                r_parallel = (res * T[i]) / (res + T[i])
            # - Podłączamy kolejny opornik szeregowo, albo
            # - równolegle, albo
            # - szukamy kolejnego opornika
            return rek(T, R, r_serial, count + 1, r1, r2, 0) or\
                rek(T, R, r_parallel, count + 1, r1, r2, 0) or\
                rek(T, R, res, count, r1, r2, i + 1)


def f(T, R):
    return rek(T, R)
