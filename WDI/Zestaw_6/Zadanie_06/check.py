# Dominik Adamczyk

def check(A):
    output = set()

    def rec(A, idx=0, idxsum=0, tabsum=0, emptyans=True):
        if len(A) == idx and not emptyans and idxsum == tabsum:
            output.add(tabsum)
        if len(A) == idx:
            return
        rec(A, idx + 1, idxsum + idx, tabsum + A[idx], False)
        rec(A, idx + 1, idxsum, tabsum, emptyans)

    rec(A)
    return output
