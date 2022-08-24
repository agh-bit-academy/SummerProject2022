# Dominik Adamczyk
# Funkcja zwraca najmniejszą, ze wszystkich możliwych odpowiedzi.
# Inne implementacje mogą dawać różne wyniki, zgodne z treścią zadania.
# Na przykład dla tablicy t = [0, 1, 2] możliwe wyniki to: 0, 1, 2, 3. f(t) zwróci 0

def f(A):
    def rec(A, idx=0, idxsum=0, tabsum=0, emptyans=True):
        if not emptyans and idxsum == tabsum:
            return tabsum
        if len(A) == idx:
            return float("inf")
        anssum1 = rec(A, idx + 1, idxsum + idx, tabsum + A[idx], False)
        anssum2 = rec(A, idx + 1, idxsum, tabsum, emptyans)
        return min(anssum1, anssum2)
    ans = rec(A)
    if ans == float("inf"):
        return None
    return ans
