# Dominik Adamczyk

def convert(A):
    lena = len(A)
    onesa = [[0 for _ in range(lena)] for _ in range(lena)]
    for y in range(lena):
        for x in range(lena):
            onescnt = 0
            num = A[y][x]
            while num != 0:
                if num % 2 == 1:
                    onescnt += 1
                num //= 2
            onesa[y][x] = onescnt
    return onesa


def f(A, B):
    onesa = convert(A)
    onesb = convert(B)
    lena = len(A)
    lenb = len(B)
    for yb in range(lenb - lena + 1):
        for xb in range(lenb - lena + 1):
            count = 0
            for ya in range(lena):
                for xa in range(lena):
                    if onesa[ya][xa] == onesb[yb + ya][xb + xa]:
                        count += 1
            if (count / (lena * lena)) > (1 / 3):
                return True
    return False
